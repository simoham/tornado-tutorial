#!/bin/sh
#
branch=$(git rev-parse --abbrev-ref HEAD)
commit=$(git log --format=format:"%H" |head -n 1)

docker build -t tornadoapi-$branch:$commit .

