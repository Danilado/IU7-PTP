#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
  echo Ошибка: Введите имена двух файлов в качестве первого и второго аргумента! >&2
  exit 42
fi
if [ ! -f "$1" ]; then
  if [[ "$4" == "-v" ]]; then
    echo Ошибка: файл 1 не найден!
  fi
  exit 42
fi
if [ ! -f "$2" ]; then
  if [[ "$4" == "-v" ]]; then
    echo Ошибка: файл 2 не найден!
  fi
  exit 42
fi
if [ ! -r "$1" ]; then
  if [[ "$4" == "-v" ]]; then
    echo Ошибка: недостаточно прав для доступа к файлу 1!
  fi
  exit 42
fi
if [ ! -r "$2" ]; then
  if [[ "$4" == "-v" ]]; then
    echo Ошибка: недостаточно прав для доступа к файлу 2!
  fi
  exit 42
fi

flag=""

tmp1=$(mktemp)
FIN=false
until $FIN; do
  read -r line || FIN=true
  if [ -z $flag ]; then
    if [[ "$line" == *"$3"* ]]; then
      flag="true"
      echo "$line" | grep -Eo "$3.*" >"$tmp1"
    fi
  else
    echo "$line" >>"$tmp1"
  fi
done <"$1"

if [ -z "$flag" ]; then
  if [[ "$4" == "-v" ]]; then
    echo Ошибка! В первом файле не найдено подстроки \"string:\"
  fi
  
  exit 42
fi

flag=""

tmp2=$(mktemp)
FIN=false
until $FIN; do
  read -r line || FIN=true
  if [ -z "$flag" ]; then
    if [[ "$line" == *"$3"* ]]; then
      flag="true"
      echo "$line" | grep -Eo "$3.*" >"$tmp2"
    fi
  else
    echo "$line" >>"$tmp2"
  fi
done <"$2"

if [ -z "$flag" ]; then
  if [[ "$4" == "-v" ]]; then
    echo Ошибка! Во втором файле не найдено подстроки \""$3"\"
  fi
  
  exit 42
fi


if cmp -s "$tmp1" "$tmp2"; then
  if [[ "$4" == "-v" ]]; then
    echo Файлы одинаковые
  fi
  exit 0
else
  if [[ "$4" == "-v" ]]; then
    echo Файлы разные
  fi
  exit 1
fi
