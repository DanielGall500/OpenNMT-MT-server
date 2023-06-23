#!/bin/bash
IP=127.0.0.1
PORT=60000
URL_ROOT=/translator
CONFIG=model-hoster/config/config.json
python model-hoster/config/generate.py
onmt_server --ip $IP --port $PORT --url_root $URL_ROOT --config $CONFIG
