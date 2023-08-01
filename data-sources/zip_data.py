"""
Zip all the data files not gitignored.
"""

import os
from zipfile import ZipFile, ZIP_DEFLATED


def should_zip(root: str, filename: str) -> bool:
    # The directories in which the files are to be zipped.
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

    # The extensions of the data files to zip.
    return filename.endswith((".json", ".jsonl"))


if __name__ == "__main__":
    for root, dirs, filenames in os.walk("."):
        for filename in filenames:
            if not should_zip(root, filename):
                continue
            filename_without_ext, _ = os.path.splitext(filename)
            with ZipFile(
                f"{root}/{filename_without_ext}.zip", "w", ZIP_DEFLATED
            ) as zip_ref:
                zip_ref.write(f"{root}/{filename}", filename)
            os.remove(f"{root}/{filename}")
