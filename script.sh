#!/bin/bash
create_cert=$(grep 'create_cert' config.yaml | awk -F': ' '{print $2}')

if $create_cert; then
  CERT_FOLDER="nginx/certs"
  if [ ! -d "$CERT_FOLDER" ]; then
    echo "Folder doesn't exist，creating：$CERT_FOLDER"
    mkdir -p "$CERT_FOLDER"
    openssl genpkey -algorithm RSA -out nginx/certs/server.key
    openssl req -new -key nginx/certs/server.key -out nginx/certs/server.csr -config ssl.conf
    openssl x509 -req -days 365 -in nginx/certs/server.csr -signkey nginx/certs/server.key -out nginx/certs/server.crt
  else
    echo "Folder exist：$CERT_FOLDER"
  fi
fi

awk '/#backend setting/, EOF' config.yaml > backend/login_backend/config.yaml

current_dir=$(pwd)
cd frontend || exit
npm run build
cd "$current_dir"

docker compose up -d