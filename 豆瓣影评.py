# -*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import time
import jieba
import wordcloud

def getHtml(url):
    """获取url页面"""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    ]

    headers = {
        #'Cookie': 你的cookie,
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        'Referer': 'https: // movie.douban.com / subject / 26752088 / comments?status = P',
        'Connection': 'keep-alive'
    }
    req = urllib.request.Request(url,headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')

    return content


def getComment(url):
    """解析HTML页面"""
    html = getHtml(url)
    soupComment = BeautifulSoup(html, 'html.parser')

    comments = soupComment.findAll('span', 'short')
    onePageComments = []
    for comment in comments:
        # print(comment.getText()+'\n')
        onePageComments.append(comment.getText()+'\n')

    return onePageComments

def wordAnalysis():
    f = open('C:/Users/Administrator/PycharmProjects/practice1/我不是药神.txt','r',encoding = 'utf-8')
    content = f.read()
    f.close()
    ls = jieba.lcut(content)
    txt = ' '.join(ls)
    w = wordcloud.WordCloud(font_path='c:\windows\Fonts\STZHONGS.TTF', width=1000, height=700, background_color='white')
    w.generate(txt)
    w.to_file('Movie.png')



if __name__ == '__main__':
    f = open('我不是药神.txt', 'a', encoding='utf-8')
    j = 0
    for page in range(30):  # 豆瓣爬取多页评论需要验证。
        url = 'https://movie.douban.com/subject/26752088/comments?start=' + str(20*page) + '&limit=20&sort=new_score&status=P'
        print('第%s页的评论:' % (page))
        print(url + '\n')

        for i in getComment(url):
            f.write(str(j))
            f.write(i)
            print(j,i)
            j += 1
        time.sleep(10)
        print('\n')
    wordAnalysis()
