# David Rumsey Map Collection

This directory stores data obtained from [David Rumsey Map Collection](https://www.davidrumsey.com).

For more information about this data source, see the [data source documentation](https://oldvis.github.io/libquery/api/david-rumsey-map-collection.html).

## Search Result

| Query                                                                                                           | #Matches | Last Accessed |
| --------------------------------------------------------------------------------------------------------------- | -------- | ------------- |
| [q=subject=data+visualization](https://www.davidrumsey.com/luna/servlet/as/search?q=subject=data+visualization) | 4906     | 2022/06/27    |
| [q=subject=statistical](https://www.davidrumsey.com/luna/servlet/as/search?q=subject=statistical)               | 1977     | 2022/06/27    |
| [q=type=chart](https://www.davidrumsey.com/luna/servlet/as/search?q=type=chart)                                 | 2473     | 2022/06/27    |
| [q=type=diagram](https://www.davidrumsey.com/luna/servlet/as/search?q=type=diagram)                             | 1820     | 2022/06/27    |
| [q=data+visualization](https://www.davidrumsey.com/luna/servlet/as/search?q=data+visualization)                 | 5938     | 2022/06/27    |
| [q=statistical](https://www.davidrumsey.com/luna/servlet/as/search?q=statistical)                               | 11890    | 2022/06/27    |
| [q=chart](https://www.davidrumsey.com/luna/servlet/as/search?q=chart)                                           | 7239     | 2022/06/27    |
| [q=diagram](https://www.davidrumsey.com/luna/servlet/as/search?q=diagram)                                       | 3190     | 2022/06/27    |
| [q=data](https://www.davidrumsey.com/luna/servlet/as/search?q=data)                                             | 9543     | 2022/06/27    |

### Notes

- The data source is actively maintained and its collection is growing over time.
- Not all the returned entries are images.
    - Some entries are websites.
    - The data type of an entry can be checked with `mediaType == "Image"`.
- The following queries return the same entries.
    - "q=subject=data+visualization"
    - "q=subject=visualization"
    - "q=subject=data"
