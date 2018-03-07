import ssl
import requests
import json
import certifi


def secureGet(url, params=None, headers=None):
    #cert = certifi.where()
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
url = 'https://shuni.tel/'

resp_data = secureGet(url)
data = _process_response(resp_data)
print(data)
