"""
Utility functions to load metadata.
"""

import json
from typing import List


def get_processed_metadata_path(dataset_name: str) -> str:
    """
    Get the path to the processed metadata of the given dataset name.
    """

    return (
        f"../data-sources/{dataset_name}/output/metadata-processed/visualizations.json"
    )


def load_processed_metadata(dataset_names: List[str]) -> List:
    """
    Load and concat all the processed metadata.
    """

    metadata = []
    for d in dataset_names:
        with open(get_processed_metadata_path(d), "r", encoding="utf-8") as f:
            metadata += json.load(f)
    return metadata
