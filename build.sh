#!/bin/bash

docker compose down 
cd client
npm run build
cd ../
rm server/build -r
cp client/build -r server
docker compose up -d