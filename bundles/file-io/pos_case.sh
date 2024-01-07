#!/bin/bash

#   args:
#   $1  :   ./func_tests/data/pos_"${num}"_in.txt
#   $2  :   ./func_tests/data/pos_"${num}"_out.txt
#   $3  :   ./func_tests/data/pos_"${num}"_args.txt
#   $4  :   ./func_tests/data/pos_file_"${num}"_in.bin
#   $5  :   ./func_tests/data/pos_file_"${num}"_out.bin

cmd="./app.exe $(cat "$3")"

if [ -f "$4" ]; then
  # expects binary output
  cp "$4" tmp.bin
  
  if ! $cmd ./tmp.bin < "$1" >./out.txt ; then
    exit 1
  fi
  
  if ./func_tests/scripts/comparator.sh ./tmp.bin "$5"; then
    exit 0
  fi
  
  exit 1
else
  # expects regular output
  
  if ! $cmd < "$1" >./out.txt ; then
    exit 1
  fi
  
  if ./func_tests/scripts/comparator.sh ./out.txt "$2"; then
    exit 0
  fi
  
  exit 1
fi
