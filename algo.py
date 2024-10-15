# a  =  [1,2,3,4,5,[1,2,3],5,{1,2 }]



# for i in a:
#     if isinstance(i,list):
#         a.remove(i)
#     # elif isinstance(i,set):
#     #     a.remove(i)

# print(a)

# a=[1,2,3,4,5,(4,5,6,7),9,6,5,6,4]
# for i in a:
#     if isinstance(i,tuple):
#         a.remove(i)
# print(a)

# a=[1,2,3,4,5,[1,2,3,4],5,6,7,{1,2,3,4}]
# for i in a:
#     if isinstance(i,list):
#         a.remove(i)
# print(a)

# a=[[1,2,3,4,5],[4,5,6,7,2,3],[2,3,5,8,5,2]]
# for x in a:
#     for k in range(len(x)):
#         g=x[k]
#         for l in range(len(x)):
#             h=x[l]
#             if x[k]<x[l]:
#                 c=x[k]
#                 x[k]=x[l]
#                 x[l]=c
# print(a)


# a=[[5,4,3,2,1],[9,8,7,6,5,4],[7,6,5,4,3,2]]
# for l in a:
#     for j in range(len(l)):
#         x=l[j]
#         for k in range(len(l)):
#             y=l[k]
#             if l[j]<l[k]:
#                 c=l[j]
#                 l[j]=l[k]
#                 l[k]=c
# print(a)
        

# a=[[2,3,4,53,2,4],[8,6,5,4,6,3],[9,7,8,6,2,3,6,4]]
# for x in a:
#     for k in range(len(x)):
#         b=x[k]
#         for l in range(len(x)):
#             h=x[l]
#             if x[k]<x[l]:
#                 c=x[k]
#                 x[k]=x[l]
#                 x[l]=c
# print(a)



    
            
# doubts
# a ={
#     "a":1,
#     "b":2,
#     "c":2,
#     "d":3,
#     "e":2,
#     "f":2
# }
 

# b=a.values()
# c={}
# y=1
# for i in b:
#     y=y+1
#     c.setdefault(i,y)
# print(c)

# a=['101','102','103']
# b=["salt",'wheat','rice']
# c=[1,2,3]

# while True:
#     user_input=input('enter user input:')
#     if user_input=="q":
#         break
#     total=0

#     for i in range(len(a)):
#         x=a[i]
#         if user_input==x:
#             indx=a.index(user_input)
#             total=total+c[indx]
# print(f'your item is {b[indx]} and its price is {c[indx]}')
# print("your total price is", total)

# a=['101','102','103']
# b=["salt",'wheat','rice']
# c=[1,2,3]
# bill=[]
# while True:
#     user_input=input('enter your number:')
#     if user_input=='q':
#         break
#     if user_input in a:
#         bill.append(user_input)
#         total=0
#         for i in bill:
#             indx=a.index(i)
#             total=total+c[indx]
# print(f'your item name is {b[indx]} and its price {c[indx]}')
# print('your total price is',total)


# item_number=['1','2','3','4','4']
# item_name=['coldrink', 'cream', 'burger', 'pizza', 'milk']
# item_price=[30,50,40,60,30]
# bill=[]
# while True:
#     user_input=input('enter user input')
#     if user_input=='q':
#         break
#     if user_input in item_number:
#         bill.append(user_input)
#     else:
#         input('enter a valid item numver')
#         for i in bill:
#             indx=item_number.index(i)
#             print(f'your item name is {item_name[indx]} and its price{item_price[indx]}')

# item_number=['1','2','3','4','4']
# item_name=['coldrink', 'cream', 'burger', 'pizza', 'milk']
# item_price=[30,50,40,60,30]
# while True:
#     user_input=input('enter your item number:')
#     if user_input=='q':
#         break
#     total=0
#     if user_input in item_number:
#         indx=item_number.index(user_input)
#         total=total+item_price[indx]
#         print(f'your item name is {item_name[indx]} and its price is  {item_price[indx]}')
# print(f'your total price is {total}')

# item_number=["1","2","3","4"]
# item_name=['maggie','biscuit', 'chocolate', 'candies']
# item_price=[20,30,40,50]
# bill=[]
# while True:
#     user_input=input('enter your item number:')
#     if user_input=='q':
#         break
#     if user_input not in item_number:
#         print('plzz enter a valid item number:')
#     elif user_input in item_number:
#         bill.append(user_input)
#         total=0
#         for i in bill:
#             indx=item_number.index(i)
#             total+=item_price[indx]
#             print(f'your item is {item_name[indx]} and its price is {item_price[indx]}')
# print(f'your total price is {total}')

# a={
#     'apple':'20',
#     'mango':'30',
#     'grapes':'40',
# }
# user_input=input('enter your item name or value of item:')
# b=list(a.keys())
# c=list(a.values())
# if user_input in b:
#     print(a.get(user_input))
    
# elif user_input in c:
#     indx=c.index(user_input)
#     print(b[indx])
# else:
#     print("not found")

# a={
#     'apple':'20',
#     'mango':'30',
#     'grapes':'40',
#     'banana':'50',
# }
# b=list(a.keys())
# c=list(a.values())

# user_input=input('enter your number')
# if user_input in b:
#     print(a.get(user_input))
# elif user_input in c:
#     indx=c.index(user_input)
#     print(b[indx])


# a={
#     'apple':'20',
#     'mango':'30',
#     'grapes':'40'
# }

# user_input=input('enter user input:')
# if user_input in a:
#    print(a.get(user_input)) 
# elif user_input not in a:
#    new_val=input('enter a new value')
#    a.update({user_input:new_val})
#    print(a)
  
# a={
#     'apple':'20',
#     'mango':'30',
#     'grapes':'40'
# }

# user_input=input('enter your number')
# if user_input in a:
#     print(a.get(user_input))
# elif user_input not in a:
#     new_val=input('enter a value')
#     a.update({user_input:new_val})
#     print(a)


# a={
#     'apple':30,
#     'mango':40,
#     'grapes':60,
# }
# c=0
# for i in a:
#     c=c+a[i]
# print(c)

# a={
#     'apple':30,
#     'mango':40,
#     'grapes':60,
# }
# c=0
# for i in a:
#     c=c+a[i]
# print(c)

# a={
#     '101':{
# 'name':'apple',
# 'price':20
#     },
#     '102':{
# 'name':'mango',
# 'price':30
#     }
# }

# user_input=input('enter user input')
# if user_input in a:
#     print(a.get(user_input).get('name'), 'and its price is' ,a.get(user_input).get('price'))
# else:
#     print('not found')
   

# a={
#     'apple':2,
#     'mango':3,
#     'grapes':3,
#     'orange':4,
#     'banana':4,
#     'cherry':5,
# }
# c=[]
# d=[]
# e={}
# x=list(a.values())
# for i in range(len(x)):
#     b=x[i]
#     if b not in c:
#         c.append(b)
#     elif b not in d:
#         d.append(b)
#         for j in range(len(d)):
#             y=d[j]
#             m=x.count(d[j])
#             z=e.setdefault(y,m)
# print(e)


# a={
#     'apple':2,
#     'mango':3,
#     'grapes':3,
#     'orange':4,
#     'banana':4,
#     'cherry':5}
# c=[]
# b=[]
# e={}
# x=list(a.values())
# for i in range(len(x)):
#     d=x[i]
#     if d not in c:
#         c.append(d)
#     elif d not in b:
#         b.append(d)
#         for j in range(len(b)):
#             y=b[j]
#             m=x.count(b[j])
#             z=e.setdefault(y,m)
# print(e)

# a={
#     "apple":'20',
#     "mango":'30',
#     "grapes":'40',
#     "oranges":'90'
# }
# b=list(a.keys())
# c=list(a.values())
# d=[]
# user_input=input("enter the value or key:")
# if user_input in a:
#     print(a.get(user_input))
# elif user_input in c:
#     indx=c.index(user_input)
#     print(b[indx])

# a={
#     "apple":'20',
#     "mango":'30',
#     "grapes":'40',
#     "oranges":'90'
# }

# user_input=input("enter the value")
# if user_input in a:
#     print(a.get(user_input))
# elif user_input not in a:
#     new_val=input("enter a  new value")
#     a.update({user_input:new_val})
# print(a)
    

# a={
#     "apple":'20',
#     "mango":'30',
#     "grapes":'40',
#     "oranges":'40',
#     "banana":'40',
#     "melon":'30'
# }   
# b=[]
# c=[]
# n={}
# v=0
# z=list(a.values())
# for i in range(len(z)):
#     x=z[i]
#     if x not in b:
#         b.append(x)
#     elif x not in c:
#         c.append(x)
#         for i in range(len(c)):
#             count=z.count(c[i])
#             m=n.setdefault(c[i], count)
# print(n)
            
# a=[1,1,2,2,3,4,5]
# b=[]
# c=[]
# for i in range(len(a)):
#     x=a[i]
#     if x not in b:
#         b.append(x)
#     elif x not in c:
#         c.append(x)
# print(c)

# a=[15,19,24,28,30,43,50]


# a  = 0
# b=  int(input('Enter a number'))
# while a < b:
#     c = 0
#     while c < a:
#         print('*', end=' ')
#         c=c+1
#     a=a+1
#     print('*')
#     print()

# a  = 0
# b=  int(input('Enter a number'))
# while a < b:
#     c = 0
#     while c < (b-a):
#         print('*', end=' ')
#         c=c+1
#     a=a+1
#     print()


# a={"a":'30', "b":'30', "c":'40',"d":'40', "e":'40', "f":'80',"e":'40'}
# b=list(a.values())
# # c={}
# # for i in range(len(b)):
# #     x=b[i]
# #     m=b.count(b[i])
# #     c.setdefault(x,m)
# # print(c)
# print(b)



# print(d)

# a={
#     "apple":'20',
#     "mango":'30',
#     "grapes":'40',
#     "oranges":'40',
#     "banana":'40',
#     "melon":'30'
# }   
# b=[]
# c=[]
# n={}
# z=list(a.values())
# for i in range(len(z)):
#     x=z[i]
#     if x not in b:
#         b.append(x)
#     elif x not in c:
#         c.append(x)
#         for i in range(len(c)):
#             count=z.count(c[i])
#             m=n.setdefault(c[i], count)
# print(n)
    

# a=0
# while a<10:
#     b=0
#     while b<a:
#         print("* ", end="")
#         b=b+1
#     print()
#     a=a+1
# a=0
# while a<10:
#     b=0
#     while b<(10-a):
#         print("* ", end="")
#         b=b+1
#     print()
#     a=a+1

# a=0
# while a<10:
#     b=0
#     c=0
#     while b<(10-a):
#         print(" ",end="")
#         b=b+1
#     while c<a:
#         print("*", end=" ")
#         c=c+1
#     print()
#     a=a+1

# a=0
# while a<10:
#     b=0
#     c=0
#     while b<a:
#         print(" ",end="")
#         b=b+1
#     while c<(10-a):
#         print("*", end=" ")
#         c=c+1
#     print()
#     a=a+1


# a={
#     "apple":20,
#     "orange":30,
#     "pomegrate":60,
#     "grapes":90,
# }
# b=list(a.values())
# c=list(a.keys())
# d=[]
# user_input=input("enter your number:")
# if user_input.isnumeric():
#     user_input =  int(user_input)
# if user_input in a:
#     print(a.get(user_input))
# elif user_input in b:
#     indx=b.index(user_input)
#     print(c[indx])

# a={
#     "1":{
#         "Question":"What is the name of Indian First Prime Minister? " "\n"
#         "(a) Dr. APJ Abdul Kalam" "\n"
#         "(b) SP Radha Krishnan" "\n"
#         "(c) Smt. Indira Gandhi" "\n"
#         "(d) Pandit Jawahar Lal Nehru" "\n",
#         "Answer":"d" ,
#     },
#     "2":{
#         "Question":"What is the name of Indian first President? " "\n"
#         "(a) Dr. APJ Abdul Kalam" "\n"
#         "(b) SP Radha Krishnan" "\n"
#         "(c) Rajendra Prasad" "\n"
#         "(d) Pandit Jawahar Lal Nehru" "\n",
#         "Answer":"c" ,
# }
# }

# b=0
# total=0

# while b<2:
#     user_input=input("enter the question number")
#     if user_input in a:
#         print(a.get(user_input).get("Question"))
#         new_val=input("enter your answer")
#         z=a.get(user_input).get("Answer")

#         if new_val==z:
#             print("your answer is correct")
#             total =total+1
#         else:
#             print("your answer is incorrect")
#             total=total-0.5
#         b=b+1
# print(f'your total score is {total}')

#factorial of number by function
# def raj(b):
   
#     a=1
#     for i in range(2,b+1):
#         a=a*i
#     return a
# c=8
# raj(c)
# print(f'factorial of c is {raj(c)}')


# def delta(n):
      
#     a = 1
     
#     for i in range(2, n+1):
#         a =a* i
#     return a
#  # Driver Code
# num = 8
# delta(num)
# print("Factorial of", num, "is",
# delta(num))

# a=pow(2,3)
# print(a)

# a=3
# b=2
# c=1
# for i in range(1,b+1):
#     c=c*a
# print(c)

# def delta(a,b,c):
#     for i in range(len(a)):
#         for j in range(len(b)):
#             if a[i]==b[j]:
#                 c.append(a[i])
#     return c
# x=[1,2,3,4,5]
# y=[3,4,5,6,7,8]
# z=[]
# y=delta(x,y,z)
# print(y)


# list=[1,2,2,3,3,4,4,5,5,5,6,6,6,6,7,7,7,7,8,9]   
# c=[]
# d=[]
# dictionary={}
# for i in range(len(list)):
#     x=list[i]
#     if x not in c:
#         c.append(x)
#     elif x not in d:
#         d.append(x)
#         for i in range(len(d)):
#             y=d[i]
#             z=list.count(d[i])
#             l=dictionary.setdefault(y,z)
# print(dictionary)
# print(d)

# Swap function
# def swapList(newList):
#     size = len(newList)
#     # Swapping 
#     temp = newList[0]
#     newList[0] = newList[size - 1]
#     newList[size - 1] = temp
#     return newList
# # Driver code
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))

#swapping of first and last element using function
# def delta(my_list):
#     my_list[0], my_list[-1]=my_list[-1], my_list[0]
#     return my_list
# my_list=[23,44,55,66,77,88]
# print(delta(my_list))

#swapping of first and last element using function
# def func(new):
#     a=len(new)
#     b=new[0]
#     new[0]=new[a-1]
#     new[a-1]=b
#     return new
# new=[12,35,9,56,24]
# print(func(new))

#swapping of first and last element using function
# def my_func(list):
#     b=list[0]
#     list[0]=list[-1]
#     list[-1]=b
#     return list
# list=[23,45,67,89,90]
# print(my_func(list))

# Python3 program to swap elements
# at given positions


# Swap function two elements
# def swapPositions(list, pos1, pos2):
# 	list[pos1], list[pos2] = list[pos2], list[pos1]
# 	return list
# # Driver function
# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
# print(swapPositions(List, pos1-1, pos2-1))

# def delta(list,a,b):
# 	list[a], list[b]=list[b],list[a]
# 	return list
# list=[12,33,44,56,78,67]
# a=2
# b=4
# print(delta(list,a-1,b-2))

#python ways to find the length of a list

# def delta(list):
#     b=0
#     for i in list:
#         b=b+1
#     print("the length of the list is", b)
# list=[1,2,3,4,5,6]
# delta(list)

#python program to find the maximum of two numbers in python
# def delta(a,b):
#     if a>b:
#         print("a is maximum")
#     elif b>a:
#         print("b is maximum")
#     else:
#         print("a is equal to b")
# delta(4,5)

# Python program to find the
# maximum of two numbers
# def maximum(a, b):
#     if a >= b:
#         return a
#     else:
#         return b
# # Driver code
# a = 2
# b = 4
# print(maximum(a, b))

#maximum of two numbers
# def delta(a,b):
#     if a>b:
#         return a
#     elif b>a:
#         return b
#     else:
#         return "both are equal"
# print(delta(4,4))

#simple method to find maximum of two number
# a=7
# b=9
# c=max(a,b)
# print(c)

#check if element exist in the list
# def my_func(list):
#     a=8
#     if a in list:
#         return "8 exist in list"
#     else:
#         return "8 not exist in list"
# list=[1,2,3,4,5,6,7,8,9]
# print(my_func(list))

# def my_func(list):
#     a=8
#     for i in list:
#         if i==a:
#             print("element exist")
# list=[1,2,3,4,5,6,7,8,9]
# my_func(list)



# program to print item details
# item_number = ['100','101','102','103','104']
# item_name   =  ['sugar', 'rice','poatato','biskit','colddrink']
# item_price = [40,70,25,20,40]

# bill = []
# while True:
#     get_i_n =  input('enter ur item number or quit with q ')
#     if get_i_n == 'q':
#         break

#     if get_i_n  not in item_number:
#         print('plz enter a valid item numbers')
#     elif get_i_n in item_number:
#         bill.append(get_i_n)
# total  = 0  
# for i in bill:
#     it_ind =  item_number.index(i)
#     total+= item_price[it_ind]
#     print(f'your item number is {i} your  item name is {item_name[it_ind]} price  {item_price[it_ind]}')
# print(f'your toal price is {total} peise dedo bhai')

#program to find whether the number is prime number or not
# num = int(input("enter a number: "))
# # input: 23
# flag = False
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             flag = True
#             break
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")
# 23 is a prime number

#program to find the largest of three numbers
# a=int(input("enter a number a"))
# b=int(input("enter a number b"))
# c=int(input("enter a number c"))
# if a>c and a>b:
#     print("a is largest")
# elif b>a and b>c:
#     print("b is largest")
# elif c>a and c>b:
#     print("c is largest")
# else:
#     print("all are equal")

#program to find the factorial of number
# a=1
# b=8
# for i in range(2,b+1):
#     a=a*i
# print(a)

#program to find the power of a number
# a=2
# b=4
# c=1
# for i in range(1,b+1):
#     c=c*a
# print(c)

# program to find index of second same element
# a=[1,1,1,1,2,4,5,2,6,8]

# b =[]
# # b   =  a.find(2,5)    b=a.find(2,1st index+1)
# for i in range(len(a)):
#     if a[i] == 2:
#         b .append(i)
# print(b)

# a=[1,2,3,4,2,5,6,7]
# b=[]
# for i in range(len(a)):
#     if a[i]==2:
#         b.append(i)
# print(b)

# a=[4,5,6,3,4,7,8,2,9,6,5,4]
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(a)):
#         y=a[j]
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
# print(a)
# print(a[len(a)-2])

# program to sort the elements using function bubble sort
# def bubble_sort(elements):
#     n = len(elements)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if elements[j] > elements[j + 1]:
#                 elements[j], elements[j + 1] = elements[j + 1], elements[j]

# # Test the function
# nums = [5, 2, 8, 1, 9]
# bubble_sort(nums)
# print(nums)


# def element(list):
#     n=len(list)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if list[j]>list[j+1]:
#                 list[j], list[j+1]=list[j+1], list[j]
#     return list
# list=[9,7,6,5,4,3,2,]
# y=element(list)
# print(y)

# list=[3,5,2,6,7,8,2]
# n=len(list)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)

# find common elements between two lists
# a=[1,2,3,4,5,6,7]
# b=[3,5,6,66,77,88,3,2]
# c=[]
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

# def delta(num,sum):
#     c=[]
#     for i in num:
#         if i in sum:
#             c.append(i)
#     return c
# num=[1,2,3,4,5]
# sum=[3,4,5,6,7,8,9]
# print(delta(num,sum))   

# def delta(num,sum):
#     c=[]
#     for i in range(len(num)):
#         x=num[i]
#         for j in range(len(sum)):
#             y=sum[j]
#             if x==y:
#                 c.append(x)
#     return c
# num=[1,2,3,4,5]
# sum=[3,4,5,6,7,8,9]
# print(delta(num,sum))

# def delta(num,sum):
#     c=[]
#     for i in num:
#         if i in sum:
#             c.append(i)
#     return c
# num=[1,2,3,4,5,6,7]
# sum=[3,5,6,66,77,88,3,2]
# print(delta(num,sum))

#program to reversing the string
# def string(num):
#     d=num[::-1]
#     return d
# my_string="hello this is Raj"
# print(string(my_string))

# remove duplicates elements from a list
# a=[1,2,3,3,4,4,5,5,6,7,8,99]
# d=[]
# c=[]
# for i in range(len(a)):
#     x=a[i]
#     if x not in d:
#         d.append(x)
#     elif x not in c:
#         c.append(x)
#         a.remove(x)
# print(a)

#remove duplicates from a list
# def remove_duplicates(numbers):
#     unique_numbers = []
#     for num in numbers:
#         if num not in unique_numbers:
#             unique_numbers.append(num)
#     return unique_numbers

# # Test the function
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# unique_nums = remove_duplicates(nums)
# print(unique_nums)

#remove duplicates from a list
# x=[1,2,2,3,3,44,4,5,6,7,7,7,8,9]
# c=[]
# for i in x:
#     if i not in c:
#         c.append(i)
# print(c)

# x=[1,2,2,3,3,4,5,6,7,8,8]
# c=[]
# for i in x:
#     if i not in c:
#         c.append(i)
# print(c)
        
# def my_func(num):
#     c=[]
#     for i in num:
#         if i not in c:
#             c.append(i)
#     return c
# list=[2,3,4,4,3,5,4,55,6,7,7,8,8,9,0]
# print(my_func(list))


#remove duplicate elements from list by converting dictionary into list
# a=[1,1,1,2,3,3,4,4,4,5]
# c={}
# for i in a:
#     c[i]=a[i]
#     d=list(c)
# print(d)
# print(c)

#recursion
# a=0
# def add():
#     global a
#     a=a+1
#     print(a)
#     return add()
# print(add())

# def check(s1, s2):
    
#     if(sorted(s1)== sorted(s2)):
#         print("The strings are anagrams.")
#     else:
#         print("The strings aren't anagrams.")        
        
# s1 = input("Enter string1: ")
# # input1: "listen"
# s2 = input("Enter string2: ")
# # input2: "silent"
# check(s1, s2)
# # Output: the strings are anagrams.



# a={
#     "1": {
#     "Question": "What is the name of Indian national Bird?" "\n"
#                  "(a) Peacock"  "\n"
#                  "(b) sparrow"  "\n"
#                  "(c) humming bird" "\n"
#                  "(d) ostrich" "\n",
#     "Answer": "a",

#     }
#     ,
#     "2": {
#     "Question": "What is the name of Indian national Animal?" "\n"
#                  "(a) Lion"  "\n"
#                  "(b) Tiger"  "\n"
#                  "(c) Giraffee" "\n"
#                  "(d) Deer" "\n",
#     "Answer": "a",

#     }

# }  
# total=0      
# b=0
# while b<2:
#     user_input=input("enter the question number:")
#     if user_input in a:
#         print(a.get(user_input).get("Question"))
#         your_answer=input("enter your answer:")
#         z=a.get(user_input).get("Answer")
#     if your_answer==z:
#         print("your answer is correct")
#         total=total+1
#     else:
#         print("your answer is incorrect")
#         total=total-0.5
#     b=b+1
# print(f'your total marks is {total}')

# a={
#     "sugar":20,
#     "bisucit":30,
#     "cream":40,
#     "wheat":20,
#     "rice":20,
# }
# b=list(a.keys())
# c=list(a.values())

# total=0
# while True:
#     user_input=input("enter your number")
#     if user_input.isnumeric():
#         user_input =  int(user_input)
#     if user_input=="q":
#         break
#     if user_input in a:
#         z=a.get(user_input)
#         print(a.get(user_input))
#         total=total+int(z)
#     elif user_input in c:
#         indx=c.index(user_input)
#         print(b[indx])
#     else:
#         print("enter a valid item")
# print(f"your total price is {total}")

# a={
#     "sugar":"20",
#     "bisucit":"30",
#     "cream":"40",
#     "wheat":"20",
#     "rice":"20",
# }
# user_input=input("enter the user input")
# if user_input in a:
#     print(a.get(user_input))
# elif user_input not in a:
#     new_val=input("enter a new value")
#     a.update({user_input:new_val})
#     print(a)


#sum of string in a list
# a=[12,34,56,78]
# z=[]
# for i in range(len(a)):
#     x=str(a[i])
#     count=0
#     for j in x:
#         count=count+int(j)
#     z.append(count)
# print(z)

# #find the last word of the string
# a="my name is raj"
# b=" "
# for i in range(len(a)):
#     b=b+a[i]
#     if a[i]==" ":
#         b=" "
# print(b)

# a="tHIS is rAj"
# b="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# d=""
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(b)):
#         y=b[j]
#         if a[i]==b[j]:
#             d=d+c[j]
# print(d)

# #print sum of numbers which you entered
# input=input("enter the number")
# d=0
# for i in input:
#     d=d+int(i)
# print(d)

# a=[1,2,3,4,5,9,6,5,4,3,8]
# for i in range(len(a)-2):
#     if a[i]+a[i+1]==a[i+2]:
#         print(a[i],a[i+1], a[i+2])

#print odd numbers in a list
# c=[]
# for i in range(1,50):
#     if i%2!=0:
#         c.append(i)
# print(c)

# def func(list,b):
    
#     for i in list:
#         if i<0:
#             b.append(i)
#     return b
# list=[1,2,3,-4,-5,-6]
# b=[]
# print(func(list,b))

#print numbers from a string
# string="my344ghtl"
# d=[]
# count=0
# for i in string:
#     if i.isnumeric():
#         d.append(i)
# print(d)

# #print numbers from a list
# z=[]
# list=[1,2,3,"myname",7]
# y=str(list)
# for i in y:
#     if i.isnumeric():
#         z.append(i)
# print(z)

#list compression print even number in a range
# b=[i for i in range(1,10) if i%2==0]
# print(b)

# #sum of number of elements in a list
# a=[2,3,4,5,6,7]
# b=0
# for i in range(len(a)):
#     b=b+a[i]
# print(b)

# a=[1,2,2,3,3,4,4,5,5,6,7,8]
# b=[]
# c=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#     elif i not in c:
#         c.append(i)
# print(c)

#remove duplicates from a list
# a=[1,2,3,3,4,4,5,5,6,7,8,9]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

#program to print class data
# a={
#     "1":
#         "Name: Raj Kumar" "\n"
#         "Class:12" "\n"
#         "Roll No.: 1" "\n"
#     ,
#     "2":
#         "Name:Ayush" "\n"
#         "Class:12"  "\n"
#         "Roll No. : 2" "\n",
#     "3":
#         "Name:neha" "\n"
#         "Class:12"  "\n"
#         "Roll No. : 2" "\n",
#     "4":
#         "Name:akash" "\n"
#         "Class:12"  "\n"
#         "Roll No. : 2" "\n",
    
# } 
# b=0
# while b<5:
        
#         user_input=(input("enter the Roll No.:"))
#         if user_input in a:
#             print(a.get(user_input))
#         b=b+1


#program to print tables
# for i in range(1,10+1):
#     for j in range(1,10+1):
#         print(f'{i}*{j}={i*j}')

# a={
#     "apple":30,
#     "orange":20,
#     "banana":10,
#     "grapes":60,
# }

# user_input=input("enter the name")
# if user_input in a:
#     print(a.get(user_input))
# elif user_input not in a:
#     print("enter a value")
#     new_value=input("enter the new value")
#     a.update({user_input:new_value})
#     print(a)

# a  =  [i for i in range(500)]
# for i in range(len(a)-2):
#     if  a[i] + a[i+1] == a[i+2]:
#         print(f'{a[i]} + {a[i+1]} = {a[i+2]}')




#remove multiple lists from a list

#greatest common divisor
# def gcd(a, b):
#     # Everything divides 0
#     if (a == 0):
#         return b
#     if (b == 0):
#         return a
#     # base case
#     if (a == b):
#         return a
#     # a is greater
#     if (a > b):
#         return gcd(a-b, b)
#     return gcd(a, b-a)
# # Driver program to test above function
# a = 96
# b = 56
# if(gcd(a, b)):
#     print('GCD of', a, 'and', b, 'is', gcd(a, b))
# else:
#     print('not found')


#greatest common divisor by recursion
# def hcf(a, b):
#     if(b == 0):
#         return a
#     else:
#         return hcf(b, a % b)
# a = 60
# b = 48
# # prints 12
# print("The gcd of 60 and 48 is : ", end="")
# print(hcf(60, 48))


#fibonacci series upto nterms
# c = int(input("How many terms? "))
# a, b = 0, 1
# if c <= 0:
#    print("Please enter a positive integer")
# elif c == 1:
#    print("Fibonacci sequence upto",c,":")
#    print(a)
# else:
#    print("Fibonacci sequence:")
#    count = 0
#    while count < c:
#        print(a)
#        final = a + b
#        a = b
#        b = final
#        count += 1




# class Calculator:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         print('welcome to Calculator', self.a, self.b,self.c)
#     def add(self):
#         print(self.a+self.b)
#     def divide(self):
#         print(self.a/self.b)
#     def multiply(self):
#         print(self.a*self.b)
#     def minus(self):
#         print(self.a-self.b)
# class Calculator:
#     def add(self,x,y):
#         print(self, x+y)
#     def divide(self):
#         print(self.a/self.b)
#     def multiply(self):
#         print(self.a*self.b)
#     def minus(self):
#         print(self.a-self.b)
# Raj=Calculator()
# Raj.add(80,90)
# Raj.divide()
# Raj.minus()
# Raj.__init__(1,21)

# brij  = Calculator(80,50,0)

# brij.add()




#find the greatest common factor or divisor
# a=60
# x=[]
# for i in range(1,60):
#     if a%i==0:
#         x.append(i)
# b=40
# y=[]
# for i in range(1,40):
#     if b%i==0:
#         y.append(i)
# l=set(x)
# k=set(y)
# z=l.intersection(k)
# f=list(z)
# print(max(f))


#fabonacci sequence
# user_input=int(input("how many terms?"))
# a,b=0,1
# if user_input==0:
#     print("enter a positive number")
# elif user_input==1:
#     print("fabonic sequence up to ", user_input)
#     print(a)
# else:
#     print("fabonic series:")
#     count=0
#     while count<user_input:
#         print(a)
#         final=a+b
#         a=b
#         b=final
#         count+=1
        

#program to make a clculator
# while True:
#     a=int(input("enter the value"))
#     b=int(input("enter the value"))
#     user_input3=(input("enter the operation you want to perform"))
#     if user_input3=="+":
#         print(a+b)
#     elif user_input3=="-":
#         print(a-b)
#     elif user_input3=="*":
#         print(a*b)
#     elif user_input3=="/":
#         print(a/b)
#     elif user_input3=="%":
#         print(a%b)

#program for frequency
# a=[1,2,3,3,4,5,5,6,7]
# b={}
# for i in a:
#     if i in b:
#         b[i]=b[i]+1
#     else:
#         b[i]=1
# print(b)

# a={
#     "1":{
#     "Question": "What is the name of India first prime minister?"
#                  "(a) Jawahar Lal Nehru"
#                  "(b) Rama bai"
#                  "(c) Tuka Ram"
#                  "(d) Radha krishnan",
#     "Answer":"a",
#     },
#     "2":{
#     "Question": "What is the name of India first prime minister?"
#                  "(a) Radha krishnan"
#                  "(b) Jawahar Lal Nehru"
#                  "(c) Tuka Ram"
#                  "(d) Radha krishnan",
#     "Answer":"b",
#     },
#     "3":{
#     "Question": "What is the name of India first prime minister?"
#                  "(a) Jawahar Lal Nehru"
#                  "(b) Rama bai"
#                  "(c) Tuka Ram"
#                  "(d) Radha krishnan",
#     "Answer":"a",
#     },
    
# }
# b=0
# total=0
# while b<4:
#     user_input=input("enter the question number")
#     if user_input in a:
#         print(a.get(user_input).get("Question"))
#         new_value=input("enter your answer")
#         z=a.get(user_input).get("Answer")
#         if new_value==z:
#             print("your answer is correct")
#             total=total+1
#         else:
#             print("your answer is not correct")
#             total=total-0.5
#     b=b+1
# print(f'your total marks is {total}')

   
# a=[1,2,3,4,5]
# d={i: i*i for i in a if i%2==0}
# print(d)

# x={i : i+2 for i in range(5)}
# print(x)

# y=[i for i in range(5)]
# print(y)

# a=[1,2,3,4,5,6,7,7]   
# v=a[1:5:1]
# print(v)

# a="12"
# it=iter(a)
# print(next(it))


# def func(a):
#     c=1
#     for i in range(2,a+1):
#         c=c*i
#     print(c)
# a=5
# func(a)

# def exmp(a,b):
#     c=1
#     for i in range(1,b+1):
#         c=c*a
#     return c
# a=2
# b=4
# print(exmp(a,b))

# b={}
# for i in range (1,100):
#     x=False
#     for j in range(2,i):
#         if i%j==0:
#             x=True
#     if x or i==1:
#         b[i]="not a prime number"
#     else:
#         b[i]="prime number"
# print(b)

# def func(list1,list2):
#     b=[]
#     for i in list1:
#         if i in list2:
#             b.append(i)
#     print(b)
# list1=[1,2,3,4,5,6,7,8]
# list2=[4,5,6,9,9]
# func(list1,list2)

# def bubblesort(list):
#     b=len(list)
#     for i in range(b-1):
#         for j in range(b-i-1):
#             if list[j]>list[j+1]:
#                 list[j],list[j+1]=list[j+1],list[j]
#     return list
# list=[6,5,4,3,2,1]
# print(bubblesort(list))

# a="testics"
# b="tecitsc"
# z=sorted(a)
# x=sorted(b)
# if z==x:
#     print("the string is anagrams")
# else:
#     print("not anagrams")

    
# c = int(input("How many terms? "))
# a, b = 0, 1
# if c <= 0:
#    print("Please enter a positive integer")
# elif c == 1:
#    print("Fibonacci sequence upto",c,":")
#    print(a)
# else:
#    print("Fibonacci sequence:")
#    count = 0
#    while count < c:
#        print(a)
#        final = a + b
#        a = b
#        b = final
#        count += 1

# a=16
# x=[]
# for i in range(1,a):
#     if a%i==0:
#         x.append(i)

# b=18
# y=[]
# for j in range(1,b):
#     if b%j==0:
#         y.append(j)

# l=set(x)
# k=set(y)
# z=l.intersection(k)
# print("the greatest common divisor of a and b is", max(z))


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


# n=5
# k=n-1
# for i in range(1,n):
#     for j in range(1,k):
#         print(" ", end ="")
#     k=k-1
#     for j in range(1,i+1):
#         print("*", end =" ")
#     print("\r")
    

# b=1
# for i in range(1,10):
#     for j in range(1,b):
#         print("*", end="")
#     print("\r")
#     b=b+1

# a=0
# b=10
# while a<b:
#     c=0
#     while c<a:
#         print("*", end ="")
#         c=c+1
#     print("\r")
#     a=a+1

# a=0
# b=10
# while a<b:
#     c=0
#     d=0
#     while c<(b-a):
#         print(" ", end="")
#         c=c+1
#     while d<a:
#         print("*", end=" ")
#         d=d+1
#     print("\r")
#     a=a+1

# num=1
# for i in range(1,6):
#     for j in range(1,i):
#         print(num, end="")
#         num=num+1
#     print("\r")

# def alphapat(n):
#     num = 65
#     for i in range(0, n):
#         for j in range(0, i+1):
#             ch = chr(num)
#             print(ch, end=" ")
#             num = num + 1
#         print("\r")
# n = 5
# alphapat(n)
    
# a=10
# b=a-1
# for i in range(1,a):
#     for j in range(1,b):
#         print(" ", end="")
#     b=b-1
#     for j in range(i):
#         print("*", end =" ")
#     print("\r")

pr




    


        


   
    




    























    
    
   
    
   




        

        



    






        
        























 

 






    
    

        

    
    
    
    
    




    
    



            

        

  

    



            

            

        

       
    









            

      


      

  






    







       
        



            
            
                




    





       
    
    
        

    
    

        

    