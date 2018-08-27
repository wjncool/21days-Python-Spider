from urllib import request

# 大鹏董成鹏的主页：http://www.renren.com/880151247/profile
# 人人网登陆主页：http://www.renren.com/SysHome.do

# 1.不使用cookie请求大鹏的主页
dapeng_url = 'http://www.renren.com/880151247/profile'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Cookie': 'anonymid=jjsown0tdf1309; _r01_=1; depovince=GW; JSESSIONID=abcu_3-iyKXRf4EQOW0vw; ick_login=60119beb-ae11-4240-889f-6fc58f5ea1ee; first_login_flag=1; ln_uact=15195775520; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20120919/2215/h_main_cz7F_2f7d0000454e1376.jpg; wp_fold=0; XNESSESSIONID=c46bdf7b4e93; jebecookies=047e62c8-5906-4451-8130-129850150b0a|||||; _de=AC7D98FED760A21B2804709FE7AD3068; p=0dd46e4d53c77beeb92f31283db810694; t=2c2585895ea823e6c9a0d66726bb1d604; societyguester=2c2585895ea823e6c9a0d66726bb1d604; id=239860894; xnsid=8b1d00ea; loginfrom=syshome'
}
req = request.Request(url=dapeng_url, headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('renren.html', 'w', encoding='utf-8') as fp:
    # write函数必须写入一个str的数据类型
    # resp.read()读出来的是一个bytes数据类型
    # bytes -> decode -> str
    # str -> encode -> bytes
    fp.write(resp.read().decode('utf-8'))