"""
Utility functions to load metadata.
"""

import json
from typing import List
from zipfile import ZipFile


def get_processed_metadata_path(dataset_path: str) -> str:
    """
    Get the path to the processed metadata of the given dataset name.
    """

    return f"{dataset_path}/output/metadata-processed/visualizations.json"


def get_zipped_processed_metadata_path(dataset_path: str) -> str:
    """
    Get the path to the zipped processed metadata of the given dataset name.
    """

    return f"{dataset_path}/output/metadata-processed/visualizations.zip"


def load_processed_metadata(dataset_paths: List[str]) -> List:
    """
    Load and concat all the processed metadata.
    """

    metadata = []
    for d in dataset_paths:
        with open(get_processed_metadata_path(d), "r", encoding="utf-8") as f:
            metadata += json.load(f)
    return metadata


def load_zipped_json(path: str):
    with ZipFile(path) as zip_ref:
        for filename in zip_ref.namelist():
            with zip_ref.open(filename) as f:
                return json.load(f)


def load_zipped_processed_metadata(dataset_paths: List[str]) -> List:
    """
    Load and concat all the processed metadata.
    """

    metadata = []
    for d in dataset_paths:
        path = get_zipped_processed_metadata_path(d)
        metadata += load_zipped_json(path)
    return metadata
