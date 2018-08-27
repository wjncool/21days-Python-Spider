from urllib import request, parse

url = 'http://www.baidu.com/s?username=zhiliao'
result1 = parse.urlsplit(url)
result2 = parse.urlparse(url)

print(result1)
print(result2)
