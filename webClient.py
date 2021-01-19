import urllib.request
with urllib.request.urlopen('http://www.example.com/') as response:
   html = response.read().decode('utf-8')

print(html)
#print(urllib.request.urlopen("http://www.exmaple.com").read().decode('utf-8'))