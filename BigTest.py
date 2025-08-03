# Vraag 1
# def integer_division(deeltal, deler):
#     """
#         doe de gehele deling van deeltal door deler
#     """
#     quotient = 0
#     while deeltal >= deler:
#         quotient += 1
#         deeltal -= deler
#
#     return quotient
#
# print(integer_division(7, 3))
# print(integer_division(123, 5))
# print(integer_division(0, 7))
# print(integer_division(7, 7))
# print(integer_division(15, 7))
import math
# Vraag 2
# from math import pi
# def area_of_circle(r):
#     area=pi*r**2
#     return area


# Vraag 3
# def is_priem(x):
#     if x<2:
#         return False
#     for i in range(2,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# print(is_priem(5))

# Vraag 4
# def volgend_priemgetal(x):
#     x+=1
#     while not is_priem(x):
#         x+=1
#     return x


# Vraag 5
# from math import pi
# def degToRad(n):
#     result=n*(pi/180)
#     return result

# Vraag 6
# def priemfactoren(x):
#     l=[]
#     deler=2
#     while x>1:
#         if x%deler==0:
#             l.append(deler)
#             x//=deler
#         elif x%deler!=0:
#             deler+=1
#     return l



# Vraag 7
# def gemiddelde_lijst(lijst):
#     if len(lijst)==0:
#         return None
#     totaal = 0
#     for i in lijst:
#         print(i)
#         totaal += i
#
#     gemiddelde = totaal / len(lijst)
#     return gemiddelde
#
# print(gemiddelde_lijst([1,2,3,4]))
# print(gemiddelde_lijst([3,2,3,4]))
# print(gemiddelde_lijst([]))

# Vraag 8
# def reverse(n):
#     result=n[::-1]
#     return result
#
# print(reverse("happy"))

# Vraag 9
# def is_palindrome(n):
#     result=n[::-1]
#     if n==result:
#         return True
#     return False
#
# print(is_palindrome("happy"))
# print(is_palindrome("non"))

# Vraag 10
# def difference(l1,l2):
#     l=[]
#     for i in l1:
#         if i not in l2:
#             l.append(i)
#     return l
#
# print(difference([7,2,1] , [3,2]))