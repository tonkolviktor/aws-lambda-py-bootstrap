#!/usr/bin/env bash
DIR=$(dirname $(readlink -f "$BASH_SOURCE"))

python3 -m unittest discover -s "$DIR/.."