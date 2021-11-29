# Where is Waldo

This repo implements a small Typescript webapp based on GoogleMaps Javascript API as well as a Flask backend with Flask_googlemaps for displaying results, for a "where is Waldo" game.

During the game, we showed pictures of Waldo in Google Streetview to the audience. They had to pinpoint on the map (hosted in the webapp) where the picture was taken. Answers are gathered in the `answers` folder and scores are computed with the `compute_scores.py` script.

Results can then be visualized on `localhost:5000`.

## Installation

1. Create and activate a virtual environment: `python -m venv env` and `source /env/bin/activate`
2. Install the python requirements in a virtualenv with pip: `pip install -r requirements.txt`
2. Install the javascript webapp with npm: `cd js-samples & npm i`
3. Add your Google maps Javascript api key to the `.env` as well as your IP on the network.
4. Copy the `.env` file inside js-samples: `cp .env js.samples`
5. All set!

## Running the game

1. Run `npm start` in the `js-samples` folder
2. Run `python main.py` at the root
3. Wait for the teams to enter their answers on `{HOST_IP}:8080`
4. Once they are done, you can run `python compute_scores.py`
5. And visualize the results on `localhost:5000`

## Known issues

* If you encounter this kind of error
```
[webpack-cli] Error: error:0308010C:digital envelope routines::unsupported
    at new Hash (node:internal/crypto/hash:67:19)
    at Object.createHash (node:crypto:130:10)
    at BulkUpdateDecorator.hashFactory (/opt/src/node_modules/webpack/lib/util/createHash.js:155:18)
    at BulkUpdateDecorator.digest (/opt/src/node_modules/webpack/lib/util/createHash.js:80:21)
    at /opt/src/node_modules/webpack/lib/DefinePlugin.js:595:38
    at Hook.eval [as call] (eval at create (/opt/src/node_modules/tapable/lib/HookCodeFactory.js:19:10), <anonymous>:100:1)
    at Hook.CALL_DELEGATE [as _call] (/opt/src/node_modules/tapable/lib/Hook.js:14:14)
    at Compiler.newCompilation (/opt/src/node_modules/webpack/lib/Compiler.js:1053:26)
    at /opt/src/node_modules/webpack/lib/Compiler.js:1097:29
    at Hook.eval [as callAsync] (eval at create (/opt/src/node_modules/tapable/lib/HookCodeFactory.js:33:10), <anonymous>:6:1) {
  opensslErrorStack: [ 'error:03000086:digital envelope routines::initialization error' ],
  library: 'digital envelope routines',
  reason: 'unsupported',
  code: 'ERR_OSSL_EVP_UNSUPPORTED'
}
```

you can go around it with: `export NODE_OPTIONS=--openssl-legacy-provider`