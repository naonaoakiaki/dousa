import urllib.request

url = "http://localhost:5000"
res = urllib.request.urlopen(url)
print(res.read().decode('utf8'))
