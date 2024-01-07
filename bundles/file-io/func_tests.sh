#!/bin/bash

errcount=0

for FILE in ./func_tests/data/pos_*_in.txt; do
  num=$(echo "$FILE" | grep -Eo "[0-9][0-9]")
  if [ -z "$num" ]; then break; fi
  echo -n POS TEST "$num"
  if bash ./func_tests/scripts/pos_case.sh \
  ./func_tests/data/pos_"${num}"_in.txt \
  ./func_tests/data/pos_"${num}"_out.txt \
  ./func_tests/data/pos_"${num}"_args.txt \
  ./func_tests/data/pos_file_"${num}"_in.bin \
  ./func_tests/data/pos_file_"${num}"_out.bin
  then
    echo " PASSED"
  else
    echo " FAILED"
    errcount=$((errcount+1))
  fi
  
  rm -f tmp.bin
done

for FILE in ./func_tests/data/neg_*_in.txt; do
  num=$(echo "$FILE" | grep -Eo "[0-9][0-9]")
  if [ -z "$num" ]; then break; fi
  echo -n NEG TEST "$num"
  if bash ./func_tests/scripts/neg_case.sh \
  ./func_tests/data/neg_"${num}"_in.txt \
  ./func_tests/data/neg_"${num}"_args.txt
  then
    echo " PASSED"
  else
    echo " FAILED"
    errcount=$((errcount+1))
  fi
done

echo FAILED TEST COUNT: "$errcount"
exit "$errcount"
