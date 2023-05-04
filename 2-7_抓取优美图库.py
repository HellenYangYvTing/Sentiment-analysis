import requests
from bs4 import BeautifulSoup
import time

url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = 'utf-8'
resp.close()
#print(resp.text)

#把源代码交给Bs4
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div",class_="TypeList").find_all("img")
print(alist)
for a in alist:
   src = a.get('src')
   print(src)
   #下载图片
   img_resp = requests.get(src)
   #img_resp.content  #这里拿到是字节
   img_name = src.split("/")[-1] #拿到url最后/以后的内容
   with open("img/"+img_name,mode="wb")as f:
      f.write(img_resp.content) #图片内容写入文件

   print("over!",img_name)
   time.sleep(1)

print("all over!!")
