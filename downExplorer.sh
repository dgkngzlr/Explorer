#!/bin/bash

docker kill $(docker ps -q)

docker rm $(docker ps -aq)

docker volume prune -f

docker system prune -f
