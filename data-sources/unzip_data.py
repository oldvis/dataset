"""
Unzip all the data files not gitignored.
"""

import os
from zipfile import ZipFile, ZIP_DEFLATED


def should_unzip(root: str, filename: str) -> bool:
    # The directories in which the files are to be unzipped.
    if not root.endswith(
        (
            "annotations",
            "metadata",
            "query-return",
            "metadata-processed",
            "queries",
        )
    ):
        return False

    return filename.endswith(".zip")


if __name__ == "__main__":
    for root, dirs, filenames in os.walk("."):
        for filename in filenames:
            if not should_unzip(root, filename):
                continue
            with ZipFile(f"{root}/{filename}", "r", ZIP_DEFLATED) as zip_ref:
                zip_ref.extractall(root)
            os.remove(f"{root}/{filename}")
