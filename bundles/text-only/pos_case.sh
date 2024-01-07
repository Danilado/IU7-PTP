#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
  echo Ошибка: Введите имена двух файлов в качестве первого и второго аргумента! >&2
  exit 42
fi
if [ ! -f "$1" ]; then
  if [[ "$3" == "-v" ]]; then
    echo Ошибка: файл 1 не найден!
  fi
  exit 42
fi
if [ ! -f "$2" ]; then
  if [[ "$3" == "-v" ]]; then
    echo Ошибка: файл 2 не найден!
  fi
  exit 42
fi
if [ ! -r "$1" ]; then
  if [[ "$3" == "-v" ]]; then
    echo Ошибка: недостаточно прав для доступа к файлу 1!
  fi
  exit 42
fi
if [ ! -r "$2" ]; then
  if [[ "$3" == "-v" ]]; then
    echo Ошибка: недостаточно прав для доступа к файлу 2!
  fi
  exit 42
fi

if [ ! -f "./app.exe" ]; then
  exit 42
fi
if [ ! -f "./func_tests/scripts/comparator.sh" ]; then
  exit 42
fi

./app.exe < "$1" > ./out.txt

if [ ! $? ]; then
  exit 1
fi

if ./func_tests/scripts/comparator.sh ./out.txt "$2"; then
  exit 0
else
  exit 1
fi
