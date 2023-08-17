#!/bin/bash

chromium --allow-file-access-from-files "$(cat url.txt)" 2>/dev/null &
sleep 2
$(dirname $0)/bin/python $(dirname $0)/main.py
