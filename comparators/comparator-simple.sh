#!/bin/bash

if cmp -s "$1" "$2"; then
  if [[ "$4" == "-v" ]]; then
    echo Файлы одинаковые
  fi
  exit 0
else
  if [[ "$4" == "-v" ]]; then
    echo Файлы разные
  fi
  exit 1
fi
