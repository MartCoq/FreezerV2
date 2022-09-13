#!/bin/bash

docker rm-f $(docker ps -a -q)
docker rmi nginxf proftpdf mariadbf jenkinsf agentf
docker volume rm $(docker volume ls -q)
rm -R cloned
