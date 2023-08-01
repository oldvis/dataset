from _querier import querier
from _queries import queries


if __name__ == "__main__":
    print("Start fetching metadata.")
    # Note: querying 1 image's metadata takes ~1s (last accessed: 2023/07/19)
    querier.fetch_metadata(queries=queries)
    querier.validate_metadata()
