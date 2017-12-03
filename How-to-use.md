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

To run these scripts, you must:

* install scrapy and its dependencies: `pip install scrapy`
* install the google-web-api-client: `pip install --upgrade
  google-api-python-client`
* install the json-rpc extension for scrapy: `pip install scrapy-jsonrpc`

* edit `matchcrawler.py` and change these lines of code:

  ```
  countries = ['England']

  seasons = ['2009/2010', '2010/2011', '2011/2012', '2012/2013', '2013/2014','2014/2015', '2015/2016', '2016/2017', '2017/2018']
  ```

...to anything that you prefer.

(TODO: Add command-line processing)

Then run `scrapy crawl match` from the command line.

The 'England' scrape in the codeblock above takes about 1 hour.

This scrapes the data-serving api-website of the Company 'Enetscores.com'. Their
motto is "Free Livescore for Everyone". See https://www.enetscores.com/ for an
human-readable site,
http://json.mx-api.enetscores.com/live_data/actionzones/2543586/0?_=1 for a
data-serving site.

The scrape will save numerous XML files to your hard drive, one file for each
match.

You'll import these XML files into an Sqlite database later, with one of the
scripts located in the `footballData/src/dataProcessing/` directory of this
repository.

---
