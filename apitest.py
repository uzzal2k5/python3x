import ssl
import requests
import json
import certifi
import  time

def secureGet(url, params=None, headers=None):
    # cert = certifi.where()
    # return requests.get(url=url, params=params, headers=headers, cert=cert, verify=True)
    return requests.get(url=url, params=params, headers=headers)


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


# url = 'https://172.17.0.4/'
# url = 'https://shuni.tel/'
url = 'https://shuni.tel/api/v1/shuni/post/'

start = time.time()
resp_data = secureGet(url)
data = _process_response(resp_data)
# print(data)
# print(resp_data.content.decode('utf-8'))
print(resp_data.status_code)
print(resp_data.status_code==requests.codes.ok)
print(requests.codes.popitem())

end = time.time()

print(end - start)
