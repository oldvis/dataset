"""
Zip all the data files not gitignored.
"""

import os
import stat
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED


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


def deterministic_zip(root: str, filename: str) -> None:
    """
    Create a zip file deterministically.
    For the same input file, the created zip will be the same.
    """

    filename_without_ext, _ = os.path.splitext(filename)
    path_zip = f"{root}/{filename_without_ext}.zip"
    path_file = f"{root}/{filename}"

    zip_info = ZipInfo.from_file(path_file, filename)
    # Set the file datetime as a fixed value.
    zip_info.date_time = (1980, 0, 0, 0, 0, 0)
    # Set the create platform as a fixed value.
    zip_info.create_system = 0
    permission = 0o555 if os.access(path_file, os.X_OK) else 0o444
    zip_info.external_attr = (stat.S_IFREG | permission) << 16

    with (
        ZipFile(path_zip, "w", ZIP_DEFLATED) as zip_ref,
        open(path_file, "r", encoding="utf-8", newline="") as f,
    ):
        zip_ref.writestr(
            zip_info,
            f.read(),
            compress_type=ZIP_DEFLATED,
            compresslevel=9,
        )


if __name__ == "__main__":
    for root, dirs, filenames in os.walk("."):
        for filename in filenames:
            if not should_zip(root, filename):
                continue
            deterministic_zip(root, filename)
            os.remove(f"{root}/{filename}")
