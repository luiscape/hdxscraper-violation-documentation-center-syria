# #!/usr/bin/python
# # -*- coding: utf-8 -*-

# # system
# import os
# import sys
# dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# sys.path.append(os.path.join(dir, 'scripts'))

# # testing
# import mock
# import unittest
# from mock import patch

# # program
# import config.load as Config
# import scripts.scraper as Scraper

# class CheckCollectorFunctions(unittest.TestCase):
#   '''Unit tests checking if the collector is working as expected.'''

#   def test_wrapper_doesnt_fail(self):
#     assert Collect.Main() != False

#   def test_fetch_data_function(self):
#     assert Collect.FetchData(url='http://localhost:8080') == False

#   def test_processing_works(self):
#     data = Collect.DownloadAndProcessData()
#     assert type(data) == list

#   def test_clean_table_fails(self):
#     assert Collect.CleanTable('foo') == False


# class CheckPatches(unittest.TestCase):
#   '''Unit tests that check if the patches are doing what they are supposed to do.'''

#   def test_read_all_records_works(self):
#     d = Database.ReadAllRecords('unprocessed_data')
#     assert type(d) == list
#     assert Database.ReadAllRecords('unprocessed_data') != False
