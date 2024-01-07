#!/bin/bash

cases=$(cat ./config/NMAX_cases_config.txt)

for NMAX in $cases; do
  echo "$NMAX" | python3 ./source_code/ordered_input_gen.py
  echo "$NMAX" | python3 ./source_code/random_input_gen.py
done
