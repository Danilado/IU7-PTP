#!/bin/bash

cmd="./app.exe $(cat "$2")"

if $cmd<"$1">/dev/null; then
  exit 1
fi

exit 0
