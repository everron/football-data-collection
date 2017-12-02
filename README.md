**knbknb 20171202:**

* original repo: https://github.com/hugomathien/football-data-collection
* modified in 2017 by github user sovello,
  https://github.com/sovello/football-data-collection , forked from there

### How to use (notes to myself):

This repository does _not_ contain any data, just the python scripts that scrape
the data from public websites.

The software used to download from the internet, _scrapy_, is free software.
However, the version used to compile this dataset in 2016 has been rewritten by
the community. Now the minimal documentation given here is not sufficient, and
the source code comments are misleading (because they point to old
documentation)

To run these script, you must:

* install scrapy and its dependencies: `pip install scrapy`
* install the google-web-api-client: `pip install --upgrade
  google-api-python-client`
* install the json-rpc extension for scrapy: `pip install scrapy-jsonrpc`

* edit `matchcrawler.py` and change these lines of code: <code> countries =
  ['England']

  seasons = ['2009/2010', '2010/2011', '2011/2012', '2012/2013',
  '2013/2014','2014/2015', '2015/2016', '2016/2017', '2017/2018'] </code>

Then run `scrapy crawl match` from the command line

---

# Collecting football data

## Welcome !

This is an open source project aiming to provide tools for people to collect and
format large set of data about football matches and players. The project is
essentially a crawler written in Python and relies on two sources:

* Football matches, end of game statistics and in-game events. You can crawl
  these with the **MatchSpider**
  [http://football-data.mx-api.enetscores.com/](http://football-data.mx-api.enetscores.com/)
* Player attributes from EA Sports FIFA video game
  [http://sofifa.com](http://sofifa.com). You can crawl these with the
  **PlayerSpider**

## Using Scrapy

To facilitate the crawling, I use an open source python library called
[Scrapy](http://scrapy.org). Have a look at the tutorials on their webpage if
you're not already familiar with the lib.

## Collection process

* 1: collect the matches stats and team lineups using the Match Crawler
* 2: build a list of unique player names
* 3: loop this list with the Player Crawler. Create a list of the players you
  haven't successfully crawled and again follow the third step, adjusting the
  crawling paramaters. Repeat until you've got all the players you need.

## Using Search Engines

Sometimes, a player name is rather complicated or not consistent accross
different sources. To help identify a player, the algorithm can be parameterized
to make use of search engines. Google is a prime choice thanks to its large
database and tolerance to mispelling player names. Unfortunately, the Google API
has a limited usage rate per day. Hence I suggest you use Yahoo or Bing first
and only use Google for those players you stuggle to find.
