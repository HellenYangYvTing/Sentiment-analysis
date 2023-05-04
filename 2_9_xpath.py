import requests
from lxml import etree

url = "https://beijing.zbj.com/search/f/?kw=saas"
resp = requests.get(url)
#print(resp.text)
resp.close()

#解析
html = etree.HTML(resp.text)
#拿到每一个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    #print(divs.get(text))
    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")
    title = div.xpath("./div/div/a[1]/div[2]/div[2]/p/text()")
    print(price)