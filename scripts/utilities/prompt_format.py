#!/usr/bin/python
# -*- coding: utf-8 -*-

from termcolor import colored as color

def item(i):
  dictionary = {
    'prompt_bullet': color(u" →", "blue", attrs=['bold']),
    'prompt_error':  color(u" ERROR:", "red", attrs=['bold']),
    'prompt_success': color(u" SUCCESS:", "green", attrs=['bold']),
    'prompt_ping': color(u" *", "green", attrs=['bold']),
    'prompt_warn': color(u" WARN:", "yellow", attrs=['bold'])
  }

  return dictionary[i].encode('utf-8')


if __name__ == '__main__':
  item()
