#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys

dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
dir = os.path.join(dir, 'scripts')
sys.path.append(dir)

from setup.load import LoadConfig
from utilities.prompt_format import item
from utilities.database import CleanTable, StoreRecords
from scraper.scrape import ExctractTotalPages, ScrapeEndpoint

__version__ = 'v.0.1.1'

def Main():
  '''Program wrapper.'''

  config = LoadConfig('dev.json')

  print '%s Version: %s' % (item('prompt_bullet'), __version__)

  for endpoint in config['endpoints']:
    data = ScrapeEndpoint(endpoint, verbose=config['verbose'])

    #
    # Clean table and store new records.
    #
    CleanTable(endpoint['name'])
    StoreRecords(data, endpoint['name'])


#
# Loading configuration and
# running program.
#
if __name__ == '__main__':

  try:
    Main()
    print '%s VDC scraped successfully.' % item('prompt_success')

  except Exception as e:
    print '%s VDC scraper failed.' % item('prompt_error')
    print e
