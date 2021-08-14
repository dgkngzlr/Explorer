#!/bin/bash

cd ../fabric-samples/fabcar

./startFabric.sh javascript

cd ../../Explorer

sudo cp -r ../fabric-samples/test-network/organizations ./

echo "Python packages are installing ..."

sudo apt install python3-pip

pip3 install glob2

./copy_org_to_exp.sh

docker-compose -f docker-compose.yaml up -d

echo "Exlplorer can be accessed from localhost:8080 "
