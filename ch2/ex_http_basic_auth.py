from urllib.request import HTTPBasicAuthHandler, build_opener

auth_handler = HTTPBasicAuthHandler() #http 인증 핸들러 생성

auth_handler.add_password(realm='ssc', user='scsong', passwd='sichan', uri='http://localhost:8000/auth/')
opener = build_opener(auth_handler) # 핸들러를 오프너에 등록
resp = opener.open('http://localhost:8000/auth/') #오프너의 open함수를 쓰면 서버에값이 전송됨.

print(resp.read().decode('utf-8'))
