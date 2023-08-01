# Library of Congress

This directory stores data obtained from [Library of Congress](https://www.loc.gov/).

For more information about this data source, see the [data source documentation](https://oldvis.github.io/libquery/api/library-of-congress.html).

## Search Result

| Query                                                                                                                             | #Matches | Query Type      | Last Accessed | Notes                |
| --------------------------------------------------------------------------------------------------------------------------------- | -------: | --------------- | ------------- | -------------------- |
| [photos](https://www.loc.gov/photos/?fa=online-format:image)                                                                      |  1092070 | entire dataset  | 2023/07/31    | /                    |
| [maps](https://www.loc.gov/maps/?fa=online-format:image)                                                                          |    56464 | entire dataset  | 2023/07/31    | [^1]                 |
| [q=historical+map](https://www.loc.gov/search/?fa=online-format:image&q=historical+map)                                           |   438101 | chart type name | 2023/07/31    | /                    |
| [photos/?q=line+chart](https://www.loc.gov/photos/?fa=online-format:image&q=line+chart)                                           |      109 | chart type name | 2023/07/31    | contains Vis         |
| [photos/?q=bar+chart](https://www.loc.gov/photos/?fa=online-format:image&q=bar+chart)                                             |       59 | chart type name | 2023/07/31    | contains Vis         |
| [photos/?q=chart](https://www.loc.gov/photos/?fa=online-format:image&q=chart)                                                     |     1048 | synonym of Vis  | 2023/07/31    | ~30% are Vis         |
| [photos/?q=visualization](https://www.loc.gov/photos/?fa=online-format:image&q=visualization)                                     |       82 | synonym of Vis  | 2023/07/31    | /                    |
| [photos/?q=graph](https://www.loc.gov/photos/?fa=online-format:image&q=graph)                                                     |      180 | synonym of Vis  | 2023/07/31    | ~40% are Vis         |
| [photos/?q=diagram](https://www.loc.gov/photos/?fa=online-format:image&q=diagram)                                                 |      613 | synonym of Vis  | 2023/07/31    | mostly illustrations |
| [photos/?q=statistic](https://www.loc.gov/photos/?fa=online-format:image&q=statistic)                                             |      429 | related subject | 2023/07/31    | /                    |
| [photos/?q=popular+and+applied+graphic+art](https://www.loc.gov/photos/?fa=online-format:image&q=popular+and+applied+graphic+art) |     4574 | related subject | 2023/07/31    | /                    |
| [q=charles+joseph+minard](https://www.loc.gov/search/?fa=online-format:image&q=charles+joseph+minard)                             |    10898 | old Vis author  | 2023/07/31    | /                    |
| [q=william+playfair](https://www.loc.gov/search/?fa=online-format:image&q=william+playfair)                                       |     5289 | old Vis author  | 2023/07/31    | /                    |

[^1]: Around half of the returned images are [Sanborn maps](https://wikipedia.org/wiki/Sanborn_maps).
    They are maps of building plans.
    We do not count them as typical visualizations.
