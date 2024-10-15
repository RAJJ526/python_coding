# def my_function(function):
#     print(function+ " dalo")
# my_function("email")
# my_function("password")
# my_function("captcha")

# def my_number(number):
#     print(number+12)
# my_number(13)
# my_number(14)
# my_number(15)

# # function intro

# def add(a,b,c):
#     print(a+b+c)
# add(2,3,5)
# add(23,33,5)
# add(32,33,5)
# add(42,34,5)
# add(24,43,9)

# # function without param

# def add():
#     a  =input("i")
#     v  = input("v")
#     print(a+v)
# add()

# def raj():
#     a=int(input("enter a number"))
#     b=int(input("enter a number"))
#     print(a+b)
# raj()
# raj()
# raj()


# def nrij(name , age, last):
#     print(f'my name is {name } {last} anfa ge is  {age}')
# nrij(name ="raj",last="kumar",age=44)


# a =  0
# while a < 10:
#     if a == 5:
#         a=a+1
#         continue
#     print(a, end='\n')
#     a = a + 1

#function parameters

# # positional parameter
# # position parameter select value according to position
# def add(a,b,c):
#     print(a+c)
# add(2,3,4)
# add(3,4,5)

# def add(a,b,c):
#     print(a+c)
# add(2,3,4)

# #keyword parameter
# def dis(Name,age,last):
#     print(f'my name is {Name} {last} and my age is {age}')
# dis(age=24,Name='Ritik', last='sharma')
# dis(age=78,Name='Aman', last='Thakur')

# def func(name,age,category,marks):
#     print(f'your name is {name}, age is {age}, categroy is {category} and your total marks are {marks}')
# func(name="Raj Kumar", category="general", marks=90 ,age=24)

# #default parameter
# def add(a,b,c):
#     print(a+b+c)
# add(1,2,3)  
# add(2,3)
# # therefore default parameter
# def add(a=0,b=0,c=0):
#     print(a+b+c)
# add(1,2)
# add(1,2,3)

# # args
# def add(*args):
#     d=1
#     for i in args:
#         d=d+i
#         print(d)
# add(2,3,4)

# def add(*args):
#     d=0
#     for i in args:
#         d=d+i
#         print(d)
# add(3,4,5)

# #kwargs
# def add(**kwargs):
#     a=kwargs['Name']
#     b=kwargs['LastName']
#     c=a+b
#     print(a+b)
# add(Name='Ritik', LastName='sharma', age=24)


# def element(**kwargs):
#     a=kwargs['Name']
#     b=kwargs['surname']
#     c=kwargs['age']
#     print(a+b+c)
# element(Name="Raj Kumar", surname=" Thakur", age=24)

# def add(**kwargs):
#     a=kwargs['Name']
#     b=kwargs['surname']
#     c=a+b
#     print(c)
# add(Name='Raj Kumar', surname=' Thakur')

# def  kw(**tio):
#      print(tio,'---------------------------------------------')
#      a  = tio['name']
#      b = tio['ge']

#      print(a,b)

# kw(name  = 'myfunc',ge=55,ppp='pppp')

# def add(**kwargs):
#     a=kwargs['Name']
#     b=kwargs['last']
#     c=a+b
#     print(c)
# add(Name='Ritik', age=24, last='sharma')



# def printKwargs(**kwargs):
#     print(kwargs)
 
 
# # # driver code
# if __name__ == "__main__":
#     printKwargs(Argument_1='gfg', Argument_2='GFG')

# def func(**kwargs):
#     print(kwargs)

# func(NAME="Raj", Age=24)

#Local and Global Variables
# a=20
# def add():
#     global a
#     a=50
# add()
# print(a)

# a=1
# def add():
#     global a
#     for i in range(5):
#         a=a+1
#         print(a)
# add()
# print(a)

#global and local variable intro
# a=30
# def add():
#     global a
#     a=50
#     print(a)
# add()    
# print(a)    
# print(a)

#example 2
# a=0
# def add():
#     global a
#     for i in range(10):
#         print(a)
#         a=a+1
# print(a)        
# add()
# print(a) 


#example 3
# a=5
# def my_function():
#     global a
#     a=8
#     while a==8:
#         print(a)
#         a=a+1
# my_function()
# print(a)

# a=9
# def add():
#     global a
#     a=5
#     while a==5:
#         print(a)
#         a=a+1
# add()

#Nested Function
# def add():
#     print('Ritik')
#     def inner():
#         print("it is a nested function")
#     print("lets call nested funtion")
#     inner()
# print('hello')
# add()

#decorator
# def func(raj):
#     def delta(a,b):
#         print(a+b)
    
#     return delta

# @func
# def inner(a,b):
#      print("hello world")
# inner(3,4)

# def element(ship):
#     def delta(a,b):
#         print(a+b)
#     return delta
# @element
# def inner(a,b):
#     print("hello world")
# inner(4,4)

#nested function example 2
# def add():
#     print('rajesh')
#     def inner():
#         a=5 
#         for i in range(7):
#             print(a)
#     print("this is nested function")
#     inner()
# print('hello this is nested function')
# add()
# print('the end')

#return function
# def add():
#     return 24
# b=add()
# print(b)

# def add(a,b):
#     c=a+b
#     return c
# x=add(2,4)
# print(x)


#function return another function
# def add():
#     print('dgfgf')
# def my_function():
#     print("this is my_function")
#     return add
# y=my_function()
# y()


# def add():
#     print('add')
#     return function()

# def function():
#     print('my name is function')
#     return 24
# x=function()
# print(x)

# def my_function():
#     a=10
#     for i in range(4):
#         print(a)
# my_function()
# def add():
#     return my_function()
# y=add()

#function pass as an argument
# def add(a):
#     b=a()+10
#     print(b)
# def seven():
#     return 7
# add(seven)


#dictionary pass as a argument
# def dash(dicto):
#     for i in dicto:
#         print(i,dicto[i])
# dicto={"A":20,
#        "B":30,
#        "C":40}
# dash(dicto)


# def dash(dicto):
#     for i in dicto:
#         print(i,dicto[i])
# dicto={"A":20,
#        "B":30,
#        "C":40}
# dash(dicto)


# def dash(dicto):
#     for i in dicto:
#         print(i,dicto[i])
# dicto={"A":20,
#        "B":30,
#        "C":40}
# dash(dicto)


# def disc(a):
#     c=a()+11
#     print(c)
# def delta():
#     a=67
#     b=78
#     c=a+b
#     return c
# disc(delta)

# def my_function(delta):
#     c=delta()+34
#     print(c)
# def function():
#     return 10
# my_function(function)

# def disc(a):
#     b=9
#     c=a()+b
#     print(c)
# def dvd():
#     return 45
# disc(dvd)

#lambda function
# normal method
# def add(a,b):
#     print(a+b)
# add(45,34)
#lambda method
# function_name=lambda a,b : a+b
# print(function_name(2,3))

# delta=lambda a,b : a+b
# print(delta(4,5))

# delta=lambda a,b: a+b
# print(delta(5,6))

# my_function=lambda a,b: a*b
# print(my_function(5,4))

# recursion
# a=0
# def add():
#     global a
#     a=a+1
#     print(a)
#     return add()
# print(add())

# def function():
#     print('raj')
# a=0
# def add():
#     global a
#     a=a+1
#     print(a)
#     return function()
# add()

#decorator
# def A():
#     print('Ritik')

# @A
# def B():
#     def inner():
#         print('Sharma')
#     inner()
# B()

# def func(raj):
#     def inner(a,b):
#         print(a+b)
#     return inner
# @func    
# def add(a,b):
#     print("hello world")
# add(9,4)

# def examp(kat):
#     def inner(x,y):
#         print(x+y)
#     return inner
# @examp
# def func(x,y):
#     pass
# func(3,9)

# def b(func):
#     def inner(a,b):
#         print(a+b)
#         return a+b
#     return inner
# @b
# def a(a,b):
#     print('Ritik')
# a(1,2)


# def h(kite):
#     def inner(a,b):
#         print(a+b)
#         print("ashish")
#         # return a+b
#     return inner
# @h
# def c(a,b):
#     print(a+b)
# c(2,5)

# def sol(raj):
#     def inner(a,b):
#         print(a+b)
#     return inner
# @sol
# def func(a,b):
#     print(a+b)
# func(2,3)

# a=[1,2,3,[3,4,5,6,[5,6,7,8,[5,6,7,8]]]]
# def sol(l):
#     b=[]
#     for i in l:
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
#     return b
# y=sol(a)
# print(y)


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

# a=[1,2,3,[3,4,[5]],6,7,8]

# def sol(l):
#     b=[]
#     for i in l:
#         if isinstance(i,list):
#             b.extend(sol(i))
#         else:
#             b.append(i)
#     return b
# y=sol(a)
# print(y)

# user_input1=int(input("enter the number:"))
# user_input2=int(input("enter the number:"))
# for i in range(user_input1,user_input1+1):
#     for j in range(1,user_input2+1):
#         print(f'{i}*{j}={i*j}')







