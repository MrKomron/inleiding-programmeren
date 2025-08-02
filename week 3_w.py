# Vraag 1
# def integer_division(deeltal, deler):
#     """
#         doe de gehele deling van deeltal door deler
#     """
#     quotient =0
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

# Vraag 2
# from math import pi
# def area_of_circle(r):
#     result=pi*(r**2)
#     return result

# Vraag 3
# from math import sqrt
# def is_priem(x):
#     if x<=1:
#         return False
#     for i in range(2,int(sqrt(x))+1):
#         if x%i==0:
#             return False
#     return True

# print(is_priem(0))
# print(is_priem(1))
# print(is_priem(2))
# print(is_priem(10))
# print(is_priem(11))
# print(is_priem(13))
# print(is_priem(19))

# Vraag 4
# from math import sqrt
# def volgend_priemgetal(x):
#     x+=1
#     while True:
#         if is_priem(x):
#             return x
#         x+=1
#
# print(volgend_priemgetal(5))   # → 7
# print(volgend_priemgetal(10))  # → 11

# Vraag 5
# from math import pi
# def degToRad(x):
#     result=x*(pi/180)
#     return result

# Vraag 6
# def priemfactoren(x):
#     lijst=[]
#     deler=2
#     while x>1:
#         if x%deler==0:
#             lijst.append(deler)
#             x=x//deler
#         else:
#             deler+=1
#     return lijst
#
# print(priemfactoren(1))     # Verwacht: []
# print(priemfactoren(2))     # Verwacht: [2]
# print(priemfactoren(3))     # Verwacht: [3]
# print(priemfactoren(4))     # Verwacht: [2, 2]
# print(priemfactoren(25))    # Verwacht: [5, 5]
# print(priemfactoren(100))   # Verwacht: [2, 2, 5, 5]
# print(priemfactoren(97))    # Verwacht: [97]  (want 97 is priem)
# print(priemfactoren(120))   # Verwacht: [2, 2, 2, 3, 5]



# Vraag 7
# def gemiddelde_lijst(lijst):
#     totaal = 0
#     for i in range(len(lijst)):
#         totaal += lijst[i]
#     gemiddelde = totaal / len(lijst)
#     return gemiddelde

# Vraag 8
# def reverse(n):
#     result=n[::-1]
#     return result
# print(reverse("happy"))

# Vraag 9
# def is_palindrome(n):
#     result=n[::-1]
#     if result!=n:
#         return False
#     return True
# print(is_palindrome("non"))
# print(is_palindrome("nob"))

# Vraag 10
# def difference(a,b):
#     lijst=[]
#     for i in a:
#         if i not in b:
#             lijst.append(i)
#     result=lijst.sort()
#     return result
# print(difference([7,2,1],[3,2]))

# def toren(hoogte):
#     s=""
#     for i in range(hoogte):
#         s=s+" "*(hoogte-i)+"="*(2*i+1)+"\n"
#     return s
# print(toren(5))
