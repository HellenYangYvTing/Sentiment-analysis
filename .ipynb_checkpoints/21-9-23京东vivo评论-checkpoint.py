import requests
import csv
import re
import time

comment_url = 'https://club.jd.com/comment/productPageComments.action'

f = open("JDcontents_vivo.csv", mode="a", encoding="utf-8", newline='')
csvwriter = csv.writer(f)
row = ('评论', '评分')
csvwriter.writerow(row)

for i in range(200):
    print(i)
    page = i
    params = {
        'productId': 100010624227,  # 商品id，先写死
        'score': 3,
        'sortType': 6,
        'page': page,
        'pageSize': 10,
        'callback': 'fetchJSON_comment98',
        'isShadowSku': 0,
        'fold': 1
    }

    headers = {
        'cookie':'shshshfpa=980322f4-0d72-08ea-9cb2-4fcadde80a00-1562576627; shshshfpb=ymAFpsvPn5OjLe2TxXJVyZQ==; __jdu=16150341377512100580391; mt_xid=V2_52007VwMVUllZUF8fSx9aAWcAElNcXFtbHUEZbAYwVhdbDVkCRh9AEFsZYgdBBkEIVw1IVUlbA24KQVEPXFcIGnkaXQZnHxNaQVhbSx5AElgAbAITYl9oUWocSB9UAGIzEVVdXg==; unpl=V2_ZzNtbUBVREUmC0QBfkkMDGJRQlwSV0ATIQFGUnIZCwBnABRYclRCFnUUR1xnGl4UZwYZXEtcQRBFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHseXAFmARddQFFFEXULRlV6HVUEZQsSbXJQcyVFDENceRhbNWYzE20AAx8TcwpBVX9UXAJnBxNfR1dBE3MMRld7GF0BbgIQVUJnQiV2; PCSYCityID=CN_110000_110100_110108; user-key=0245721f-bdeb-4f17-9fd2-b5e647ad7f3e; jwotest_product=99; __jdc=122270672; mba_muid=16150341377512100580391; wlfstk_smdl=ey5hfakeb6smwvr1ld305bkzf79ajgrx; areaId=1; ipLoc-djd=1-2800-55811-0; __jdv=122270672|baidu|-|organic|not set|1632740808675; token=48ce2d01d299337c932ec85a1154c65f,2,907080; __tk=vS2xv3k1ush1u3kxvSloXsa0YznovSTFXUawXSawushwXpJyupq0vG,2,907080; shshshfp=3da682e079013c4b17a9db085fb01ea3; shshshsID=2ee3081dbf26e0d2b12dfe9ebf1ac9a8_1_1632744359396; __jda=122270672.16150341377512100580391.1615034138.1632740809.1632744359.28; __jdb=122270672.1.16150341377512100580391|28.1632744359; 3AB9D23F7A4B3C9B=OOGFR7VEBOKC3KPZ6KF3FKUOPTYV2UTP6I26CTJWT6CBR7KDFT6DA7AKGYBOIC5VE3AGWVCO44IPRLJZQM5VPBDKRE; JSESSIONID=82C0F348483686AC9A673E31126675D3.s1',
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
        time.sleep(5)
f.close()
