#!/bin/bash

set -e

pip install --target ./package feedparser
cd package
zip -r ../main.zip .
cd ../
zip -g main.zip main.py
aws lambda update-function-code --function-name newsfeed-formatter --zip-file fileb://main.zip