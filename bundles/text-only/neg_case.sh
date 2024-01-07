#!/bin/bash

if [ -z "$1" ]; then
  echo Ошибка: Введите имя  файла в качестве первого аргумента! >&2
  exit 42
fi
if [ ! -f "$1" ]; then
  if [[ "$3" == "-v" ]]; then
    echo Ошибка: файл 1 не найден!
  fi
  exit 42
fi
if [ ! -r "$1" ]; then
  if [[ "$3" == "-v" ]]; then
    echo Ошибка: недостаточно прав для доступа к файлу 1!
  fi
  exit 42
fi

if [ ! -f "./app.exe" ]; then
  exit 42
fi
if [ ! -f "./func_tests/scripts/comparator.sh" ]; then
  exit 42
fi

if ./app.exe < "$1" > /dev/null; then
  exit 0
fi

exit 1
