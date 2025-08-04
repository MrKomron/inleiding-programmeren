# Vraag 1
# def hms(n):
#     uur=n//3600
#     rest=n%3600
#     minuten=rest//60
#     seconden=rest%60
#     l=[uur,minuten,seconden]
#     return l

# Vraag 2
# def tijdNaarSeconden(uur,minuten,seconden):
#     result=seconden+(minuten*60)+(uur*3600)
#     return result
# print(tijdNaarSeconden(1,0,1))
# print(tijdNaarSeconden(0,1,40))

# Vraag 3
def faculteit(n):
    result=1
    for i in range(1,n+1):
        result*=i
    return result
# print(faculteit(5))

# Vraag 4
# def variatie(n,k):
#     result=int(faculteit(n)/faculteit((n-k)))
#
#     return result
# print(variatie(4,1))
# print(variatie(5,2))
# print(variatie(6,3))

# Vraag 5
# def combinatie(n,k):
#     result=int(faculteit(n)/(faculteit(k)*faculteit(n-k)))
#     return result
# print(combinatie(4, 1))
# print(combinatie(5, 2))
# print(combinatie(6, 3))

# Vraag 6
# def remove_multiples(l,n):
#     for i in l[:]:
#         if i%n==0:
#             l.remove(i)

# Vraag 7
# def remove_multiples(l,n):
#     nieuw_list=[]
#     for i in l:
#         if i%n!=0:
#             nieuw_list.append(i)
#     return nieuw_list
# print(remove_multiples([1,2,3,4,5,6],5))

# Vraag 8
# def even(n):
#     if n%2==0:
#         return True
#     return False

# Vraag 9
def piramide(n):
    result=""
    for i in range(1,n+1):
        prefix=" "*(n-i)
        numbers =" ".join(str(x) for x in range(1,2*i))
        result+=prefix+numbers+"\n"
    print()
    return result.rstrip()
print(piramide(4))
print()
print(piramide(5))

def piramide(n):
    for i in range(n):
        print(" "*(n-i-1),end="")
        for j in range(2*i+1):
            print(j+1,end=" ")
        print()

# Vraag 10
# def som_veelvouden(n):
#     result=0
#     for i in range(1,n):
#         if i%3==0 or i%5==0:
#             result+=i
#     return result
#
# print(som_veelvouden(9))

# Vraag 11
# def som_veelvouden(getal1, getal2, bovengrens):
#     result=0
#     for i in range(1,bovengrens):
#         if i%getal1==0 or i%getal2==0:
#             result+=i
#     return result

