# recursion program
# def sol(l):
#     b=[]
#     for i in l:
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
#     return b

# v=[1,2,3,4,[2,3,4,5,5,[2,3,4,5,6,[6,7,4,3,7,[4,5,6,7,8,[3,4,5,7,8]]]]],4,67,54,67,32,45]
# d=sol(v)
# print(d)

# v=[1,2,3,4,[2,3,4,5,5,[2,3,4,5,6,[6,7,4,3,7,[4,5,6,7,8,[3,4,5,7,8]]]]],4,67,54,67,32,45]
# def sol(l):
#     b=[]
#     for i in l:
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
#     return b
# y=sol(v)
# print(y)


            
# remove unnecessay list tuples set from the list
# b=[2,[3,4,5],4,{4,5,6,7},3,4,5,"rjgjt",[]]
# a=0
# while True:
#     x=True
#     for i in b:
#         if isinstance(i,list):
#             x=False
#         elif isinstance(i,set):
#             x=False
#     if x:
#         break
#     if isinstance(b[a],list):
#         b.remove(b[a])
#         continue
#     elif isinstance(b[a],set):
#         b.remove(b[a])
#         continue
#     a=a+1
# print(b)



# def func(sol):
#     b=0
#     for i in sol:
#         if isinstance(i,list):
#             b=b+func(i)
#         else:
#             b=b+i
#     return b
# sol=[1,2,3,4,[5,6,7,8,9,[5,6,3,2,4,[44,55,66,77]]]]
# print(func(sol))
        
# class Employee:

#     def __init__(self, name, age,salary):


#         self.name = name
#         self.age = age
#         self.salary = 20000
# E1 = Employee("XYZ", 23, 20000)
# # E1 is the instance of class Employee.
# #__init__ allocates memory for E1. 
# print(E1.name)
# print(E1.age)
# print(E1.salary)









    





