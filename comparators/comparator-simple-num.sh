#!/bin/bash

if [ $# -ne 2 ]; then
  exit 1
fi

out_prog=$1
out_test=$2

mask="[+-]?[0-9]+\.?[0-9]*"

clean_out_prog=$(grep -Eo "$mask" "$out_prog")
clean_out_test=$(grep -Eo "$mask" "$out_test")

if [ "$clean_out_prog" != "$clean_out_test" ]; then
  exit 1
fi

exit 0
