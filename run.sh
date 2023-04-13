#!/bin/bash
IP=0.0.0.0
PORT=60000
URL_ROOT=/translator
CONFIG=config.json

# pull the latest code from the repo
git pull origin master

# run the virtual environment
source env/bin/activate

# generate the model configuration file
python generate.py

# serve the MT models using OpenNMT
onmt_server --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG