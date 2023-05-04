'''
1.定位到2020必看片
2.从2020必看片中提取到子页面的链接地址
3.请求子页面的链接地址，拿到我们想要下载的地址
'''
import re

import requests
requests.packages.urllib3.disable_warnings()
domain = "https://www.dytt89.com/"
resp = requests.get(domain,verify = False)   #verify = False :去掉安全验证
resp.encoding = 'gb2312'   #编码方式
#print(resp.text)
resp.close()

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2 = re.compile(r"<a href='(?P<herf>.*?)'",re.S)
#obj3 = re.compile(r"◎片　　名　(？P<movie>.*？)<br />", re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)
result1 = obj1.finditer(resp.text)
child_herf_list = []
for it in result1:
    ul = it.group('ul')
    print(ul)

    #提取子页面链接
    result2 = obj2.finditer(ul)
    for itt in result2:
        #拼接地址：url+子页面地址
        child_herf = domain + itt.group('herf').strip("/")
        child_herf_list.append(child_herf)

#提取子页面内容
for herf in child_herf_list:
    child_resp = requests.get(herf,verify = False)
    child_resp.encoding = 'gb2312'
    #print(child_resp.text)
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
    #break #测试用