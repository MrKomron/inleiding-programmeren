# Vraag 1
# def midden(p1,p2):
#     result=((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
#     return result

# Vraag 2
# def midden(A,B):
#     temp_result=[]
#     for a,b in zip(A,B):
#         temp_result.append((a+b)/2)
#     return tuple(temp_result)

# Vraag 3
# def tel_getallen(l):
#     max_getal = max(l)
#     frequenties = [0] * (max_getal + 1)  # Maak lijst van nullen
#     for getal in l:
#         frequenties[getal] += 1  # Verhoog de teller op de juiste plek
#     return frequenties
#
# l = [1, 2, 5, 3, 2, 17, 5, 6, 7, 3, 2, 1, 9, 3]
# frequenties = tel_getallen(l)
# print(frequenties)

# Vraag 4
# from alice_book import book
# def tel_woorden(l):
#     result={}
#     teller=0
#     for i in l:
#         if i not in result:
#             result[i]=1
#         else:
#             result[i]+=1
#
#     return result
#
# woorden = book.split()
# print(tel_woorden(woorden))

# Vraag 5
# def print_frequenties(dict):
#     for woord,aantal in dict.items():
#         print(woord, aantal)

# Vraag 6
def list2dict(l1,l2):
    result={}
    for key,value in zip(l1,l2):
        if len(l1)==len(l2):
            result[key]=value
        else:
            return None
    return result

print(list2dict(['Ten', 'Twenty', 'Thirty'],[10, 20, 30]))
print(list2dict(['Ten', 'Twenty', 'Thirty'],[10, 20]))
print(list2dict(['Ten', 'Ten', 'Thirty'],[10, 20]))
print(list2dict([1,2,3,4],[5,6,7,8]))

# Vraag 7
# def bepaal_winnaar(data):
#     counter=None
#     winnaar=None
#     for key, value in data.items():
#         som=sum(value)
#         if counter is None or som<counter:
#             counter=som
#             winnaar=key
#     return winnaar
#
# punten = { "Calders": [2, 4, 3, 2, 3, 4, 4, 4, 3, 3], # Som is 32
#            "Hofkens": [3, 3, 2, 4, 2, 4, 3, 3, 4, 3], # Som is 31
#            "Laenens": [2, 3, 4, 2, 3, 4, 4, 3, 4, 3], # Som is 32
#            "Symens": [2, 3, 2, 4, 2, 2, 3, 2, 2, 4] }# Som is 26 }
# print(bepaal_winnaar(punten))

# Vraag 8
# def tel_elementen(l):
#     return len(set(l))


# Vraag 9
# def is_priem(getal):
#     if getal < 2:
#         return False
#     for i in range(2, int(getal**0.5)+1):
#         if getal % i == 0:
#             return False
#     return True
#
# def volgend_priemgetal(getal):
#     volgende = getal + 1
#     while not is_priem(volgende):
#         volgende += 1
#     return volgende
#
#
# def priemgetallen(n):
#     start=2
#     result=[]
#     while len(result)<n:
#         if is_priem(start):
#             result.append(start)
#         start+=1
#     return result

# Vraag 10
# def fibonacci(n):
#     result=[1,1]
#     new_item=0
#     while len(result)<n:
#         new_item=result[-1]+result[-2]
#         result.append(new_item)
#     return result
# print(fibonacci(6))

# Vraag 11
# def priem_en_fib(n):
#     return set(priemgetallen(n)) & set(fibonacci(n))

# Vraag 12
# def priem_of_fib(n):
#     return set(priemgetallen(n)) | set(fibonacci(n))

# Vraag 13
# def priem_xof_fib(n):
#     return set(priemgetallen(n)) ^ set(fibonacci(n))

# Vraag 14
# Function to add a new task
# def add_task(tasks, task):
#     tasks.append(task)
#
# # Function to update a task's status
# def update_task(tasks, task, status):
#     for t in tasks:
#         if t['name'] == task:
#             t['status'] = status
#
# # Function to print all pending tasks
# def print_pending_tasks(tasks):
#     pending_tasks = []
#     for task in tasks:
#         if task['status'] == 'pending':
#             print(task['name'])
#
# # Function to check if a task is complete
# def is_task_complete(tasks, task):
#     for t in tasks:
#         if t['name'] == task:
#             return t['status'] == 'complete'
#     return None
#
# tasks = []
# # Adding tasks
# add_task(tasks, {'name': 'Task 1', 'status': 'pending'})
# add_task(tasks, {'name': 'Task 2', 'status': 'complete'})
# add_task(tasks, {'name': 'Task 3', 'status': 'pending'})
#
# print_pending_tasks(tasks)
#
# update_task(tasks, 'Task 1', 'complete')
#
# print_pending_tasks(tasks)
#
# print("Is Task 1 complete?", is_task_complete(tasks, 'Task 1'))
# print("Is Task 3 complete?", is_task_complete(tasks, 'Task 3'))
# print("Is Task 4 complete?", is_task_complete(tasks, 'Task 4'))