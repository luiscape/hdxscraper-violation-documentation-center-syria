#!/bin/bash

#
# Creating a virtual environment
# and installing dependencies.
#
virtualenv venv
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt

#
# Creates data folder.
#
mkdir data

#
# Setup database.
#
python scripts/setup/
