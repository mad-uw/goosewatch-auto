#!/bin/sh
cd /home/jmccarth/goosewatch-auto
python goose_auto.py
cd /home/jmccarth/Datasets
statusout=$(git status -s)
if [ "$statusout" = "" ]; then
  echo No changes
else
  echo Changes
fi
