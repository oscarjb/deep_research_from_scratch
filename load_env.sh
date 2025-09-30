#!/usr/bin/env bash
CONFIG_FILE=./.env
if [ -f $CONFIG_FILE ]; then
  export $(grep -v '^#' $CONFIG_FILE | xargs)
  echo "Done $CONFIG_FILE."
else
  echo "Environment file $CONFIG_FILE not found."
fi

