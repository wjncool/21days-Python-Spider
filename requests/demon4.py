import requests

#获取cookie
# response = requests.get('http://www.baidu.com')
# print(response.cookies.get_dict())

url = 'http://www.renren.com/PLogin.do'
data = {'email': '970138074@qq.com', 'password': 'pythonspider'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

session = requests.Session()
session.post(url, data=data, headers=headers)

response = session.get('http://www.renren.com/880151247/profile')

with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)