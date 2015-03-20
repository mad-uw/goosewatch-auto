#!/bin/bash

# Go to location of update python script and run it
cd /home/deploy/goosewatch-auto
python goose_auto.py

# Go to respository location
cd /home/deploy/Datasets

# Check that we have all changes from upstream
git pull upstream autoupdate
git pull origin autoupdate

# Make sure we're in the autoupdate branch
git checkout autoupdate

# Check for changes to the repo
statusout=$(git status -s)
if [ "$statusout" = "" ]; then
  # If there aren't any changes, don't bother committing
  echo No changes
else
  # If there are changes
  echo Changes found

  # Add the changes to the repo and commit locally
  git add GooseWatch/1151GooseWatch.csv
  git commit -m "Automated update to goosewatch data"

  # Push the changes to the mad-uw autoupdate branch
  git push origin autoupdate

  # Push the changes upstream
  git push -n upstream autoupdate
fi
