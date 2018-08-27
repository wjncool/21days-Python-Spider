from urllib import request
url = 'http://httpbin.org/get'
# 1. 使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({'http': '139.224.24.26:8888'})
# 2. 使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3. 使用opener发送一个请求
resp = opener.open(url)
print(resp.read().decode('utf-8'))