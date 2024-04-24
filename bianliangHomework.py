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

source = int(input("成绩判断:"))
if source == 100:
    print("A")
elif source >= 90:
    print("B")
elif source >= 80:
    print("C")
elif source >= 70:
    print("D")
else:
    print("E")
