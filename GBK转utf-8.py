import csv

# 打开要修改格式的csv文件 data1,并读出内容到reader
with open('评论汇总.csv', 'r', encoding ='GBK') as f:
    reader = csv.reader(f)
    for line in reader:
    # 将data1的内容以utf8格式写入新的csv文件data2
        with open('评论汇总-utf.csv', 'a', encoding ='utf-8-sig', newline='') as d:
            writer = csv.writer(d)
            writer.writerow(line)
