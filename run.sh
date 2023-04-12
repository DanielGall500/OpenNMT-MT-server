#!/bin/bash
IP=0.0.0.0
PORT=60000
URL_ROOT=/translator
CONFIG=conf.json

python generate.py

onmt_server --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG