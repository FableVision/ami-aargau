from flask import Flask, request, jsonify
from flask_cors import CORS

# Setup
app = Flask(__name__)
CORS(app)

submittedAnswers = {}

# Routers, they just call the functions below
@app.route('/', methods=['GET'])
def hello():
    return "Working Website!"

@app.route('/receive', methods=['POST'])
def receive_data():

    data = request.get_json()
    received_string = data.get('message', '')
    print(f"Received Message: {received_string}")

    group = request.args.get('group', 'NOGROUP')
    question = request.args.get('question', -1)
    answer = request.args.get('answer', "NOANSWER")
    
    handleMessageReceived(group, question, answer)
    return jsonify({"status": "success", "received": received_string})

@app.route('/send', methods=['GET'])
def send_data():
    print(f"Got send request!")

    group = request.args.get('group', 'NOGROUP')
    question = request.args.get('question', -1)

    response = handleSendMessageRequest(group, question)
    print(response)

    return jsonify({"message": response})



# Actual game logic


def handleMessageReceived(group, question, answer):
    global submittedAnswers

    print(f"{group}, {question}, {answer}")

    # handle resetting everything
    if(answer == "FULLRESETALL"):
        print("Resetting everything")
        submittedAnswers.clear()
        return

    if (answer == "FULLRESET"):
        print("Resetting group: " + group)
        submittedAnswers.pop(group, None)
        return

    # otherwise, add it to the list
    if(not group in submittedAnswers):
        submittedAnswers[group] = {}
    
    if(not (question in submittedAnswers[group])):
        submittedAnswers[group][question] = []
    
    submittedAnswers[group][question].append(answer)
    print(f"Added {group} {question}, answer: {answer}")

def handleSendMessageRequest(group, question):
    global submittedAnswers

    response = f"You're asking about: {group} {question}"
    
    found = ""
    if(group in submittedAnswers):
        if(question in submittedAnswers[group]):
            returnString = ",,,,,".join(submittedAnswers[group][question])
            print(returnString)
            return returnString

    print("did not find!")

    return found

if __name__ == '__main__':
    app.run(debug=True)