#!/usr/bin/env sh

# Update schema information
yarn generate

wait

yarn build
