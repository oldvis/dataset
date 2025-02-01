# Gallica

This directory stores data obtained from [Gallica](https://gallica.bnf.fr).

For more information about this data source, see the [data source documentation](https://oldvis.github.io/libquery/api/gallica.html).

## Search Result

| Query                                                                                                                                                                   | #Matches | Last Accessed |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| [carte figurative](https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords=10&startRecord=1&query=dc.title+all+%22cartes+figurative%22)          | 63       | 2023/03/11    |
| [tableau graphique](https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords=10&startRecord=1&query=dc.title+all+%22tableau+graphique%22)         | 35       | 2023/03/11    |
| [statistique graphique](https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords=10&startRecord=1&query=dc.title+all+%22statistique+graphique%22) | 26       | 2023/03/11    |
| [atlas de](https://gallica.bnf.fr/SRU?operation=searchRetrieve&version=1.2&maximumRecords=10&startRecord=1&query=dc.title+all+%22atlas+de%22)                           | 3794     | 2023/03/11    |


**Notes on the search result:**
- We tried the search queries in French as most of the indexed documents in Gallica are in French.
- Each match corresponds to an image collection. An image collection may contain multiple images.
- In the implementation, each keyword corresponds to multiple queries with different `startRecord`. The URL above for each query is the URL of the first query with `startRecord=1` among the multiple queries.
