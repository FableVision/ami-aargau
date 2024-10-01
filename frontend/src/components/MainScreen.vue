<template>
    <div id="top-buttons-container">
        <button class="nav-button" id="back-button" @click="back()">
            <img id="back-image" src="@/assets/png/back.png">
            Back
        </button>
        <button class="nav-button" id="home-button" @click="home()">
            <img id="home-image" src="@/assets/png/home.png">
        </button>
    </div>
    <div id="group-banner">
        <div class="banner-img-container">
            <img id="my-team-img" class="banner-img" :src="teamImageUrl">
        </div>
        <div class="banner-text-container">
            <div class="banner-team-text">Team Name</div>
            <div class="banner-round-text">Question 2</div>
        </div>
    </div>
    <div id="choose-a-team" class="centered-div">
        <div class="game-main-text">Join a team</div>
        <div class="team-selection">
            <div class="team-container">
                <button class="team-img-container" @click="chooseTeam('ant')">
                    <img class="team-img" src="@/assets/png/ant.png">
                </button>
                Ant
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="chooseTeam('butterfly')">
                    <img class="team-img" src="@/assets/png/butterfly.png">
                </button>
                Butterfly
                
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="chooseTeam('cat')">
                    <img class="team-img" src="@/assets/png/cat.png">
                </button>
                Cat
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="chooseTeam('octopus')">
                    <img class="team-img" src="@/assets/png/octopus.png">
                </button>
                Octopus
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="chooseTeam('whale')">
                    <img class="team-img" src="@/assets/png/whale.png">
                </button>
                Whale
            </div>
            <div class="team-container">
                <button class="team-img-container" @click="chooseTeam('owl')">
                    <img class="team-img" src="@/assets/png/owl.png">
                </button>
                Owl
            </div>
        </div>
    </div>
    <div id="find-artwork" class="centered-div">
        <div class="artwork-container">
            <img id="artwork" :src="artworkImageUrl">
        </div>
        <div>Find this painting</div>
        <span id="artwork-title">{{ artworkTitle }}</span>
        <div style="height: 50px"></div>
        <button class="confirm-button" @click="nextPage">I found it!</button>
    </div>
    <div id="select-judge" class="centered-div center-vertically">
        <span style="font-weight: bold;">Are you the judge?</span>
        <span>The judge for this round is:</span>
        <span style="font-weight: 600;" id="judge-question">{{judgeQuestion}}</span>
        <div style="height: 75px"></div>
        <button class="option-button" @click="selectJudge(false)">No, I am not!</button>
        <button class="option-button" @click="selectJudge(true)">Yes, I am!</button>
    </div>
    <div id="pick-an-answer" class="centered-div">
        <span class="game-main-text">{{ questionText }}</span>
        <div style="height: 25px"></div>
        <div id='answer-selection-container' class="answer-selection">
            <div class="answer-container" @click="selectAnswerOption(0)">The option they are picking goes here</div>
            <div class="answer-container" @click="selectAnswerOption(1)">The option they are picking goes here</div>
            <div class="answer-container" @click="selectAnswerOption(2)">The option they are picking goes here</div>
            <div class="answer-container" @click="selectAnswerOption(3)">The option they are picking goes here</div>
        </div>
        <div style="height: 0px"></div>
        <div class="answer-redraw-container">
            <button class="redraw-icon-container" @click="refreshPossibleAnswers()">
                <img class="redraw-icon" src="@/assets/png/delete.png">
            </button>
            <span style="font-weight: 300; font-size: 14pt;">Discard and draw new options</span>
        </div>
        <div style="height: 25px"></div>
        <button id='answer-confirm' class="confirm-button" @click="submitAnswer">Submit</button>
    </div>
    <div id="submitted-answer" class="centered-div center-vertically">
        <span style="font-size: 24pt; font-weight: bold;">You've submitted!</span>
        <span style="text-align: center;">Let's wait until everyone has submitted their answers</span>
        <div style="height: 25px"></div>
        <span style="text-align: center;">Are they done yet?</span>
        <button class="confirm-button" @click="nextPage">Let's go!</button>
    </div>
    <div id="judge-pick" class="centered-div">
        <span id="judge-screen-text" class="game-main-text">You are the judge!</span>
        <div id="answer-selection-instructions">
            <span>1. Wait for all players to submit.</span>
            <span>2. Ask each player to defend their responses.</span>
            <span>3. Decide on the best response and reward that player with a point card!</span>
            <div style="height: 25px"></div>
        </div>
        <span class="game-main-text">{{ questionText }}</span>
        <div class="answer-redraw-container">
            <button class="redraw-icon-container" @click="refreshJudgeOptions()">
                <img class="redraw-icon" src="@/assets/png/refresh.png">
            </button>
            <span style="font-weight: 300; font-size: 14pt;">Refresh for new submissions</span>
        </div>
        <div id='judge-answer-selection' class="answer-selection">
            <div class="answer-container" @click="selectJudgeOption(0)">The option they are picking goes here</div>
        </div>
        <div style="height: 25px"></div>
        <button id='judge-confirm' class="confirm-button" @click="nextPage">Next Round</button>
    </div>
    <RouterView />
  </template>

<script>
    import { onMounted } from 'vue'
    import { RouterLink, RouterView } from 'vue-router'
    import { useRouter } from 'vue-router';
    import { ref } from 'vue'
    import { useStore } from 'vuex';
    import allText from '../text/text.json'

    export default {
        setup() {
            const router = useRouter();

            // These keep track of which question and page we are on
            let questionIndex = 0;
            let screenIndex = 0;
            let isJudge = false;
            let teamname = "";
            let answerSelected = -1;

            let questionOrder = [1,2,3,4,5];

            let pages = [];

            onMounted(() => {
                console.log("on mounted");
                setup();
            });

            function setup(){
                questionIndex = 0;
                screenIndex = 0;
                isJudge = false;

                pages.push(document.getElementById('choose-a-team'));
                pages.push(document.getElementById('find-artwork'));
                pages.push(document.getElementById('select-judge'));
                pages.push(document.getElementById('pick-an-answer'));
                pages.push(document.getElementById('submitted-answer'));
                pages.push(document.getElementById('judge-pick'));

                redraw();
            }

            const getTeamImageUrl = (name) => {
                return new URL(`../assets/png/${name}.png`, import.meta.url).href
            }

            const getArtworkImageUrl = (name) => {
                return new URL(`../assets/jpg/${name}.jpg`, import.meta.url).href
            }

            const teamImageUrl = ref(getTeamImageUrl('ant'));
            const artworkImageUrl = ref(getArtworkImageUrl('6246'));
            const questionText = ref("question text here");
            const artworkTitle = ref("Artwork Title");
            const judgeQuestion = ref("Judge question");

            function send(submittedAnswer) {
                console.log("sending");

                const group = teamname;
                const question = questionIndex;
                const answer = submittedAnswer;
                
                const params = new URLSearchParams({
                    group: group,
                    question: question,
                    answer: answer
                });

                const baseUrl = import.meta.env.VITE_API_URL;
                fetch(baseUrl + '/receive?' + params.toString(), {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({message: ""}),
                })
                .then(response => response.json())
                .then(data => console.log(data));
            }

            function nextPage(){
                if(isJudge){
                    const shouldSkipAnswerInput = screenIndex === 2; // the answer input is screen index 3
                    if(shouldSkipAnswerInput){
                        screenIndex += 3;
                    }
                    else{
                        screenIndex++;
                    }
                }
                else{
                    screenIndex++;
                }
                if(screenIndex == 6){
                    // Go back to the next question
                    questionIndex++;
                    if(questionIndex >= questionOrder.length){
                        router.push('/end');
                        return;
                    }
                    screenIndex = 1;
                    isJudge = false;
                }
                redraw();
            }

            function chooseTeam(teamName){
                teamname = teamName;

                const groupBanner = document.getElementById('group-banner');
                const teamNameField = groupBanner.getElementsByClassName('banner-team-text')[0];
                teamNameField.innerText = teamname.toUpperCase();

                teamImageUrl.value = getTeamImageUrl(teamName);

                // Set the correct order of artworks to show
                for(let i = 0; i < allText.question_order.length; i++){
                    if(allText.question_order[i].teamName.toLowerCase() == teamName.toLowerCase()){
                        const questionOrderString = allText.question_order[i].artworkIdOrder;
                        // Turn the order string into ints
                        questionOrder = questionOrderString.split(',').map(num => parseInt(num.trim()));
                        console.log("questino order:" + questionOrder);
                    }
                }
                
                screenIndex = 1;
                redraw();
            }

            function selectJudge(isjudge){
                isJudge = isjudge;
                nextPage();
            }

            function updateJudgeOptions(answerOptions) {
                const answerSelection = document.getElementById('judge-answer-selection');
                const existingOptions = answerSelection.children;
                
                answerOptions.forEach((option, index) => {
                    let optionElement;
                    if (index < existingOptions.length) {
                        // Update existing option
                        optionElement = existingOptions[index];
                        optionElement.textContent = option;
                    } else {
                        // Create new option
                        optionElement = document.createElement('div');
                        optionElement.className = 'answer-container';
                        optionElement.textContent = option;
                        answerSelection.appendChild(optionElement);
                    }
                    
                    optionElement.onclick = () => selectJudgeOption(index);
                    optionElement.style.display = 'block'; 
                });
                
                // Hide or remove extra options
                for (let i = answerOptions.length; i < existingOptions.length; i++) {
                    existingOptions[i].style.display = 'none';
                    existingOptions[i].remove();
                }
            }

            function selectAnswerOption(index) {
                const answerSelectionContainer = document.getElementById('answer-selection-container');
                const options = answerSelectionContainer.getElementsByClassName('answer-container');

                for (let i = 0; i < options.length; i++) {
                    if (i === index) {
                        options[i].classList.add('selected');
                    } 
                    else {
                        options[i].classList.remove('selected');
                    }
                }
                
                const answerConfirmButton = document.getElementById('answer-confirm');
                if(index != -1){
                    answerConfirmButton.classList.remove('uninteractable');
                }
                else{
                    answerConfirmButton.classList.add('uninteractable');
                }
            }

            function submitAnswer(){
                // Figure out what has been selected
                let answer = "";
                const answerSelectionContainer = document.getElementById('answer-selection-container');
                const options = answerSelectionContainer.getElementsByClassName('answer-container');

                for (let i = 0; i < options.length; i++) {
                    if(options[i].classList.contains('selected')){
                        answer = options[i].innerText;
                    }
                }

                if(answer != ""){
                    send(answer);
                }

                nextPage();
            }

            function refreshPossibleAnswers(){
                handleChooseAnswersScreen();
            }

            function selectJudgeOption(index) {
                const judgeOptionsContainer = document.getElementById('judge-answer-selection');
                const options = judgeOptionsContainer.getElementsByClassName('answer-container');

                if(!isJudge) return;

                for (let i = 0; i < options.length; i++) {
                    if (i === index) {
                        options[i].classList.add('selected');
                    } 
                    else {
                        options[i].classList.remove('selected');
                    }
                }
                
                const judgeConfirmButton = document.getElementById('judge-confirm');
                if(index == -1 && isJudge){
                    judgeConfirmButton.classList.add('uninteractable');
                }
                else{
                    judgeConfirmButton.classList.remove('uninteractable');
                }
            }

            function redraw(){
                for(let i = 0; i < pages.length; i++){
                    const shouldShow = i == screenIndex;
                    pages[i].style.display = shouldShow ? 'flex' : 'none';
                }

                globalThis.scrollTo({ top: 0, left: 0, behavior: "smooth" });

                if(screenIndex > 0){
                    console.log("here");
                    let questionData = getQuestionData(questionOrder[questionIndex]);
                    console.log(questionData.question);
                    questionText.value = questionData.question;
                    artworkTitle.value = questionData.artworkName;
                    judgeQuestion.value = questionData.judgeStatement;
                }

                const groupBanner = document.getElementById('group-banner');
                const questionField = groupBanner.getElementsByClassName('banner-round-text')[0];
                questionField.innerText = "ROUND " + (questionIndex + 1);

                const isChooseTeamScreen = screenIndex == 0;
                groupBanner.style.display = isChooseTeamScreen ? 'none' : 'flex';

                const isArtworkScreen = screenIndex == 1;
                if(isArtworkScreen){
                    let questionData = getQuestionData(questionOrder[questionIndex]);
                    artworkImageUrl.value = getArtworkImageUrl(questionData.imageFileName);
                }

                const isChooseAnswersScreen = screenIndex == 3;
                if(isChooseAnswersScreen){
                    handleChooseAnswersScreen()
                }

                const isShowAnswersScreen = screenIndex == 5;
                if(isShowAnswersScreen){
                    handleShowAnswersScreen();
                }
            }

            function handleChooseAnswersScreen(){
                selectAnswerOption(-1);
                const answerCategory = getQuestionData(questionOrder[questionIndex]).answerType;
                const allPossibleAnswers = allText.answers;
                const answerOptions = [];
                for(let i = 0; i < allPossibleAnswers.length; i++){
                    if(answerCategory == allPossibleAnswers[i].wordCategory){
                        answerOptions.push(allPossibleAnswers[i].word);
                    }
                }

                const fourRandomOptions = selectRandomElements(answerOptions, 4);

                const answerSelection = document.getElementById('answer-selection-container');
                const existingOptions = answerSelection.children;
                
                fourRandomOptions.forEach((option, index) => {
                    let optionElement;
                    if (index < existingOptions.length) {
                        // Update existing option
                        optionElement = existingOptions[index];
                        optionElement.textContent = option;
                    }
                    
                    optionElement.style.display = 'block'; 
                });
            }

            function selectRandomElements(array, count) {
                const copyArray = [...array];
                const result = [];

                for (let i = 0; i < count; i++) {
                    const randomIndex = Math.floor(Math.random() * copyArray.length);
                    const [selectedElement] = copyArray.splice(randomIndex, 1);
                    result.push(selectedElement);
                }

                return result;
            }

            function handleShowAnswersScreen(){
                const judgeInstructions = document.getElementById('answer-selection-instructions');
                judgeInstructions.style.display = isJudge ? 'flex' : 'none';

                const judgeTitle = document.getElementById('judge-screen-text')
                judgeTitle.innerText = isJudge ? "You are the judge!" : "All Responses";

                // Grab the current options
                selectJudgeOption(-1);
                updateJudgeOptions([]);
                refreshJudgeOptions();
            }

            function refreshJudgeOptions(){
                if(screenIndex != 5){
                    return;
                }
                
                console.log("refreshing!!");
                
                const group = teamname;
                const question = questionIndex;
                
                const params = new URLSearchParams({
                    group: group,
                    question: question,
                });

                const baseUrl = import.meta.env.VITE_API_URL;
                fetch(baseUrl + '/send?' + params.toString())
                .then(response => response.json())
                .then(data => {
                    console.log(data.message);
                    if(data.message != ""){
                        let strMessage = data.message.toString();
                        let listofanswers = strMessage.split(",,,,,");
                        console.log(listofanswers);
                        updateJudgeOptions(listofanswers);

                        setTimeout(()=>{
                            refreshJudgeOptions();
                        }, 3000);
                    }
                });
            }

            function getQuestionData(id){
                console.log(allText.artwork_list);
                for(let i = 0; i < allText.artwork_list.length; i++){
                    if(allText.artwork_list[i].artworkId == id){
                        return allText.artwork_list[i];
                    }
                }
            }

            function back(){
                if(screenIndex == 0){
                    router.push("/title");
                    return;
                }
                if(isJudge){
                    const shouldSkipAnswerInput = screenIndex === 5; // the answer input is screen index 3
                    if(shouldSkipAnswerInput){
                        screenIndex -= 3;
                    }
                    else{
                        screenIndex--;
                    }
                }
                else{
                    screenIndex--;
                }
                if(screenIndex == 0 && questionIndex > 0){
                    // Go back to the previous question
                    questionIndex = Math.max(0, questionIndex - 1)
                    screenIndex = 5;
                    isJudge = false;
                }
                if(screenIndex == 0 && questionIndex == 0){
                    questionIndex = 0;
                    screenIndex = 0;
                    isJudge = false;
                }
                screenIndex = Math.max(0, screenIndex);
                questionIndex = Math.max(0, questionIndex)
                redraw();
            }

            function home(){
                router.push('/title');
            }

            return {
                back, home, send, nextPage, chooseTeam, selectJudge, 
                selectJudgeOption, selectAnswerOption, submitAnswer, refreshPossibleAnswers,
                refreshJudgeOptions, teamImageUrl, artworkImageUrl, questionText, artworkTitle,
                judgeQuestion
            }
        }
    }

</script>