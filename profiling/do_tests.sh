#!/bin/bash

i=0

while [ 10 -gt "$i" ]; do
  
  ./update_data.sh
  ./update_data.sh
  ./update_data.sh
  ./generate_input_data.sh
  
  i=$((i+1))
  
  printf '\r'
  echo -n $i
  
done
