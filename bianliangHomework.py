import datetime
import time

print("\\n")  # \n
print("\\t")  # \t
print("\\r")  # \r
print("\\""\\")  # \\

name = "chai"
age = 23
num = 100
xb = True
ah = "football"
print("""nihao""")
if xb:
    print("姓名", "age", "成绩", "性别", "爱好\n" + f"{name} {age} {num} ""man"" {ah}")

    print(-10 % 3)

days = 97
weeks = days // 7
day = days % 7
print(weeks, day)
print("这是第%f,这也是第%f" % (day, days))

print(10 and 20)
# total_friends = int(input("请输入顾客人数："))

a1 = 30
a2 = 40
a1, a2 = a2, a1
print(f"a1={a1}, a2={a2}")

a3 = 10
a4 = 20
a5 = 15
print(a3 if a3 > a4 else a4 if a5 < a4 else a5)

"""a6 = int(input("qignhsuru:"))
a7 = 1
if a6 + a7 >= 50:
    print("hello~~")
else:
    print("noHello")"""

a8 = 1
a9 = 7
if (a8 + a9) % 3 == 0 & (a8 + a9) % 5 == 0:
    print("ok")
else:
    print("no")

"""a10 = int(input("闰年判断:"))
if (a10 % 4 == 0 and a10 % 100 != 0) or a10 % 400 == 0:
    print("闰年")
else:
    print("不是闰年")"""

"""source = int(input("成绩判断:"))
if source == 100:
    print("A")
elif source >= 90:
    print("B")
elif source >= 80:
    print("C")
elif source >= 70:
    print("D")
else:
    print("E")"""

"""sex = input("性别判断:")
num = float(input("成绩判断:"))
if num >= 8.0:
    print("合格")
    if sex == "man":
        print("分到男子组")
    else:
        print("分到女子组")
else:
    print("成绩不合格")"""

"""age = int(input("年龄判断:"))
month = int(input("月份判断:"))
if 4 <= month <= 10:
    if 18 <= age <= 60:
        print("60$")
    elif age < 18:
        print("30$")
    else:   
        print("20$")
else:
    # 成人和儿童
    if 18 <= age:
        print("40$")
    else:
        print("20$")"""

num = range(1, 101)
i = 0
while i < len(num):
    if num[i] % 3 == 0:
        print(num[i])
    i += 1
print("上段代码结束")

num = range(40, 201, 2)
i = 0
while i < len(num):
    print(num[i])
    i += 1

# name = input("请输入姓名:")
# while name != "exit":
#     name = input("请继续输入姓名:")
#     print(f"姓名是{name}")


# 输出1-100中能被9整除的个数和下标
num = range(1, 101)
i = 0
n = 0
index = 0
while i < len(num):
    if num[i] % 9 == 0:
        n += 1
        index = i
    i += 1
print(n, index)

# print("kaish")
# number = int(input())
# i = 1
# while i <= number:
#     if number % i == 0:
#         print(i)
#     i += 1


"""
先写一个直角三角形
"""
line = 5
for i in range(line + 1):
    for j in range(i):
        print("*", end="")
    print()

"""
再写一个正三角形
其中我用k来代替空格，方便数空格
"""

for i in range(line + 1):
    for k in range(line - i):
        print("k", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

"""
再把中间的空格给去掉，优化第一行是空行
tips：为什么第一行是空行呢？因为range（）的起始值是0，所以第一行是空行
"""
line = 5
for i in range(line + 1):
    for k in range(line - i):
        print("k", end="")
    for j in range(2 * i + 1):  # j是*号的位置
        if j == 0 or i == line or j == 2 * i:
            print("*", end="")
        else:
            print("k", end="")
    print()

# for i in range(6):  # 循环6次打印6行
#     for j in range(5 - i):  # 打印空格每次循环递减
#         print('k', end='')
#     for q in range(2 * i + 1):  # 打印星星
#         if q == 0 or i == 5 or q == 2 * i:  # 判断打印星星位置，在开头，结尾和最后一行打印星星
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()  # 每行循环结束后换行

#  要求！！！
# 统计3个班成绩情况,每个班有5名同学，
# 求出各个班的平均分和所有班级的平均分，学生的成绩从键盘输入
# 统计三个班及格人数
# num_avg_score = 0
# num_score = 0
# avg_score = 0
# people = 0
# for i in range(3):
#     for j in range(3):
#         score = float(input("请输入成绩:"))
#         num_score = num_score + score
#         if score >= 60:
#             people += 1
#     print(f"第{i + 1}班的平均分是{num_score / 3}")
#     num_avg_score += num_score
#     num_score = 0
# print(f"所有班级的平均分是{num_avg_score / 3}")
# print(f"及格人数是{people}")

# 九九乘法表
a = 1
b = 1
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}*{j}={i * j}\t", end="")
    print()

current_timestamp_float = time.time()
current_timestamp_int = int(current_timestamp_float)
print(f"原始时间戳（浮点数）: {current_timestamp_float}")


# 编写一个递归函数来计算一个数的阶乘（n! = n * (n-1) * ... * 1）。
def digui1(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * digui1(n - 1)


# test
print(digui1(0))

start_time = time.perf_counter()


# 实现一个递归函数，计算斐波那契数列中的第n项（F(n) = F(n-1) + F(n-2)，F(0)=0, F(1)=1
def digui2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return digui2(n - 1) + digui2(n - 2)


end_time = time.perf_counter()
print(digui2(1))
print(end_time - start_time)
import sys
print(sys.version)
import pandas as pd
print(pd.__version__)
# '1.2.1'