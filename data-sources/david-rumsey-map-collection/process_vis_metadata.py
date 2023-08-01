import json

from _querier import querier


if __name__ == "__main__":
    print("Start processing metadata of visualizations.")
    with open("./output/annotations/annotations.json", "r", encoding="utf-8") as f:
        annotations = json.load(f)
    querier.process_metadata(
        save_path="./output/metadata-processed/visualizations.json",
        use_img=True,
        uuids=[d["subject"] for d in annotations if d["value"] == "Vis"],
    )
