import csv

# 打开要修改格式的csv文件 data1,并读出内容到reader
with open('iQOO5_1.csv', 'r',encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for i,line in enumerate(reader):
    # 将data1的内容以utf8格式写入新的csv文件data2

        if(i > 0):

            with open('test1.csv', 'a', encoding ='utf-8-sig', newline='') as d:

                    writer = csv.writer(d)
                    print(line)
                    writer.writerow(line)
