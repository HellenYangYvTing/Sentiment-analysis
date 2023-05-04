#拿到页面源代码
#通过re提取想要的有效信息 re
import requests
import re
import csv

#url = "https://www.jd.hk/"
url = "https://movie.douban.com/top250"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
resp = requests.post(url= url,headers= headers)
page_context = resp.text
#print(resp.text)
resp.close()

#解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">'
                 r'.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                 r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>',re.S)
result = obj.finditer(page_context)
f = open("data.csv", mode="w",encoding="utf-8")
csvwriter = csv.writer(f)
for it in result:
    '''
    print(it.group("name"))
    print(it.group("year").strip())
    print(it.group("score"))
    print(it.group("num"))
    '''
    dic = it.groupdict()#字典
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over!")