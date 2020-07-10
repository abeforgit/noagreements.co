#! /bin/sh

build='true'
migrate=''

while getopts ":n:m" opt; do
  case $opt in
  n)
    build=''
    ;;
  m)
    migrate='true'
    ;;
  *) ;;
  esac

done

shift $((OPTIND - 1))

if [ -n "$build" ]; then
  docker-compose -f docker-compose.yml -f docker-compose-dev.yml build
fi

if [ -n "$migrate" ]; then
  docker-compose -f docker-compose.yml -f docker-compose-dev.yml run web python3 manage.py migrate
fi

docker-compose -f docker-compose.yml -f docker-compose-dev.yml up

