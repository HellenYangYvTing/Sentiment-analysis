
import csv

# 打开要修改格式的csv文件 data1,并读出内容到reader

d = open('test1.csv', 'w', encoding ='utf-8-sig', newline='')
fildnamea = ['评论', '评分']
#csvwriter = csv.writer(d)
csvwriter = csv.DictWriter(d,fieldnames=('评论', '评分'))
row = ['perfect', '5']
csvwriter.writerow({'评论':'dsadd','评分':2})


