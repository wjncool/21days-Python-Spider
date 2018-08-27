from urllib import request, parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=pyth'

# resp = request.urlopen(url)
# print(resp.read())
#
# request.urlretrieve(url ,'test.html')

url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8D%97%E4%BA%AC&needAddtionalResult=false'

data = {
    'first': ']true',
    'pn': '1',
    'kd': 'ffmpeg'

}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_ffmpeg?px=default&city=%E5%8D%97%E4%BA%AC'
}

req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
