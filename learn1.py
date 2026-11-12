# # i=0
# # while i<10:
# #     print(i)
# #     i+=1
# #     if i==5:
# #         break
# # else:
# #     print("循环正常结束")
#
# # i,sum=2,0
# # while i<=100:
# #     sum+=i
# #     i+=2
# # print(sum)
#
# for i in range(1,11):
#     day = int(input("今天星期几:"))
#     match day:
#         case 1:
#             print(f"工作会议{day}")
#         case 2:
#             print("学习培训")
#         case 3:
#             print("项目开发")
#         case 4:
#             print("代码审查")
#         case 5 if True:
#             print("总结规划")
#         case 6|7:
#             print("休息放松")
#         case _:
#             print("输入错误")

# msg = "hello 我是中国人"
# for i in msg:
#     print(i,end="")
# else:
#     print("\n循环结束")
# sum=0
# for i in range(1,101,2):
#     sum+=i
# print(f"{sum}")
# sum=0
# for i in range(100,501):
#     if i%3==0:
#         sum+=i
# print(sum)
# i=int(input("长"))
# j=int(input("宽"))
# for n in range(1,i+1):
#     for m in range(1,j+1):
#         print("* ",end="")
#     print("\n")

# for i in range(1,10):
#     for j in range(1,10):
#         print(f"{j}*{i}={i*j}",end=" ")
#         if j==i:
#             break
#     print("\n")
#
# from random import *
# num=randint(1,100)
# while True:
#     i=int(input("你猜是多少？"))
#     if i==num:
#         print("这都给你猜出来了")
#         break
#     elif i<num:
#         print("猜小了")
#         continue
#     else:
#         print("猜大了")
# print("游戏结束")
#

# =[1,2,3,4,5,6,7,8,9]
# del list[2]
# print(list)

# print(range(1,10))
# print(a[:-2:],a)
#a.append(10086)
#a.insert(4,4.5)
#a.append(1)
##a.remove(1)
# a.pop(-2)
# a.reverse()
# a.sort()
# print(a)
# a=[]
# sum=0
# for i in range(0,10):
#     num=int(input(f"输入第{i+1}个数字"))
#     a.append(num)
#     sum+=num
# a.sort()
# print(f"最小值{a[0]},最大值{a[-1]},平均值{sum/10}")
# print(a)
# e=0
# a1=[19,23,54,64,875,20,109,232,123,54]
# a2=[55,80,72,35,60,123,54,29,91]
# for j in range(0,8):
#     for i in range(0,9):
#         if a2[j]==a1[i]:
#             a2.pop(j)
# while e<len(a2):
#     a1.append(a2[e])
#     e+=1
# print(a1)


# for num in a2:
#     if num in a1:
#         continue
#     a1.append(num)
# print(a1)

# for num in a2:
#     a1.append(num)
# print(a1)
# new=[]
# for num in a1:
#     if num not in new:
#         new.append(num)

# num=[*a1,*a2]
# print(num)
# a=[i**2 for i in range(1,21)]
#
# # for i in range(1,21):
# #      a.append(i**2)
# b=[19,23,54,64,87,20,109,232,123,43,26,55,72]
# # for num in b:
# #     if num%2==0:
# #         c.append(num)
# c=[i**2 for i in b if i%2==0]
# print(a,c)
#
# a="       python kkk ]"
# # print(a.upper().lower(),a)
# print(a.split("k"))
# print(a.strip())
# print(a.replace("y","eee"))
# print(a.endswith("]"))

# # a=input('输入邮箱')
# if a.count('@')==1 and "." in a:
#     print("ok")

# a=input(">")
# if a[::-1]==a:
#     print('是回文数')
# else:
#     print('啥也不是')

