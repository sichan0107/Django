### POST 방식으로 요청해보기

from http.client import HTTPConnection
from urllib.parse import urlencode

host = '127.0.0.1:8000'
params = urlencode({
    'lang' : 'python',
    'name' : '송시찬',
    'email' : 'scsong@naver.com'
})

headers ={
    'Content-Type' : 'application/x-www-form-urlencoded',
    'Accept' : 'text/plain'
}

conn = HTTPConnection(host)
conn.request('POST', '', params, headers)
resp = conn.getresponse()

print(resp.status, resp.reason)

data = resp.read()
print(data.decode('utf-8'))

conn.close()