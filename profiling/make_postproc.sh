#!/bin/bash

# Кусочно-линейный

## Наилучший случай
(
  cd ./preproc_data || exit 1
  printf "1\n\n%s.svg\n" "../postproc_svg/avg_ordered" | \
  python3 ../postproc_file.py
)

## Случайные массивы
(
  cd ./preproc_data || exit 1
  printf "1\n1\n%s.svg\n" "../postproc_svg/avg_random" | \
  python3 ../postproc_file.py
)

# С ошибкой
(
  cd ./preproc_data || exit 1
  printf "2\n\n%s.svg\n" "../postproc_svg/err_o2" | \
  python3 ../postproc_file.py
)

# С усами
(
  cd ./preproc_data || exit 1
  filename="qsort_O2_random"
  printf "3\n%s\n%s.svg\n" "${filename}" "../postproc_svg/moustache_${filename}" | \
  python3 ../postproc_file.py
)

