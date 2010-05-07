#!/bin/sh

while true; do
    wget http://buedastatus.com/check --output-document=- --output-file=- >/dev/null
    sleep 300
done
