#!/usr/bin/env sh



if [ "$PRODUCTION" -eq 1 ]
then
  echo "PRODUCTION MODE"
  yarn install --production=true
  wait
  yarn build
else
  echo "DEVELOPMENT MODE"
  yarn install --production=false
fi
