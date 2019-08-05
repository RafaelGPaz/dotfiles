#!/usr/bin/env bash

URL=$1

M3U8="$(youtube-dl -g $URL)"

open -a "quicktime player" $M3U8
