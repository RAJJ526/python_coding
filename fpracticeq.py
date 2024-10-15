
#factorial of a number using function
# def delta(n):      
#     a = 1    
#     for i in range(2, n+1):
#         a =a* i
#     return a
#  # Driver Code
# num = 8
# delta(num)
# print("Factorial of", num, "is",delta(num))

# def alpha(b):
#     a=1
#     for i in range(2,b+1):
#         a=a*i
#     return a
# num=5
# alpha(num)
# print(f'factorial of 5 is {alpha(num)}')

# factorial of a number by calling the function
# def func():
#     a=1
#     n=8
#     for i in range(2,n+1):
#         a=a*i
#     print(a)
# func()

# simple factorial formula
# a=1
# b=8
# for i in range(2,b+1):
#     a=a*i
# print(a)

# a=1
# b=6
# for i in range(2,b+1):



# def delta():
#     a=2
#     b=9
#     print(a+b)
#     return a+b
# delta()

#How to print multiple arguments in python
# def GFG(name, num):
#     print("Hello from ", name + ', ' + num)
# GFG("geeks for geeks", "25")

# def delta(name,num):
#     print("hello from",name,num)
# delta("RAJ",45)

# def delta(name,num):
#     print(f'His name is {name}  and his total marks are {num} ')
# delta("Raj", 57)

# def GFG(name, num="25"):
#     print("Hello from", name + ', ' + num)
# GFG("gfg")
# GFG("gfg", "26")

# def delta(name,num="45"):
#     print(f'hello  from {name} and how are {num}')
# delta("Raj","you")

# def delta(name,num):
#     print(f'hello  from {str(name)} and how are {str(num)}')
# delta("Raj",45)

#find the power of a number method 1
# print(pow(9, 2))

#method 2
# a=pow(5,2)
# b=pow(4,2)
# c=a+b
# print(c)

#simple formula for find the power of a number
# a=3
# b=2
# p=1
# for i in range(1,b+1):
#   p=p*a
# print(p)
  
# find power of a number by passing the argument
# def CalculatePower(a,b):
#   P=1
#   for i in range(1, b+1):
#     P=P*a
#   return P
# N,X=2,3
# print(CalculatePower(N,X))
# N,X=3,4
# print(CalculatePower(N,X))

# def my_func(a,b):
#   c=1
#   for i in range(1,b+1):
#     c=c*a
#   return c
# num1=5
# num2=4
# my_func(num1,num2)
# print(f'the power of {num1} raise to power 4 is {my_func(num1,num2)}')


#find the power of a function by calling the function
# def delta(a,b):
#   p=1
#   for i in range(1,b+1):
#     p=p*a
#   return p
# y=delta(2,4)
# print(y)

#function that accepts vairable length key value pair as argument
#example 1
# def printKwargs(**kwargs):
#     print(kwargs)
# # # driver code
# if __name__ == "__main__":
#     printKwargs(Argument_1='gfg', Argument_2='GFG')

#example 2
# def func(**kwargs):
#     print(kwargs)
# func(NAME="Raj", Age=24)

#example 3
# using kwargs
# in functions
# def printValues(**kwargs):
# 	for key, value in kwargs.items():
# 		print(f"The value of {key} is {value}")
# # driver code
# if __name__ == '__main__':
# 	printValues(abbreviation="GFG", full_name="geeksforgeeks")

#example 4     
# def func(**kwargs):
# 	for key, value in kwargs.items():
# 		print(f'the key is {key} and the value is {value}')
# func(key="fire", role="creating fire" )
     


#assign a function to a variable in python
#example 1
# def delta():
#   print("Raj Kumar")
# var=delta
# var()  

#example 2
# def func(a):
#   if a%2==0:
#     print("even number")
#   else:
#     print("odd number")
# z=func
# z(5)

#example 3
# defined function
# x = 123
# def sum():
#     x = 98
#     print(x)
#     print(globals()['x'])
# # drivercode
# print(x)
# # assigning function
# z = sum
# # invoke function
# z()


#function return another function
#example 1
# define two methods 
# second method that will be returned
# by first method
# def B():
#     print("Inside the method B.")
# # first method that return second method
# def A():
#     print("Inside the method A.")
#     # return second method
#     return B
# # form a object of first method 
# # i.e; second method
# z = A()
# # call second method by first method
# z()


#function return another function example 2
# def raj():
#     print("this is raj")
# def kumar():
#     print("this is kumar")
#     return raj
# y=kumar()
# y()


#find the power of a function using recursion

#example 3
# # first method that return second method
# def A(u, v):
#     w = u + v
#     z = u - v
    
#     # return second method without name
#     return lambda: print(w * z)

# # form a object of first method 
# # i.e; second method
# returned_function = A(5, 2)
# # check object
# # print(returned_function)

# # call second method by first method
# returned_function()

# def delta(a,b):
#     c=a+b
#     d=a-b
#     return lambda: print(c*d)
# y=delta(5,2)
# y()

# def alpha():
#     print('this is raj')
    
# def delta():
#     print("this is kumar")
#     return lambda: print(2*4)
# y=delta()
# print(y)

#check whether the number is prime or not
# a=int(input("enter a number"))
# check=False
# for i in range(2,a):
#     if a%i==0:
#         check = True
# if check or a==1:
#     print("not a prime number")
# else:
#     print("prime number")

#check whether the number is prime number or not
# a=int(input("enter a number"))
# check=False
# for i in range(2,a):
#     if a%i==0:
#         check=True
# if check or a==1:
#     print("not a prime number")
# else:
#     print(" prime number")


# def count_frequency(numbers):
#     frequency = {}
#     for num in numbers:
#         if num in frequency:
#             frequency[num] += 1
#         else:
#             frequency[num] = 1
#     return frequency

# # Test the function
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# frequency_count = count_frequency(nums)
# print(frequency_count)

# #find the frequency of a numbers
list=[1,2,3,2,1,3,2,4,5,4]
d={}
for i in list:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)

# Program Code to find the frequency of numbers or actual program to print duplicate elements and how many they come
# list1 = [4, 6, 8, 9, 10]
# list2 = [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]
# frequency = {}
# for item in list1:
# 	count = 0
# 	for element in list2:
# 		if item == element:
# 			count += 1
# 	frequency[item] = count
# print("Lists elements Frequency :", frequency)

# a=[1,2,3,4,5,6]
# b=[1,1,2,2,2,3,4,6,3,4,5,6,7]
# d={}
# for i in a:
# 	count=0
# 	for j in b:
# 		if i==j:
# 			count=count+1
# 	d[i]=count
# print(d)

# actual program to print duplicate elements and how many time it come
# list1=[2,3,4,5,6,7]
# list2=[1,22,3,4,2,5,6,7,2,2,2,6,8,6,7,9,5,3,4,5,6,7,2,9]
# dictionary={}
# for i in list1:
# 	count=0
# 	for j in list2:
# 		if i==j:
# 			count=count+1
# 	dictionary[i]=count
# print(dictionary)
	
# def element(num,sum):
# 	dictionary={}
# 	for i in num:
# 		count=0
# 		for j in sum:
# 			if i==j:
# 				count=count+1
# 		dictionary[i]=count
# 	print(dictionary)
# num=[2,3,4,5,6,7]
# sum=[1,22,3,4,2,5,6,7,2,2,2,6,8,6,7,9,5,3,4,5,6,7,2,9]	
# element(num,sum)

#string is palindrome or not  
# string="madam"
# b=string[::-1]
# if b==string:
#     print("string is palindrome")
# else:
#     print("not palindrome")  


#program to find index of second same element
# a=[1,1,1,1,2,4,5,2,6,8]

# b =[]
# # b   =  a.find(2,5)    b=a.find(2,1st index+1)
# for i in range(len(a)):
#     if a[i] == 2:
#         b .append(i)
# print(b)

#program to find maximum of two numbers
# def maximum(a, b):
    
#     if a >= b:
#         return a
#     else:
#         return b
    
# a = int(input("Enter a number: "))
# # input1: 2
# b = int(input("Enter a number: "))
# # input2: 4
# print(maximum(a, b))
# # output: 4

#program to find the maximum of two numbers
# def delta(a,b):
#     if a>b:
#         return a
#     elif b>a:
#         return b
#     else:
#         return "a equal to b"
# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# y=delta(a,b)
# print(y)

#find factorial
# def factorial(user_input):
#     b=1
#     for i in range(2,user_input+1):
#         b=b*i
#     return b
# user_input=int(input("enter a number"))
# print(factorial(user_input))

#find the power of a number
# def power(user_input,user_input2):
#     c=1
#     for i in range(1,user_input2+1):
#         c=c*user_input
#     return c
# user_input=int(input("enter the number:"))
# user_input2=int(input("enter the number:"))
# print(power(user_input,user_input2))
    
#find the frequency of a numbers
# list=[1,2,3,2,1,3,2,4,5,4]
# d={}
# for i in list:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

# listo=[1,2,2,3,3,4,4,5,5,6,6,7,7,8]
# d={}
# for i in listo:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

#remove duplicates elements from the list
# a=[1,2,2,3,3,4,4,5,5,6,7]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#make right angle triangle using for loop
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("\n")

# def func(a):
#     for i in range(1,a):
#         for j in range(1,i+1):
#             print("*", end="")
#         print("\r")
# a=6
# func(a)

# user_input=int(input("enter the number:"))
# for i in range(1,user_input):
#     for j in range(1,i+1):
#         print("*", end="")
#         print("\r")

#make the triangle pattern using for loop
# def myfunc(n):
#     k = n - 1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 1
#         for j in range(0, i+1):
#             print("* ", end="")
#         print("\r")
# n = 5
# myfunc(n)

# n=8
# k=n-1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         print(" ", end="")
#     k=k-1
#     for j in range(0,i+1):
#         print("*",end=" ")
#     print("\r")

#program to print number pattern
# for i in range(1,6):
#     num=1
#     for j in range(1,i+1):
#         print(num, end="")
#         num=num+1
#     print("\r")
        
#program to print numbers in series pattern
# num=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(num, end="")
#         num=num+1  
#     print("\r")

#new pattern
# num=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(num, end="")
#         num=num+1  
#     print("\r")


#Alphabetical patterns series            
# def alphapat(n):
#     num = 65
#     for i in range(0, n):
#         for j in range(0, i+1):
#             ch = chr(num)
#             print(ch, end=" ")
#         num = num + 1
    
#         print("\r")
# n = 5
# alphapat(n)


# for i in range(1,7):
# num=65
# for i in range(1,7):
#     for j in range(1,i+1):
#         print(chr(num), end="")
#     num=num+1
#     print("\r")

# num=65
# for i in range(1,9):
#     for j in range(1,i+1):
#         print(chr(num),end="")
#         num=num+1
#     print("\r")


# for i in range(1,9):
#     num=65
#     for j in range(1,i+1):
#         print(chr(num),end="")
#         num=num+1
#     print("\r")
    
#pythton program to direct remove duplicates elements without any other list
# a=[1,2,2,3,3,4,4,5,5,5,6,6,7,8]
# for i in a:
#     n=i
#     z=a.count(i)
#     if z>1:
#         a.remove(i)
# print(a)

#counting vowels in a given word
# vowel=['a','e','i','o','u']
# word="programiang"
# count=0
# for i in word:
#     if i in vowel:
#         count=count+1
# print(count)

# vowel=['a','e','i','o','u']
# word="programming"
# count=0
# for i in word:
#     if i not in vowel:
#         count+=1
# print(count)

#convert list into dictionaries
# def convert(lst):
#    res_dict = {}
#    for i in range(0, len(lst), 2):
#        res_dict[lst[i]] = lst[i + 1]
#    return res_dict

# lst = ['a', 1, 'b', 2, 'c', 3]
# print(convert(lst))

# def add(lst):
#     b={}
#     for i in range(0,6,2):
#         b[lst[i]]=lst[i+1]
#     return b
# lst=["a",1,"b",2,"c",3]
# print(add(lst))

# def add(list):
#     b={}
#     for i in range(0,6,2):
#         b[list[i]]=list[i+1]
#     return b
# list=["a",3,"b",6,"c",9]
# print(add(list))










   
 

    

    





  


        
    



    