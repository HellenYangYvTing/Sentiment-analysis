import requests

url = "https://movie.douban.com/j/chart/top_list"

param = {
    "type": "24",
    "interval_id": "100:90",
    "action":"",
    "start":1,
    "limit":20,
}
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}

resp = requests.get(url=url, params=param,headers=headers)
print(resp.status_code)
print(resp.text)
resp.close()