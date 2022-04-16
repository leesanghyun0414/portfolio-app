#!/usr/bin/env sh


ls

cat src/router/router.ts

cat src/pages/MenuPage.vue

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
