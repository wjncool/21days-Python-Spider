# 大鹏董成鹏的主页：http://www.renren.com/880151247/profile
# 人人网登陆主页：http://www.renren.com/SysHome.do

from urllib import request, parse
from http.cookiejar import CookieJar

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


# 1. 登陆
def get_opener():
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener


def login_renren(opener):
    # 1.4 使用opener发送登陆的请求（人人网的邮箱和密码）
    data = {'email': '970138074@qq.com', 'password':'pythonspider'}
    data = parse.urlencode(data).encode('utf-8')
    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, headers=headers, data=data)
    opener.open(req)


# 2. 访问个人主页
def visit_profile(opener):
    url = 'http://www.renren.com/880151247/profile'
    req = request.Request(url, headers=headers)
    resp = opener.open(req)
    with open('profile.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
