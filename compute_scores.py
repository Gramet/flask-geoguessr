import json
import os
from geopy.distance import distance


def compute_scores():
    answers_fp = os.listdir("answers")
    results = {}

    with open("ground_truth.json", "r") as f:
        ground_truth = json.load(f)

    for fp in answers_fp:
        with open(f"answers/{fp}", "r") as f:
            ans = json.load(f)

        team_name = ans["team_name"]
        results[team_name] = 0
        for i in range(10):
            pred = ans[f"pos{i}"]
            gt = ground_truth[f"pos{i}"]

            dist = compute_distance(pred, gt)

            points = get_points(dist)
            ans[f"pos{i}"]["score"] = points

            results[team_name] += points

        with open(f"answers/{fp}", "w") as f:
            json.dump(ans, f)

    print(json.dumps(results, indent=4, sort_keys=True))


def compute_distance(pred, gt):
    pred_t = (pred["lat"], pred["lng"])
    gt_t = (gt["lat"], gt["lng"])

    dist = distance(pred_t, gt_t).km
    return dist


def get_points(dist):
    if dist <= 1:
        return 2.0
    elif dist <= 10:
        return 1.5
    elif dist <= 100:
        return 1.0
    elif dist <= 1000:
        return 0.5
    else:
        return 0.0


if __name__ == "__main__":
    compute_scores()
