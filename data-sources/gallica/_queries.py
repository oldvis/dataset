"""
Reference
---------
The search query grammar can be found at <https://api.bnf.fr/api-gallica-de-recherche>.
"""

# The base urls for search the items.
# maximumRecords: the number of returned entries in range [1, 50]
# (if not given, the default value is 15).
_base_url = "https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords={maximumRecords}&startRecord={startRecord}"

# Note: Use %22 to represent double quote (").
# When storing the query result, double quote cannot be used in filename.
queries = [
    f"{_base_url}&query=dc.title+all+%22cartes+figurative%22",
    f"{_base_url}&query=dc.title+all+%22tableau+graphique%22",
    f"{_base_url}&query=dc.title+all+%22statistique+graphique%22",
    f"{_base_url}&query=dc.title+all+%22atlas+de%22",
]
