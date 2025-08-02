# Vraag 1
# def hms(n):
#     uren=(n//3600)
#     rest=(n%3600)
#     minuten=(rest//60)
#     seconden=(rest%60)
#     lijst=[uren,minuten,seconden]
#     return lijst
#
# print(hms(3601))
# print(hms(100))
from cgitb import reset


# Vraag 2
# def tijdNaarSeconden(uren,min,sec):
#     result=sec+(min*60)+(uren*3600)
#     return result
#
# print(tijdNaarSeconden(1,0,1))
# print(tijdNaarSeconden(0,1,40))

# Vraag 3
# def faculteit(n):
#     result=1
#     for i in range(n,0,-1):
#         # print(i)
#         result*=i
#     return result
# print(faculteit(5))

# Vraag 4
# def variatie(n,k):
#     result=faculteit(n)//faculteit((n-k))
#     return result
# print(variatie(5, 2))


# Vraag 5
# def combinatie(n,k):
#     result=faculteit(n)//(faculteit(k)*(faculteit(n-k)))
#     return result
# print(combinatie(5, 2))


# Vraag 6
# def remove_multiples(l,n):
#     for i in l[:]:
#         if i%n==0:
#             l.remove(i)
#     return l
# lijst1 = [1, 2, 3, 4, 5, 6, 10]
# remove_multiples(lijst1, 2)
# print(lijst1)  # Verwacht: [1, 3, 5]

# Vraag 7
# def remove_multiples(l,n):
#     lijst=[]
#     for i in l:
#         if i%n!=0:
#             lijst.append(i)
#     return lijst
# print(remove_multiples([3,5,2,6,8,9],2))
# print(remove_multiples([3,5,2,6,8,9,5,6],3))

# Vraag 8
# def even(x):
#     if x%2==0:
#         return True
#     return False
#
# print(even(20))
# print(even(23))

# Vraag 9
def pyramide(n):
    start=1
    result=""
    for i in range(start,n+1):
        spaties=" "*(n-i)
        getallen=" "
        for j in range(1,2*i):
            getallen+=str(j)+" "
        result+=spaties+getallen.rstrip()+"\n"
    return result

print(pyramide(5))

# Vraag 10
# def som_veelvouden(n):
#     counter=0
#     for i in range(1,n+1):
#         if i%3==0 or i%5==0:
#             counter+=i
#     return counter
# print(som_veelvouden(10))

# Vraag 11
# def som_veelvouden(getal1, getal2, bovengrens):
#     counter=0
#     for i in range(1,bovengrens):
#         if i%getal1==0 or i%getal2==0:
#             counter+=i
#     return counter
# # Test 1
# print(som_veelvouden(3, 5, 10))   # Verwacht: 3 + 5 + 6 + 9 = 23
#
# # Test 2
# print(som_veelvouden(2, 4, 15))   # Verwacht: som van 2, 4, 6, 8, 10, 12, 14 = 56
#
# # Test 3
# print(som_veelvouden(7, 11, 50))  # Verwacht: som van 7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49 = 316
#
# # Test 4
# print(som_veelvouden(3, 3, 10))   # Verwacht: veelvouden van 3 < 10 → 3, 6, 9 =_

def count(w):
    c=[0]*7
    for x in w:
        c[x]=c[x]+1
    return c

def count(w):
    c=[0]*6
    for x in w:
        c[x-1]=c[x-1]+1
    return c