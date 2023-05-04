from urllib.request import urlopen

url = "http://www.baidu.com"
resp = urlopen(url)
ht = resp.read().decode("utf-8")
print(ht)
with open("mybaidu.html",mode="w",encoding='utf-8') as f:
    f.write(ht)
print("over!")