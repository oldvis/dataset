import json
import os
from typing import List

from _querier import querier


def try_load(path: str) -> List:
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    path_metadata_all = "./output/metadata-processed/all.json"
    path_metadata_unlabeled = "./output/metadata-processed/unlabeled.json"
    path_annotations = "./output/annotations/annotations.json"

    print("Start processing metadata of unlabeled entries.")
    querier.process_metadata(save_path=path_metadata_all, use_img=False)
    uuids_all = {d["uuid"] for d in try_load(path_metadata_all)}
    uuids_labeled = {d["subject"] for d in try_load(path_annotations)}
    querier.process_metadata(
        save_path=path_metadata_unlabeled,
        use_img=False,
        uuids=uuids_all - uuids_labeled,
    )
