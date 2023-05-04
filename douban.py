#将提取目标字段的功能封装成函数
#参考
#author  yyt
#参考链接：1.https://blog.csdn.net/moujinzhuo/article/details/103389218
#data    2021/9/18/16:19
import re
import requests
import re
import time
import pymongo
import random

def re_select(string):
    # 取出作者字段
    pat_author = r'class="name">(.*?)</a>'
    re_au = re.compile(pat_author, re.S)
    auList = re_au.findall(string)#获取目标文档中的所有符合条件的字段
    # 取出评价等级字段
    pat_level = r'main-title-rating" title="(.*?)"></span>'
    re_level = re.compile(pat_level, re.S)
    levelList = re_level.findall(string)
    # 取出影评内容
    pat_story = r'<div class="short-content">(.*?) &nbsp;'
    re_story = re.compile(pat_story, re.S)
    storyList = re_story.findall(string)
    for i in range(len(storyList)):#将获取的字段进行格式调整
        storyList[i] = storyList[i].strip()#去掉字段中的空白字符
        storyList[i] = re.sub(r"[a-z\s\"\<\>\/\=\-]", "", storyList[i])#删除多余的字符
    # 取出评价时间
    pat_time = r'class="main-meta">(.*?)</span>'
    re_time = re.compile(pat_time, re.S)
    timeList = re_time.findall(string)
    #返回所有的目标字段列表
    return auList,levelList,storyList,timeList

url = r'https://movie.douban.com/subject/26266893/reviews?start='
#定义一个内核列表
u_a = [ 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0']

def re_select(string):
    # 取出作者字段
    pat_author = r'class="name">(.*?)</a>'
    re_au = re.compile(pat_author, re.S)
    auList = re_au.findall(string)
    # 取出评价等级字段
    pat_level = r'main-title-rating" title="(.*?)"></span>'
    re_level = re.compile(pat_level, re.S)
    levelList = re_level.findall(string)
    # 取出影评内容
    pat_story = r'<div class="short-content">(.*?) &nbsp;'
    re_story = re.compile(pat_story, re.S)
    storyList = re_story.findall(string)
    for i in range(len(storyList)):
        storyList[i] = storyList[i].strip()
        storyList[i] = re.sub(r"[a-z\s\"\<\>\/\=\-]", "", storyList[i])
    # 取出评价时间
    pat_time = r'class="main-meta">(.*?)</span>'
    re_time = re.compile(pat_time, re.S)
    timeList = re_time.findall(string)
    return auList,levelList,storyList,timeList

page=0
k = 0
while page<1073:
    urls = url+str(k)
    user = random.randint(0, 2)
    header = {'User-Agent': u_a[user]}
    response = requests.get(urls, headers=header)
    page = page + 1
    #防止短时间内请求次数过多被网站封IP，所有爬一个页面后休息5秒，爬100个后休息一分钟
    if page % 100 == 0:
        time.sleep(60)
    else:
        time.sleep(5)
    k = k + 20
    if response.status_code == 200:
        print("成功爬取评论第%d页......" % page)
        auList, levelList, storyList, timeList = re_select(response.text)
        length = len(auList)
        #如果提取的页面信息有缺失，则不要当前页面的信息，直接跳转到下一页面继续爬取
        if(len(levelList)!=length or len(levelList)!=length or len(timeList)!=length):
            continue
        for i in range(len(auList)):
            di = {'作者': auList[i], '评级': levelList[i], '评论': storyList[i], '评论时间': timeList[i]}
            #collection.insert(di)
    else:
        print("爬取失败.......")


