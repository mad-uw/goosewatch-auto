#!/bin/bash
cd /home/jmccarth/goosewatch-auto
python goose_auto.py
cd /home/jmccarth/Datasets
git pull
statusout=$(git status -s)
if [ "$statusout" = "" ]; then
  echo No changes
else
  echo Changes
  git add GooseWatch/1151GooseWatch.csv
  git commit -m "Automated update to goosewatch data"
fi
