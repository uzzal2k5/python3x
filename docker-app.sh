#!/usr/bin/env bash
docker run -itd --name shuni_apps \
    -v /root/docker-apps/var/apps/graphapi:/var/apps/graphapi:ro \
    uzzal2k5/shuni_apps

openssl s_client -showcerts -connect shuni.live:443 </dev/null 2>/dev/null|openssl x509 -out /etc/ssl/certs/shuni_web.crt
export SSL_CERT_FILE=/etc/ssl/certs/shuni_web.crt

openssl s_client -showcerts -connect 139.59.29.195:443 </dev/null 2>/dev/null|openssl x509 -outform PEM >/etc/ssl/certs/shuni_web.pem

python3 facebookscrap.py --ca-certificate=/var/apps/mycertfile.pem

curl --cacert /etc/ssl/certs/shuni_web.crt https://shuni/api/v1/shuni/post/
curl --cacert  /etc/ssl/certs/shuni_web.crt https://shuni.live/api/v1/shuni/post/


mykey = '/etc/ssl/certs/shuni_web.key'
mycert = '/etc/ssl/certs/shuni_web.crt'
r =  requests.get(url,headers=header,cert=certificate,timeout=5,verify=False




import requests
url = "https://www.thenewboston.com/forum/category.php?id=15&orderby=recent&page=1"
response = requests.get(url, verify=False)
response.status_code
openssl s_client -connect 192.168.122.111:443 -CAfile cacert.pem





import urllib.request
x = urllib.request.urlopen('https://192.168.122.111/api/v1/shuni/post/')
r =  requests.get(x, stream=True)
print(x.read())
print (r.read())


tarball_url = 'https://github.com/requests/requests/tarball/master'
r = requests.get(tarball_url, stream=True)