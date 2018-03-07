#!/usr/bin/env bash
cd /etc/ssl/ssl_certs/
#cd ${PWD}
openssl genrsa -des3 -passout pass:x -out ssl_web.pass.key 2048
openssl rsa -passin pass:x -in ssl_web.pass.key -out ssl_web.key
rm ssl_web.pass.key
openssl req -new -key ssl_web.key -out ssl_web.csr \
  -subj "/C=BD/ST=Dhaka/L=/O=apitest/OU=IT Department/CN=apitest"
openssl x509 -req -days 365 -in ssl_web.csr -signkey ssl_web.key -out ssl_web.crt
