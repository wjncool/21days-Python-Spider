from urllib import request
from urllib import parse

url = 'https://www.baidu.com/s?'

para = {'wd':'刘德华'}
qs = parse.urlencode(para)

url += qs
resp = request.urlopen(url)
print(resp.read())

request.urlretrieve(url, 'wjn.html')
