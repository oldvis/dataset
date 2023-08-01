"""
Reference
---------
The search query grammar can be found at <https://archive.org/advancedsearch.php>.

Notes
-----
For each query, we include the condition "-collection:(david-rumsey-map-collection)"
to exclude entries that belong to David Rumsey Map Collection.
The consideration is that we already have dedicated implementation for
querying the official API of David Rumsey Map Collection.
"""

queries = [
    "(statistical atlas) AND -collection:(david-rumsey-map-collection) AND date:[0001-01-01 TO 1990-12-31]",
    "creator:(Snow, John) AND -collection:(david-rumsey-map-collection) AND date:[1800-01-01 TO 1950-12-31]",
    "creator:(Cheysson, Émile) AND -collection:(david-rumsey-map-collection) AND date:[0001-01-01 TO 1990-12-31]",
]
