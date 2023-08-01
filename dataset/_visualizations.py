"""
Utility functions to build "visualization" entities.
"""

from typing import List

from libprocess.typing import ProcessedMetadataEntry


def is_old(d: ProcessedMetadataEntry) -> bool:
    if d["publishDate"] is None:
        return True
    if isinstance(d["publishDate"], list):
        return d["publishDate"][0]["year"] <= 1950
    return d["publishDate"]["year"] <= 1950


def build_visualizations(
    processed_metadata: List[ProcessedMetadataEntry],
) -> List[ProcessedMetadataEntry]:
    return [d for d in processed_metadata if is_old(d)]
