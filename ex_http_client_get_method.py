### http.client 모듈

'''
urllib.request는 get,post 두 가지 방법으로 처리를 하는데 다른 메소드도 쓰고 싶다거나, urllib 만으로는 버거울 경우 세밀한 컨트롤을 위해 사용한다.

웹 클라이언트를 작성하는 순서는 다음을 기본으로 한다.

1. 연결 객체 생성
2. 요청을 보냄
3. 응답 객체 생성
4. 응답 데이터를 읽음
5. 연결을 닫음

'''

from http.client import HTTPConnection

host = 'www.example.com'
conn = HTTPConnection(host)
conn.request('GET', '/')

r1 = conn.getresponse()
data = r1.read()

print(data)

conn.close()