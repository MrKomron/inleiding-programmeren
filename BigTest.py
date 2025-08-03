# Vraag 1
# l = [2, 8, 3, 4, 7, 9]
# resultaat = []
# for i in l[1:-1]:
#     resultaat.append(i)
# print(resultaat)

# Vraag 2
# n = int(input('lengte van Fibonacci-lijst: '))
# resultaat=[1,1]
# temp=0
# for i in range(2,n):
#     temp=resultaat[-1]+resultaat[-2]
#     resultaat.append(temp)
# print(resultaat)

# Vraag 3
# l = [2, 8, 3, 9, 4, 7]
# max_num=l[0]
# for i in l[1:]:
#     if i>max_num:
#         max_num=i
# print(max_num)

# Vraag 4
# l1 = [100, 20, 13, 7, 8]
# l2 = [7, 2, 3, 1, 20]
# doorsnede = []
# for i in l1:
#     if i in l2:
#         doorsnede.append(i)
# doorsnede.sort()
# print(doorsnede)

# Vraag 5
# dimx = int(input('lengte van de x-as: '))
# dimy = int(input('lengte van de y-as: '))
# print("^")
# for i in range(dimy):
#     print("|")
# print("+",end="")
# for j in range(dimx):
#     print("-",end="")
# print(">")

# Vraag 6
# dimx = int(input('lengte van de x-as: '))
# dimy = int(input('lengte van de y-as: '))
# a = int(input('a: '))
# print("^")
# for i in range(dimy):
#     print("|"+" "*a+"|")
# print("+",end="")
# for j in range(dimx):
#     print("-",end="")
# print(">")

# Vraag 7
# dimx = int(input('lengte van de x-as: '))
# dimy = int(input('lengte van de y-as: '))
# b = int(input('b: '))
# print("^")
# for i in range(dimy):
#     if i==dimy-b-1:
#         print("|" + "-" * dimx)
#     else:
#         print("|")
# print("+",end="")
# for j in range(dimx):
#     print("-",end="")
# print(">")

# Vraag 8
# basis = int(input('basis: '))
# hoogte = int(input('hoogte: '))
# for i in range(hoogte):
#     print(basis*"*")

# Vraag 9
# basis = int(input('basis: '))
# hoogte = int(input('hoogte: '))
# for i in range(hoogte):
#     if i==0 or i==hoogte-1:
#         print(basis*"*")
#     else:
#         print("*"+" "*(basis-2)+"*")

# Vraag 10
# zijde = int(input('zijde: '))
# for i in range(1,zijde+1):
#     print(i*"*")

# Vraag 11
# zijde = int(input('zijde: '))
# for i in range(zijde):
#     if i==0:
#         print("*")
#     elif i==1:
#         print("**")
#     elif i==zijde-1:
#         print("*"*zijde)
#     else:
#         print("*"+" "*(i-1)+"*")

# Vraag 12
# l1 = [1, 3, 6, 7, 8]
# l2 = [2, 6, 9, 9, 10]
# l = []
# for i in l1:
#     l.append(i)
# for j in l2:
#     l.append(j)
# l.sort()
# print(l)

# Vraag 13 - NU NU NU
# l1 = [1, 3, 6, 7, 8]
# l2 = [2, 6, 9, 9, 10]
# l=[]
# i=0
# j=0
#
# while i<len(l1) and j<len(l2):
#     if l1[i]<=l2[j]:
#         l.append(l1[i])
#         i+=1
#     else:
#         l.append(l2[j])
#         j+=1
# while i<len(l1):
#     l.append(l1[i])
#     i+=1
# while j<len(l2):
#     l.append(l2[j])
#     j+=1
#
# print(l)


# Vraag 14
# punten = [81.23, 72.44, 52.89, 64.13, 68.74]
# result=round((sum(punten)/len(punten)),2)
# print(result)
