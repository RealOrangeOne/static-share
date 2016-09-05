#!/usr/bin/env bash

set -e

if [ "$NODE_ENV" = "production" ]
then
  echo ">>> WARNING: Building in Production Mode!"
fi

uglifyjs node_modules/jquery/dist/jquery.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/jquery.js

echo ">> Building Application JS..."
browserify -t [ babelify ] static/src/js/app.js -o static/build/js/app.js

if [ "$NODE_ENV" = "production" ]
then
  echo ">> Compressing Application..."
  uglifyjs static/build/js/app.js --compress --screw-ie8 --define --stats --keep-fnames -o static/build/js/app.js
fi

echo "> JS Built!"
