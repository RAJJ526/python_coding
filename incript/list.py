# a=['r','i','i']
# b=['k', 'I', 'y']
# for i in range(len(b)):
#     x=b[i]
#     a.append(x)
# print(a)

# a=['R', 'I', 'T']
# b=['7', '8', '9']
# a.append(b)
# print(a)

# a=['R', 'i', 't', 'i']
# b=['7', '8', '9']
# a.extend(b)
# print(a)

# a=['R', 'i', 't', 'i']
# b=['7', '8', '9']
# for i in range(len(b)):
#     x=b[i]
#     a.append(x)
# print(a)

# a=[1,2,3,4,5,6]
# b=[45,56,78,23,45]
# for i in range(len(b)):
#     x=b[i]
#     a.append(x)
# print(a)

# a=[7,8,9]
# a.pop(2)
# print(a)

# a=['r', 'rh', 'sh']
# a.remove('rh')
# print(a)

# a=[7,8,9]
# a.clear()
# print(a)


# a=[7,8,9]
# b=a.copy()
# print(b)

# a=[4,7,9,4]
# b=a.count(5)
# print(b)

# a=[4,5,3,8,5]
# b=a.index(8)
# print(b)

# a=[4,3,6,7,2]
# a.sort()
# print(a)

# a=7
# b=9
# c=a
# a=b
# b=c
# print(a)
# print(b)

# a=[1,2,3,4,5,6,7]
# print("Initial List: ", a)

# swapping two elements in a list
# a=[1,2,3,4,5,6,7]
# x=a[0]
# a[0]=a[-1]
# a[-1]=x
# print(a)


# fruits=['oranges', 'grapes', 'bananas']
# fruits[0], fruits[2]= fruits[2], fruits[0]
# print(fruits)


# a=[1,2,3,4,5,6,7]
# a[0], a[6]=a[6],a[0]
# print(a)

# a=[1,2,3,4,5,6,7]
# a[0], a[3]=a[3], a[0]
# print(a)

# txt = "Hello World"[::-1]
# print(txt)

# a=['Gfg', 'is', 'best', 'for', 'Geeks']
# c=[]
# for i in range(len(a)):
#     c.append(a[i][::-1])
# print(c)

# #sorting of list in list with the help of slicing or indexing
# a=[[5,4,3,2,1],[9,7,6,5,4],[6,5,4,3,2]]
# c=[]
# for i in range(len(a)):
#     c.append(a[i][::-1])
# print(c)

# a=['Gfg', 'is', 'best', 'for', 'Geeks']
# b=len(a)
# print(b)

# program to interchange first and last element in a list
# a=[1,2,3,4,5,6]
# x=a[0]
# b=a[-1]
# a[0]=a[-1]
# a[-1]=x
# print(a)

# # program to swap two elements in a list
# a=[1,2,3,4,5]
# a[0], a[1]=a[1], a[0]
# print(a)

# # reverse elements in a string list and also reverse the list
# a=['raj', 'taj', 'daj']
# c=[]
# for i in range(len(a)):
#     x=a[i]
#     b=x[::-1]
#     c.append(b)
#     c.reverse()
# print(c)

# #length of a list
# a=[1,2,3,4,5,6,7]
# b=len(a)
# print(b)

# #maximum of two numbers in a list
# a=10
# b=20
# if a>b:
#     print("maximum number is:",a)
# else:
#     print("maximum number is:", b)

# #minimum of two numbers
# a=10
# b=20
# if a<b:
#     print("minimum number is:",a)
# else:
#     print("minimum number is:", b)

# # program to check element exist or not
# a=[1,3,4,5,6]
# b=2
# if b in a:
#     print("exist")
# else:
#     print("not exist")

# clear the list with the help of slicing
# a=[1,2,3,4,5,6,7,8]
# b=a[:0]
# print(b)

#reversing a list in python
# a=[1,2,3,4,5,6]
# b=a[::-1]
# print(b)

#copy of a list
# a=[1,2,3,4,5,6]
# b=a.copy()
# print(b)
# count how many times an element exist

# a=[1,2,3,3,4,5,6,6,6,6,'ritik','ritik']
# b=a.count('ritik')
# print(b)

# another method to check occurence of element
# a = [8, 6, 8, 10, 8, 20, 10, 8, 8,8]
# x=9
# if x in a:
#     print('it exists')
# else:
#     print('not exists')

#python program to find sum and average of list in python
# a=[1,2,3,4,5,3,3]
# c=0
# for i in range(len(a)):
#     x=a[i]
#     c=c+a[i]
#     d=c/len(a)
# print(c)
# print(d)

# program to count even and odd number in a list
# a=[10,20,32,45,66,93,1,44]
# b,c=0,0
# for i in a:
#     if i%2==0:
#         b+=1
#     else:
#         c+=1
# print(b)
# print(c)

# program to print duplicate elements from list
# a=[1,2,3,3,3,4,5,5,5,6,6,7,8,9,9,]
# c=[]
# d=[]
# for i in a:
#     if i not in c:
#         c.append(i)
#     elif i not in d:
#         d.append(i)
# print(d)

# a=[1,2,3,34,5,6,6,7,8,8]
# c=[]
# d=[]
# for i in a:
#     if i not in c:
#         c.append(i)
#     elif i not in d:
#         d.append(i)
#         e=tuple(d)
# print(e)

# program to count even and odd number in tuple or list
# a=(10,20,32,45,66,93,1,44)
# b=0
# c=0
# for i in a:
#     if i%2==0:
#         b=b+1
#     else:
#         c=c+1
# print(b)
# print(c)


#program to print sum of string in a list
# a=[12,33,44,55,66]
# z=[]
# for i in range(len(a)):
#     d=str(a[i])
#     c=0
#     for j in d:
#         c=c+int(j)
#     z.append(c)
# print(z)

# a=[23,44,55,66,78]
# z=[]
# for i in range(len(a)):
#     x=str(a[i])
#     c=0
#     for j in x:
#         c=c+int(j)
#     z.append(c)
# print(z)
    

# print duplicate elements from a list
# a=[1,2,3,3,4,5,5,6,7,7,8]
# c=[]
# d=[]
# for i in a:
#     x=i
#     if x not in c:
#         c.append(x)
#     elif x not in d:
#         d.append(x)
# print(d)

#program to print sum of elements in a list
# a=[12,33,44,55,66]
# for i in a:
#     c=0
#     x=i
#     y=str(x)
#     for j in y:
#         c=c+int(j)
#     print(c)

#program to count even and odd numbers
#         a=[1,2,3,4,5,6,7,8,9]
#         c=0
#         d=0
#         for i in a:
#             if i%2==0:
#                 c=c+1
#             else:
#                 d=d+1
# print(c, "even numbers")
# print(d, "odd numbers")

#program to sort lists in a list
# a=[[1,2,3,4,5],[4,5,6,7,2,3],[2,5,8,5,3,2]]
# c=[]
# for k in a:
#     for i in range(len(k)):
#         x=k[i]
#         for j in range(len(k)):
#             y=k[j]
#             if k[i]<k[j]:
#                 c=k[i]
#                 k[i]=k[j]
#                 k[j]=c
# print(a)

# program to remove list from a list
# a=[1,2,3,4,[3,4,5,6],6,7,8]
# for i in a:
#     if isinstance(i,list):
#         a.remove(i)
# print(a)

# a=[1,2,3,4,[3,4,5,6],6,7,8]
# for i in a:
#     if isinstance(i,list):
#         a.remove(i)
# print(a)

#program to find index of second same element
# a=[1,1,1,1,2,4,5,2,6,8]
# b =[]
# # b   =  a.find(2,5)    b=a.find(2,1st index+1)
# for i in range(len(a)):
#     if a[i] == 2:
#         b .append(i)
# print(b)

#remove duplicate elements from list by converting dictionary into list
# a=[1,1,1,2,3,3,4,4,4,5]
# c={}
# for i in a:
#     c[i]=a[i]
#     d=list(c)
# print(d)
# print(c)
 

#remove duplicate elements from a list
# a=[1,2,2,3,3,3,4,5,6,7]
# for i in a:
#     for j in a:
#         if i==j:
#             a.remove(j)
# print(a)

# a = range(1,15)+
# b =  range(15,20)
# c =  range(20,30)
# x =  input('enter yoy daye')

# if int(x) in a:
#     print('leo')
# elif int(x) in b:
#     print('libra')
# elif int(x) in c:
#     print('ro')

# a= range(1,15)
# b= range(15,20)
# c= range(20,30)
# d=range(15,17)
# x=input('enter your age')

# if int(x) in a:
#     print('leo')
# elif int(x) in c:
#     print('libra')

#remove duplicates from a list
# a  =  [2,2,5,5,5,6,6,7,7,8,8,98,98,98,5]
# b=  set(a)
# a  =  list (b)
# print(a)

# a=[2,3,4,4,5,5,6,6,7,7,8,9]
# b=set(a)
# a=list(b)
# print(a)

# remove unnecessay list tuples set from the list
# b=[{4,3,2,7,8},[4,3,2,5],{1,2,3,4},2,3,4,5,"rjgjt",[]]
# a=0
# while True:  
#     x= 1
#     for i in b:
#         if isinstance(i,list):
#             x=0
#         elif isinstance(i,set):
#             x=0
#     if x is 1:
#         break
#     if isinstance(b[a],list):
#         b.remove(b[a])
#         continue
#     elif isinstance(b[a],set):
#         b.remove(b[a])
#         continue
#     a=a+1
#     x=1
# print(b)

# b=[2,3,4,5,"rjgjt",[]]
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

# def my_func(num):
#     c=[]
#     for i in num:
#         if i not in c:
#             c.append(i)
#     return c
# list=[2,3,4,4,3,5,4,55,6,7,7,8,8,9,0]
# print(my_func(list))


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
# num=[1,2,3,4,5,6,7]
# sum=[3,5,6,66,77,88,3,2]
# print(delta(num,sum))


#  program to sort the elements using function bubble sort
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


# list=[3,5,2,6,7,8,2]
# n=len(list)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if list[j]>list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
# print(list)


#program to sort a list
# a=[7,6,5,4,3,2]
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(a)):
#         y=a[j]
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
# print(a)











    

    
    



















    




    
    
    



    
   

    
    
    









