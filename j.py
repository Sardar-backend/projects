from urllib.request import urlopen
import json
with urlopen('https://jsonplaceholder.typicode.com/comments') as x:
    d=x.read()
f=list(json.loads(d))
for j in f:
    print(j['name'])
