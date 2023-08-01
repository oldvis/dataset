from libprocess_extensions import BritishLibraryCollectionItems

querier = BritishLibraryCollectionItems(
    query_path="./output/queries/queries.jsonl",
    metadata_path="./output/metadata/metadata.jsonl",
    img_dir="./output/imgs",
)
