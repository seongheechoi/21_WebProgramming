# from urllib.parse import urlparse
# result = urlparse("http://www.python.org:80/guido/python.html;philosophy?overall=3#n10")
# print(result)

'''
# GET 방식 요청
from urllib.request import urlopen

f = urlopen("http://www.example.com")
print(f.read(500).decode('utf-8'))
'''

"""
# POST 방식 요청
from urllib.request import urlopen
data = "language=python&framework=django"
f = urlopen("http://127.0.0.1:8000", bytes(data, encoding='utf-8'))
print(f.read(500).decode('utf-8'))
"""

# Request 클래스로 요청 헤더 지정
'''
from urllib.request import urlopen, Request
from urllib.parse import urlencode

url = "http://127.0.0.1:8000"
data = {
    'name' : '최성희',
    'email' : 'seonghee.choi@lge.com',
    'url' : 'sso.lge.com',
    }
encData = urlencode(data)
print(data)
print(encData)
postData = bytes(encData, encoding='utf-8')
print(postData)
req = Request(url, data=postData)
print(req)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read(500).decode('utf-8'))
'''

# urllib.request 모듈 예제
from urllib.request import urlopen
from html.parser import HTMLParser

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def parse_image(data):
    parser = ImageParser()
    parser.feed(data)
    dataSet = set(x for x in parser.result)
    return dataSet

def main():
    url = "http://www.google.co.kr"

    with urlopen(url) as f:
        charset = f.info().get_param('charset')
        data = f.read().decode(charset)

    dataSet = parse_image(data)
    print("\n>>>>>>> Fetch Image from", url)
    print('\n'.join(sorted(dataSet)))

if __name__ == '__main__':
    main()