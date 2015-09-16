#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from scripts.setup.load import LoadConfig
from scripts.scraper.store import StoreRecords
from scripts.scraper.scrape import ExctractTotalPages, ScrapeEndpoint

if __name__ == '__main__':

  config = LoadConfig('dev.json')

  i = 0
  for endpoint in config['endpoints']:
    data = ScrapeEndpoint(endpoint, verbose=True)
    StoreRecords(data, path='data_{index}.csv'.format(index=i))
    i += 1

