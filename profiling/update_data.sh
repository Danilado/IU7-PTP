#!/bin/bash

(
  cd ./executables || exit 1
  for exec_file in ./*.exe; do
    filename=$(echo "$exec_file" | grep -o "^[^[:digit:]]*[[:digit:]][^[:digit:]]*")
    nmax=$(echo "$exec_file" | grep -o "[[:digit:]]*\.exe")
    
    filename="${filename%.exe}"
    nmax="${nmax%.exe}"
    
    $exec_file < ../input_data/ordered_"${nmax}".txt >> ../data/"${filename}"ordered.txt
    $exec_file < ../input_data/random_"${nmax}".txt >> ../data/"${filename}"random.txt
  done
)
