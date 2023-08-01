from libprocess import InternetArchive

querier = InternetArchive(
    metadata_dir="./output/metadata",
    download_dir="./output/downloads",
    img_dir="./output/imgs",
)
