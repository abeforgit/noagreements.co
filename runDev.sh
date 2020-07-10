#! /bin/sh

build='true'

while getopts ":n" opt; do
  case $opt in
  n)
    build=''
    ;;
  *) ;;
  esac

done

shift $((OPTIND - 1))

if [ -n "$build" ]; then
  docker-compose -f docker-compose.yml -f docker-compose-dev.yml build
fi

docker-compose -f docker-compose.yml -f docker-compose-dev.yml up
