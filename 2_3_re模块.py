import re
lst1 = re.findall("\d+","我的电话号：2131231,第二个号：987978")
print(lst1)


lst2 = re.search(r"\d+","我的电话号：23232,第二个号：879897")
print(lst2.group())

#预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号：23232,第二个号：9789799")
print(ret)
for it in ret:
    print(it.group())

ret2 = obj.findall("这是：23123，第二个：7732299392")
print(ret2)