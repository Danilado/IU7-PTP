#!/bin/bash

optimizations=$(cat ./config/O_cases_config.txt)
nmax_values=$(cat ./config/NMAX_cases_config.txt)

(
  cd ./source_code || exit 1
  for opt in $optimizations; do
    for FILE in ./*sort.c; do
      for nmax in $nmax_values; do
        gcc "$FILE" \
        -std=c99 \
        -"${opt}" -DNMAX="${nmax}" \
        -o "../executables/${FILE%.c}_${opt}_${nmax}.exe"
      done
    done
  done
)
