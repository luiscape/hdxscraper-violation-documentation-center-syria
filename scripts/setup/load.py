#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import csv
import json

# Below as a helper for namespaces.
# Looks like a horrible hack.
dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(dir)

from os import path as p
from utilities.prompt_format import item

#
# Global variables.
#
DATA_DIR = p.dirname(p.dirname(p.dirname(__file__)))
DEV_CONFIG_PATH = p.join(DATA_DIR, 'config', 'dev.json')
PROD_CONFIG_PATH = p.join(DATA_DIR, 'config', 'prod.json')


def LoadConfig(config_path=DEV_CONFIG_PATH, verbose=True):
  '''Load configuration parameters.'''

  try:
    with open(config_path) as json_file:
      config = json.load(json_file)

  except Exception as e:
    print "%s Couldn't load configuration." % item('prompt_error')
    if verbose:
      print e
    return False

  #
  # Perform basic quality checks.
  #
  if len(config['hdx_key']) is not 36:
    print '%s API key seems to be wrong. Please check: %s' % (item('prompt_error'), os.path.split(config_path)[1])
    return False

  return config
