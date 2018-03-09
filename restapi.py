import requests
import ssl
import json
import certifi
import urllib.request
import urllib3.request

# # import urllib.request as urlrq
# # resp = urlrq.urlopen('https://172.17.0.4/', cafile=certifi.where())
#
# # requests.packages.urllib3.disable_wornings()
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context =_create_unverified_https_context
#
# # req = requests.get('http://127.0.0.1:5000/')
# req = requests.get('https://172.17.0.4/')
# # req = requests.get('https://github.com/timeline.json')
# data = req.text
# print(data)


#
#
#
# # r = requests.get('https://api.github.com/events')
# # data = r.json()
# # print(data)


def get(url, params=None, headers=None):
    return requests.get(url=url, params=params, headers=headers, verify=False)


def _process_response(response):
    try:
        text = json.loads(response.text) if response.text else {}
    except ValueError:
        return response.text
    else:
        if 'error' in text:
            # raise SSLError(status_code=text['error'])
            raise ssl.SSLError(status_code=text['error'])
    return text


x = urllib.request.urlopen('https://shuni.tel/api/v1/shuni/post/')

url = urllib.request.Request('https://shuni.tel/api/v1/shuni/post/')


context = ssl.create_default_context()
#ctx = ssl.SSLContext.load_default_certs()
host = urllib3.connection_from_url(url)
print(host)
version = ssl.OPENSSL_VERSION
info = ssl.OPENSSL_VERSION_INFO
v_num = ssl.OPENSSL_VERSION_NUMBER
hex_v_num = hex(v_num)
vri_path = ssl.get_default_verify_paths()

# cert = ssl.get_server_certificate('172.168.10.4', ssl_version=2, ca_certs=None)

# cert = ssl.get_server_certificate(host, ssl_version=2, ca_certs='apitest')
# print(cert)
# print(cert)
# cert = {'subject': ((('commonName', 'apitest'),),)}
# ssl.match_hostname(cert, "apitest")
context = ssl.create_default_context()
print(context)
resp_data = get(url)
data = _process_response(resp_data)
print(resp_data)
print(data)

# print(version)
# print(info)
# print(v_num)
# print(hex_v_num)

#r = urllib.request.urlopen(url, stream=True)
data = urllib.request.urlopen(url)
testdata = data.read().decode('utf-8')
print(testdata)
