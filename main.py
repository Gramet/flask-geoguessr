# coding: utf-8
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

app = Flask(__name__, template_folder="templates", static_folder="static")
app.config["TEMPLATES_AUTO_RELOAD"] = True

CORS(app)

load_dotenv()
# you can also pass key here
GoogleMaps(
    app,
    key=os.getenv("GOOGLE_MAPS_API_KEY"),
)

marker_dict = {
    0.0: "http://maps.google.com/mapfiles/ms/icons/purple-dot.png",
    0.5: "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
    1.0: "http://maps.google.com/mapfiles/ms/icons/yellow-dot.png",
    1.5: "http://maps.google.com/mapfiles/ms/icons/green-dot.png",
    2.0: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
}


def create_result_map(round, answers, ground_truth):
    markers = []
    paths = []

    for ans in answers:
        markers.append(
            {
                "lat": ans[f"pos{round}"]["lat"],
                "lng": ans[f"pos{round}"]["lng"],
                "label": f"{ans['team_name']}",
                "icon": marker_dict[ans[f"pos{round}"]["score"]],
            }
        )
        paths.append(
            [
                (
                    ground_truth[f"pos{round}"]["lat"],
                    ground_truth[f"pos{round}"]["lng"],
                ),
                (ans[f"pos{round}"]["lat"], ans[f"pos{round}"]["lng"]),
            ]
        )
    markers.append(
        {
            "icon": "static/waldo_face.png",
            "lat": ground_truth[f"pos{round}"]["lat"],
            "lng": ground_truth[f"pos{round}"]["lng"],
            # "label": "Charlie"
        }
    )

    map = Map(
        identifier=f"plinemap{round}",
        varname=f"plinemap{round}",
        lat=33.678,
        lng=-116.243,
        markers=markers,
        polylines=paths,
        style="width:700px; height:500px; margin-left:80px;",
        fit_markers_to_bounds=True,
    )

    return map


@app.route("/")
def mapview():

    answers_fp = sorted(os.listdir("answers"))
    answers = []
    for fp in answers_fp:
        with open(f"answers/{fp}", "r") as f:
            d = json.load(f)
        answers.append(d)

    with open("ground_truth.json", "r") as f:
        ground_truth = json.load(f)

    maps = []
    for i in range(0, 10):
        maps.append(
            create_result_map(round=i, answers=answers, ground_truth=ground_truth)
        )

    return render_template(
        "results.html",
        plinemap0=maps[0],
        plinemap1=maps[1],
        plinemap2=maps[2],
        plinemap3=maps[3],
        plinemap4=maps[4],
        plinemap5=maps[5],
        plinemap6=maps[6],
        plinemap7=maps[7],
        plinemap8=maps[8],
        plinemap9=maps[9],
        GOOGLEMAPS_KEY=request.args.get("apikey"),
    )


@app.route("/submit", methods=["POST"])
def submit_answers():
    d = request.json
    timestamp = datetime.now().strftime("%H_%M_%S_%f")
    with open(f"answers/{timestamp}.json", "w") as f:
        json.dump(d, f)
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")
