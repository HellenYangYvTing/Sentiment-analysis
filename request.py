import requests

query = input("请输入你喜欢的明星：")
url = f'https://www.baidu.com/s?wd={query}'

Hd = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
resp = requests.get(url, headers=Hd)  #处理一个小小的反爬

print(resp)
print(resp.text)