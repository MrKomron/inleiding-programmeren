# Vraag 1
# resultaat = []
# values = [1,2]
# for i in values[1:-1]:
#     resultaat.append(i)
# print(resultaat)
from cgitb import reset

# Vraag 2
# n = int(input('lengte van Fibonacci-lijst: '))
# lijst=[1,1]
# result=0
# for i in range(2,n):
#     result=lijst[-1]+lijst[-2]
#     lijst.append(result)
# print(lijst)

# Vraag 3
# l = [2, 8, 3, 9, 4, 7,10]
# maxNumber=l[0]
# for i in l[1:]:
#     if i>maxNumber:
#         maxNumber=i
# print(maxNumber)

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
# print("+", end="")
# for j in range(dimx):
#     print("-",end="")
# print(">")

# Vraag 6
# dimx = int(input('lengte van de x-as: '))
# dimy = int(input('lengte van de y-as: '))
# a = int(input('a: '))
# print("^")
# for i in range(dimy):
#     print("|"+" "*(a-1)+"|")
# print("+", end="")
# for j in range(dimx):
#     print("-",end="")
# print(">")

# Vraag 7
# dimx = int(input('lengte van de x-as: '))
# dimy = int(input('lengte van de y-as: '))
# a = int(input('a: '))
# print("^")
# for i in range(dimy):
#     if i==a+1:
#         print("|" + "-"*dimx)
#     else:
#         print("|")
#
# print("+", end="")
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
#         print("*"+(basis-2)*" "+"*")

# Vraag 10
# zijde = int(input('zijde: '))
# for i in range(zijde+1):
#     print(i*"*")

# Vraag 11
# zijde = int(input('zijde: '))
# for i in range(1,zijde+1):
#     if i==1:
#         print("*")
#     elif i==2:
#         print("**")
#     elif i==zijde:
#         print("*"*zijde)
#     else:
#         print("*"+" "*(i-2)+"*")

# Vraag 12
# l1 = [1, 3, 6, 7, 8]
# l2 = [2, 6, 9, 9, 10]
# l=[]
# for i in l1:
#     l.append(i)
# for j in l2:
#     l.append(j)
# l.sort()
# print(l)

# Vraag 13
# l1 = [1, 3, 6, 7, 8]
# l2 = [2, 6, 9, 9, 10]
# i=0
# j=0
# l=[]
# length=len(l1)
# while i<len(l1) and j<len(l2):
#     if l1[i]<l2[j]:
#         l.append(l1[i])
#         i+=1
#     elif l2[j]<=l1[i]:
#         l.append(l2[j])
#         j+=1
# while i<len(l1):
#     l.append(l1[i])
#     i+=1
# while j<len(l2):
#     l.append(l2[j])
#     j+=1
# print(l)

# Vraag 14
# punten = [81.23, 72.44, 52.89, 64.13, 68.74]
# result=round(sum(punten)/len(punten),2)
# print(result)