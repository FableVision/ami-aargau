# Summary
Main Dev: Owen Hey (owen@fablevision.com)

Producers: Kellian / Snow

This is one of the AMI projects, for the Aargau MOMA museum.

There is a content sheet [here](https://docs.google.com/spreadsheets/d/1ZoJpM_bfQw78Rzfk8jzCsRyD0K8B6bSZuDxG-cqcw0A/edit?gid=0#gid=0):
- You can export the json and put it into the text.json, and then upload to fvdev3

GDD: [LINK HERE](https://docs.google.com/document/d/1VYomxuFA_c6z58PgrfWNEcfWgGIkAOsSQq1h881cuGM/edit)

# Dev stuff
There are two codebases here, the python server and the frontend (Vue)

For the frontend:
- cd into the `frontend` directory
- Maybe run npm install to get packages
- `npm run dev` to run locally
- `npm run build` to run build

The build goes up on fvdev3 under ami.fablevision-dev/aargau

For the backend (python server):
- cd into `python-server`
- you need python3 for this, install that, and then install Flask and flaskcors
- To get flask / flaskcors: either `pip install Flask` and `pip install flaskcors` OR `python3 -m pip install Flask` and `python3 -m pip install flaskcors`
- This runs as a service up on fvdev3. The service can be found in `etc/systemd/system/`. This just runs the python server when fvdev3 restarts.
- The app.py can be found in vhosts under ami-aargau-server.fablevision-dev
