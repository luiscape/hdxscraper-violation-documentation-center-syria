#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import scraperwiki
import progressbar as pb
from bs4 import BeautifulSoup

# Below as a helper for namespaces.
# Looks like a horrible hack.
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from utilities.prompt_format import item

#
# It seems that the site uses session tokens
# to recognize single sessions and possibly
# avoid automated data collection.
#
start = 1

def ExctractTotalPages(endpoint, verbose=False):
  '''Extracts the total number of pages an endpoint has.'''

  #
  # Making request.
  #
  token = endpoint['token']
  u = '%s/%s/%s' % (endpoint['url'], start, token)
  r = requests.get(u)

  if verbose:
    print 'Endpoint data: %s' % u

  #
  # Parsing data.
  #
  soup = BeautifulSoup(r.content, 'html.parser')
  body = soup.findAll("div", class_='tablePgaination')

  #
  # Extracting total.
  #
  href = str(body[0].findAll('a', href=True)[-1]['href'])
  total = href.replace(endpoint['url'], '').replace(token, '').replace('/', '')

  return int(total)


def ScrapeEndpoint(endpoint, verbose=False):
  '''Scrapes data from the Violation Documentation Center in Syria website.'''

  print "%s Scraping the VDC website: %s." % (item('prompt_bullet').decode('utf-8'), endpoint['name'])

  #
  # Calculate total.
  #
  start = 1
  total = ExctractTotalPages(endpoint)

  if total == False:
    return False

  #
  # Configure and start progress bar.
  #
  widgets = [item('prompt_ping'), ' Progress:', pb.Percentage(), ' ', pb.Bar('-'), ' ', pb.ETA(), ' ']
  pbar = pb.ProgressBar(widgets=widgets, maxval=total).start()

  token = endpoint['token']
  keys = endpoint['keys']
  complete_output = []
  for index in range(start, total):

    #
    # Assemble URL.
    #
    u = '%s/%s/%s' % (endpoint['url'], index, token)

    if verbose:
      print 'Querying URL: %s' % u

    #
    # Download data from Motivate's website.
    #
    r = requests.get(u)

    #
    # Find data with BeautifulSoup.
    #
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.findAll("table")


    #
    # Iterates over every row.
    #
    out = []
    i = 0
    for row in table[0].findAll('tr'):
      col = [ d.text.replace('\t', '').replace('\n', '') for d in row.findAll('td') ]
      if i <= 1:
        i += 1
        continue

      else:
        out.append(dict(zip(keys, col)))
        i += 1

    #
    # Append results and update progress bar.
    #
    complete_output += out
    pbar.update(index)
    index += 1


  #
  # Closes progress bar and
  # returns output.
  #
  pbar.finish()
  return complete_output
