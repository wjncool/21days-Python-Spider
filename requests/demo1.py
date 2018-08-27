import requests

params = {'wd': '中国'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
response = requests.get('https://www.baidu.com/s', params=params, headers=headers)

with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))

print(response.url)
