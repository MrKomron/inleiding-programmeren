# Vraag 1
# def splits(l):
#     mid = len(l) // 2
#     if len(l)%2==0:
#         left=l[:mid]
#         right=l[mid:]
#     else:
#         left=l[:mid]
#         right=l[mid+1:]
#     return (left, right)

# Vraag 2
# from math import sqrt
# def is_prime(n):
#     """
#     check whether n is a prime number
#     :param n: the number being tested
#     :return: True iff the number is prime
#
#     # >>> is_prime(2)
#     True
#     # >>> is_prime(4)
#     False
#     """
#     if n < 2:
#         return None
#
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#
#     return True
# print(is_prime(5))
# print(is_prime(2))
# print(is_prime(8))
# print(is_prime(29))
# print(is_prime(101))
# print(is_prime(25))
# print(is_prime(487))

# Vraag 3 / Maar wat als we niet weten s,w en h?
# def item_order(bestellingen):
#     s=bestellingen.count("s")
#     h=bestellingen.count("h")
#     w=bestellingen.count("w")
#     result=[s,h,w]
#     return result
# print(item_order(["s", "w", "h", "s", "h"]))
# print(item_order(["h", "w", "h"]))
# print(item_order(["s", "h", "w", "h", "h", "w"]))
# print(item_order(["s"]))

# Vraag 4
# def place_order(db,email,order):
#     db[email]=item_order(order)

# Vraag 5
# def print_previous_order(db,email):
#     if email not in db:
#         print("Je hebt nog geen bestellingen geplaatst.")
#         return
#
#     bestelling=db[email]
#     items=["salade","hamburger","water"]
#     for count, item in zip(bestelling,items):
#         print(f"Je bestelde {count} {item}(s).")
#
# db = {}
# print_previous_order(db,"jefke@gmail.com")
# place_order(db,"jefke@gmail.com",["s", "w", "h", "s", "h"])
# place_order(db,"mieke@gmail.com",["w", "w", "h", "s", "h"])
# print_previous_order(db,"jefke@gmail.com")
# print_previous_order(db,"mieke@gmail.com")

# Vraag 6
# def create_dice():
#     dice=[]
#     for i in range(1,14):
#         dice.append(set())
#     return dice

# Vraag 7
# def create_dice():
#     dice=[]
#     for i in range(1,14):
#         dice.append(set())
#     for a in range(1,7):
#         for b in range(1,7):
#             s=a+b
#             dice[s].add((a,b))
#     return dice

# Vraag 8
# def lose():
#     dice=create_dice()
#     return dice[2] | dice[3] | dice[12]
#
# def win():
#     dice=create_dice()
#     return dice[7] | dice[11]

# Vraag 9
# from random import randint, random
# def roll_dice():
#     left=random.randint(1,6)
#     right=random.randint(1,6)
#     return (left,right)

# Vraag 10
# def game_ends(worp):
#     total=sum(worp)
#     return total in {2,3,7,11,12}


# Vraag 11
# def minimum_elements(l):
#     if not l:
#         return None
#     counter=0
#     min_val=l[0]
#     for i in range(1,len(l)):
#         if l[i]<min_val:
#             min_val=l[i]
#             counter=1
#         elif l[i]==min_val:
#             counter+=1
#     return (min_val, counter)
#
# print(minimum_elements([3,2,4,3,1,1,3,2,1]))
# print(minimum_elements([1,3,5,4,3,1,2]))
# print(minimum_elements([5,3,6,5,7,4,2]))
# print(minimum_elements([10**7,10**6,10**6,10**6]))

# Vraag 12
# def add_matrices(m1,m2):
#     result=[]
#     for row1, row2 in zip(m1,m2):
#         if len(row1) != len(row2):
#             return None
#
#         new_row=[]
#         for val1,val2 in zip(row1,row2):
#             new_row.append(val1+val2)
#         result.append(new_row)
#     return result

# Vraag 13
# def multiply_matrices(a,b):
#     if len(a[0]) != len(b):
#         return None
#     m=len(a)
#     n=len(a[0])
#     p=len(b[0])
#     result=[[0 for _ in range(p)] for _ in range(m)]
#
#     for i in range(m):
#         for j in range(p):
#             for k in range(n):
#                 result[i][j]+=a[i][k]*b[k][j]
#     return result
