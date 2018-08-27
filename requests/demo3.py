import requests

url = 'http://httpbin.org/ip'

proxy = {
    'http': '1.194.133.171:39383'
}

response = requests.get(url, proxies=proxy)
print(response.text)