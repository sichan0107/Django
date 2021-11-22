from urllib.request import Request, HTTPCookieProcessor, build_opener

url ='http://localhost:8000/cookie/'

cookie_handler = HTTPCookieProcessor() #  cookie 핸들러 생성

opener = build_opener(cookie_handler) # 쿠키 데이터 저장 객체는 디폴트로 CookieJar

req = Request(url)
res = opener.open(req)

print("========== first ==========")
print(res.info())
print(res.read().decode('uth-8'))

print("========= second ==========")
data = "language=python&framework=django"
encData = bytes(data, encoding='utf-8')

req = Request(url, encData)
res = opener.open(req)

print(res.info())
print(res.read().decode('utf-8'))