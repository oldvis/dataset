# Telefact

This directory stores data obtained from [Telefact: 1938-1945 by Pictograph Corporation](https://modley-telefact-1939-1945.tumblr.com/archive).

For more information about this data source, see the [data source documentation](https://oldvis.github.io/libquery_extensions/api/telefact.html).

## Data Fetching Approach

The queried URLs in `queries` of `_queries.py` are obtained with the following steps:

1. Open <https://modley-telefact-1939-1945.tumblr.com/archive> in a browser.
2. Scroll to the bottom of the webpage until no new images are loaded.
3. Launch DevTools of the browser and execute in the console `const urls = [...document.querySelectorAll('.NGc5k a')].map((d) => d.href)` to get the URLs of all the image pages.
4. Copy the value of `urls` and store it into `queries` of `_queries.py`.

## Image Types

The visualizations in this data source are mainly [Isotypes](https://wikipedia.org/wiki/Isotype_(picture_language)).
