# a=()
# a=tuple()
#indexing in tuple
# a=(2,4,7,8,9)
# b=a[4]
# print(b)

# # slicing in tuple
# a=(2,4,5,6,7,9)
# b=a[0:5:1]
# print(b)

# # count in tuple
# a=(4,7,9,'R',9,'R')
# b=a.count(4)
# print(b)

# # string indexing in tuple
# a=(1,2,3,'ritik',4,5,6)
# b=a.index("ritik")
# print(b)

# # data casting type 
# #add a new element in tuple
# a=(1,3,4,5)
# b=list(a)
# b.append(2)
# c=tuple(b)
# print(c)

# #insert a new element in tuple at which index you want
# a=(1,3,4,5)
# b=list(a)
# b.insert(2,8)
# c=tuple(b)
# print(c)

# # add a new element in tuple by different method
# a=(2,4,5,7,8)
# b=a+(1,9)
# print(b)

# # # add a new element in tuple by other method
# a=(2,4,5,7,8)
# b=a[0:2]+(1,6)+a[2:]
# print(b)

# # for loop in tuple
# a=(1,2,3,4,5,6,)
# for i in range(len(a)):
#     print(a[i])

#tuple program to interchange first and last element of a list
# a=(1,2,3,4,5,6,7)
# b=list(a)
# c=b[0]
# b[0]=b[-1]
# b[-1]=c
# d=tuple(b)
# print(d)

# python program to swap two elements in tuple
# a=(1,2,3,4,5,6,7,8)
# b=list(a)
# c=b[0]
# b[0]=b[4]
# b[4]=c
# d=tuple(b)
# print(d)

#python program to swap elements in a string list

# a=('ritik','raj','lokesh')
# b=list(a)
# c=[]
# for i in b:
#     x=i
#     d=x[::-1]
#     c.append(d)
#     e=tuple(c)
# print(e)

# python ways to find length of a tuple
# a=(1,2,3,4,5,6,7)
# b=list(a)
# c=len(b)
# print(c)

#program to check element exist in a tuple
# a=(1,2,3,4,5,6,7)
# b=6
# if b in a:
#     print("exist")
# else:
#     print("not exist")

#different ways to clear a tuple in python
# a=(1,2,3,4,5,6,7)
# b=list(a)
# b.clear()
# d=tuple(b)
# print(d)

#python reversing a tuple
# a=(1,2,3,4,5,6,7)
# b=list(a)
# b.reverse()
# d=tuple(b)
# print(d)

# reversing a tuple with the help of slicing
# a=(1,2,3,4,5,6,7)
# b=list(a)
# c=b[::-1]
# print(c)

#python cloning or copying a tuple
# a=(1,2,3,4,5,6,7)
# b=list(a)
# z=b.copy()
# d=tuple(z)
# print(d)

#python count occurence of an element in a tuple
# a=(1,2,3,4,4,4,5,6,7)
# b=4
# c=[]
# for i in a:
#     if b==i:
#         c.append(b)
#         d=c.count(4)
# print(d)

# a=(1,2,3,4,5,6,6,6,7)
# b=list(a)
# d=b.count(6)
# print(d)

#program to find sum and average of tuple
# a=(1,2,3,4,5,6,7)
# c=0
# for i in range(len(a)):
#     x=a[i]
#     c=c+a[i]
#     d=c/len(a)
# print(c)
# print(d)

#program to multiply all numbers in a tuple
# a=(1,2,3,4,5,6)
# c=1
# for i in range(len(a)):
#     x=a[i]
#     c=c*a[i]
# print(c)

# a=(1,2,3,4,5,6)    
# c=1
# for i in a:
#     c=c*i
# print(c)

#program to find the smallest number in a tuple
# a=(2,3,4,1,6,7)
# b=list(a)
# b.sort()
# d=tuple(b)
# x=d[0]
# print(x)

# program to find even numbers in a tuple
# a=(8,2,3,4,48,6,7,8)
# for i in a:
#     if i%2==0:
#         print(i)

# program to count even and odd number in a tuple
# a=(8,2,3,4,48,6,7,8)
# c=[]
# for i in a:
#     if i%2!=0:
#         c.append(i)
#         d=len(c)
# print(d)

#program to print positive numbers in a tuple
# a=(1,2,3,-4,-5,-6,-7,8,9)
# for i in a:
#     if i>0:
#       print(i)

# #program to print negative numbers in a tuple
# a=(1,2,3,-4,-5,-6,-7,8,9)
# for i in a:
#     if i<0:
#       print(i)

# # program to count positive and negative number in a tuple
# a=(1,2,3,-4,-5,-6,-7,8,9)
# c=[]
# for i in a:
#    if i<0:
#       c.append(i)
#       d=len(c)
# print(d)

# # program to remove multiple elements from tuple
# a=(1,2,3,4,5,6,7,8)
# b=list(a)
# for i in b:
#    if i%2==0:
#       b.remove(i)
#       d=tuple(b)
# print(d)

#program to print duplicate elements from tuple
# a=(4,5,6,7,7,7,6)
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#         d=tuple(b)
# print(d)

# program to print duplicate elements from tuple
# a=(1,2,3,3,3,4,5,5,5,6,6,7,8,9,9,)
# c=[]
# d=[]
# for i in a:
#     if i not in c:
#         c.append(i)
#     elif i not in d:
#         d.append(i)
#         e=tuple(d)
# print(d)
 
# a=[1,2,3,3,3,4,4,5,6,7,7,8,9]
# c=[]
# d=[]
# for i in a:
#     if i not in c:
#         c.append(i)
#     elif i not in d:
#         d.append(i)
#         e=tuple(d)
# print(e)

# program to count even and odd number in tuple
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


    







  
            
    

    
      
      























    



        
    
  







    







        









    





        

   





















