from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = 'http://localhost:8000'

data = {
    'name' : '송시찬'
    , 'email' : 'scc0103@naver.com'
    , 'url' : 'http://www.naver.com'
}

# data를 쿼리스트링으로 변환
encData = urlencode(data) 
print(encData) # name=%EC%86%A1%EC%8B%9C%EC%B0%AC&email=scc0103%40naver.com&url=http%3A%2F%2Fwww.naver.com

postData =bytes(encData, encoding='utf-8')
print(postData) # b'name=%EC%86%A1%EC%8B%9C%EC%B0%AC&email=scc0103%40naver.com&url=http%3A%2F%2Fwww.naver.com'

req = Request(url, data=postData)
print(req) # <urllib.request.Request object at 0x00000280A2789340>

req.add_header('Content-Type', 'application/x-www-from-urlencoded')

f = urlopen(req)
print(f) # <http.client.HTTPResponse object at 0x00000280A4558610>

print(f.info())

print(f.read(500).decode('utf-8'))

# f를 utf-8로 디코드 후 출력

'''
<!doctype html>

<html lang="en-us" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>The install worked successfully! Congratulations!</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" type="text/css" href="/static/admin/css/fonts.css">
        <style>
          html {
            line-height: 1.15;
          }
          a {
            color: #19865C;
          }
          header {
            border-bottom: 1
            
'''