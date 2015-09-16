## VDC Scraper
Scraper for data from the [Violations Documentation Center in Syria](http://www.vdc-sy.info/index.php/en/).

[![Build Status](https://travis-ci.org/luiscape/hdxscraper-violation-documentation-center-syria.svg)](https://travis-ci.org/luiscape/hdxscraper-violation-documentation-center-syria) [![Coverage Status](https://coveralls.io/repos/luiscape/hdxscraper-violation-documentation-center-syria/badge.svg?branch=master&service=github)](https://coveralls.io/github/luiscape/hdxscraper-violation-documentation-center-syria?branch=master)


## Run and Setup
This scraper makes use of a `Makefile`. Clone it, navigate to this repository's directory, and run the following in your terminal:

```shell
$ make setup && make test
$ make run
```

The output should be available as a `SQLite` database called `scraperwiki.sqlite`.
