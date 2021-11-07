# Where is Waldo

This repo implements a small Typescript webapp based on GoogleMaps Javascript API as well as a Flask backend with Flask_googlemaps for displaying results, for a "where is Waldo" game

During the game, we showed pictures of Waldo in Google Streetview in to the audience. They had to pinpoint on the map (hosted in the webapp) where the picture was taken. Answers are gathered in the `answers` folder and scores are computed with the `compute_scores.py` script.

Results can then be visualized on `localhost:5000`.

## Installation

1. Install the python requirements in a virtualenv with pip
2. Install the javascript webapp with np `npm i` inside the `js-samples` folder
3. Add your Google maps Javascript api key to the `.env` both at the root and inside `js-samples`

## Running the game

1. Run `npm start` in the `js-samples` folder
2. Run `python main.py` at the root
3. Wait for the teams to enter their answers on `HOST_IP:8080`
4. Once they are done, you can run `python compute_scores.py`
5. And visualize the results on `localhost:5000`