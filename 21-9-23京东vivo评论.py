import requests
import csv
import re
import time

comment_url = 'https://club.jd.com/comment/productPageComments.action'

f = open("10-18-data.csv", mode="a", encoding="utf-8", newline='')
csvwriter = csv.writer(f)
#row = ('评论', '评分')
#csvwriter.writerow(row)

for i in range(200):
    print(i)
    page = i
    params = {
        'productId': 100016115902,  # 商品id，先写死
        'score': 2,
        'sortType': 5,
        'page': page,
        'pageSize': 10,
        'callback': 'fetchJSON_comment98',
        'isShadowSku': 0,
        'fold': 1
    }

    headers = {
        'cookie':'shshshfpa=980322f4-0d72-08ea-9cb2-4fcadde80a00-1562576627; shshshfpb=ymAFpsvPn5OjLe2TxXJVyZQ==; __jdu=16150341377512100580391; user-key=0245721f-bdeb-4f17-9fd2-b5e647ad7f3e; PCSYCityID=CN_110000_110100_110108; mt_xid=V2_52007VwMVUllZUF8fSx9aAWcAElNcXFtbHUEZbAFkVxMBXVgARhtPHF0ZYgUXBUELWg4fVUxUAGEGFFdVXlJZSnkaXQZnHxJTQVhSSx9OEl4NbAARYl1oUmoaQRpZB2YKF1JbaFdZGUo=; areaId=1; ipLoc-djd=1-2800-55811-0; jwotest_product=99; unpl=V2_ZzNtbUBTRBAhCxJUch5YAWJRQlwRAkMTcw0WB3sRDABkVhBaclRCFnUURlVnGVUUZwYZXUBcQxVFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseXAFmARddQFFFEXULRlV6HVUEZQsSbXJQcyVFDEZdfhhfNWYzE20AAx8XfQ9PVX5UXAJnBxNfR1dBE3MMRld7GF0BbgIQVUJnQiV2; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_3564e2e186554ca0bd1774ab19a42d36|1634537591800; __jda=122270672.16150341377512100580391.1615034138.1634264988.1634537592.35; __jdc=122270672; token=f728a66c2999b1686a24e547706241a8,2,908076; __tk=WnbLVki5WkuCiIeBTIlFWnbKikaEVAqETIVvTIaEWnY,2,908076; __jdb=122270672.3.16150341377512100580391|35.1634537592; shshshfp=060bd7a2efecdadf164b439347d1728d; shshshsID=7433a3c07372c22a82e840c13fad27ba_3_1634537626853; ip_cityCode=2802; 3AB9D23F7A4B3C9B=OOGFR7VEBOKC3KPZ6KF3FKUOPTYV2UTP6I26CTJWT6CBR7KDFT6DA7AKGYBOIC5VE3AGWVCO44IPRLJZQM5VPBDKRE; JSESSIONID=1D4710B7B692719F919CD34B4CBF23FD.s1',
        'referer': 'https://item.jd.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }

    comment_resp = requests.get(url=comment_url, params=params, headers=headers)
    comment_resp.close()
    obj1 = re.compile(r'.*?"comments":(?P<coments>.*?)[)];', re.S)
    obj2 = re.compile(r'.*?"content":"(?P<content>.*?)",".*?"score":(?P<score>.*?),"', re.S)

    file_json = 'comments.json'
    comment_str = obj1.finditer(comment_resp.text)

    for it in comment_str:
        json = it.group('coments')
        print(json)
        result = obj2.finditer(json)
        for it in result:
            #print(it.group('content'))
            dic = it.groupdict()  # 字典
            dic['content'] = dic['content'].replace('\\n', '').replace('&hellip;','') #去掉换行字符存入字典中
            csvwriter.writerow(dic.values())

        print("over!")
        time.sleep(1)
f.close()
