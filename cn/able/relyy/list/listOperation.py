bicycles = ['1', '2', '3', '4', '5']
print(bicycles)
#新增元素
#末尾新增
bicycles.append('6')
print(bicycles)
#指定位置新增
bicycles.insert(3, '4')
print(bicycles)

#删除元素
del bicycles[3] #无返回值
print(bicycles)
#有返回值,移除第一个
var = bicycles.remove('4')
print(bicycles)

#更改元素
bicycles[4] = '7'
print(bicycles)

#排序
bicycles.sort() #改变本身的顺序
print(bicycles)
#倒序
bicycles.sort(reverse=True)
print(bicycles)
print(sorted(bicycles)) #临时排序

#反转
bicycles.reverse()

#长度
llen = len(bicycles)

for i in bicycles:
    print(i)

for i in range(1, 5):
    print(i)

#range(x,y) 包含x，不包含y
number_list = list(range(1,10))

max(bicycles)
min(bicycles)
sum(bicycles)

squares = [value ** 2 for value in range(1,11)]


##  切片：列表的任何子集
## 取列表中0，1，2位置元素作为切片
print(squares[0:3])

#复制列表
copyList = squares[:]
# 这样复制行不通
copyList = squares





