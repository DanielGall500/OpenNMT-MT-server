#!/bin/bash

# serve the MT models using OpenNMT
gunicorn --workers 4 app.server:app 
