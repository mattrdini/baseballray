#!/usr/bin/python

import os, sys

path = "/Users/athena/Sites/baseballray/data/rosters/"
dirs = os.listdir(path)

for file in dirs:
    print file
