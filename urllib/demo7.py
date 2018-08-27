from http.cookiejar import MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)

for cookie in cookiejar:
    print(cookie)