#!/bin/bash

cd client
npm run build
cd ../
rm server/build -r
cp client/build -r server
docker compose down 
docker compose up -d