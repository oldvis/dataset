from _querier import querier
from _queries import queries


if __name__ == "__main__":
    print("Start fetching metadata.")
    querier.fetch_metadata(queries=queries)
    querier.validate_metadata()
