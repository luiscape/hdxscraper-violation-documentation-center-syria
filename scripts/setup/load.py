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
CONFIG_DIR = os.path.join(p.dirname(p.dirname(p.dirname(__file__))), 'config')

def LoadConfig(file_name='dev.json', verbose=True, test=False):
  '''Load configuration parameters.'''

  config_path = os.path.join(CONFIG_DIR, file_name)

  try:
    with open(config_path) as json_file:
      config = json.load(json_file)

  except Exception as e:
    print "%s Couldn't load configuration." % item('prompt_error')
    if verbose:
      print e
    return False

  return config
