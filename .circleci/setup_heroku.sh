#!/bin/bash

set -e

cat > ~/.netrc << EOF
machine api.heroku.com
    login
    password $HEROKU_API_KEY
machine git.heroku.com
    login
    password $HEROKU_API_KEY
EOF
