from _querier import querier


if __name__ == "__main__":
    print("Start processing metadata.")
    querier.process_metadata(
        save_path="./output/metadata-processed/all.json",
        use_img=False,
    )
