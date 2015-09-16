#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv

def StoreRecords(data, path='data.csv', verbose=False):
  '''Store records in a CSV file.'''

  try:
    with open(path, 'wb') as f:
      w = csv.writer(f)
      w.writerow(data[0].keys())
      for record in data:
        w.writerow([ value.encode('utf-8') for value in record.values() ])

  except Exception as e:
    print 'Could not store data in CSV.'
    print e
    return False
