# a="my name is ritik"
# c=" "
# for i in range(len(a)):
#     c=c+a[i]
#     if a[i]==" ":
#      c=" "
# print(c)

# print word of the string
# a='my name is ritik'
# c=" "
# for i in range(len(a)):
#    c=c+a[i]
#    if a[i]==" ":
#       c=" "
# print(c)

# a="hello this is raj"
# c=" "
# for i in range(len(a)):
#     c=c+a[i]
#     if a[i]==" ":
#         c=" "
# print(c)


# print sum of digits in a string
# b='0123456789'
# a='Riti7ik4i404jf94jf9'
# c=0
# for i in range(len(a)):
#    if a[i] in b:
#       c=c+int(a[i])
# print(c)

# b='0123456789'
# a='Riti7ik4i56lfk'
# c=0
# for i in range(len(a)):
#    x=a[i]
#    if a[i] in b:
#       c=c+int(a[i])
# print(c)

# import random
# wining_number  =  random.randint(1,100)
# for i in range(1,4):
#    guess_number = input('enter your gussing number')
#    int_guess_number  = int(guess_number)
#    if int_guess_number == wining_number:
#       print('you win', wining_number)
#       break
#    else:
#       print('your numbrr is worn plzz')
#       if i  == 3:
#          print('game over',wining_number)

# import random
# winning_number=random.randint(1,100)
# for i in range(1,4):
#     guess_number= input('enter your guessing number')
#     int_guess_number=int(guess_number)
#     if int_guess_number==winning_number:
#         print('you win', winning_number)
#         break
#     else:
#         print('your number is wrong')
#         if i ==3:
#             print('game over', winning_number)

# winning_number=54
# for i in range(1,7):
#     guess_number=input('enter your number:')
#     int_guess_number=int(guess_number)
#     if int_guess_number==winning_number:
#         print('you win', winning_number)
#         break
#     else:
#         print('wrong number enter the number again')
#         if i==4:
#             print('game over', winning_number)




# x='MYNAMEISRITIK'
# a='abcdefghijklmnopqrstuvwxyz'
# A='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# c=''
# for i in range(len(x)):
#     z=x[i]
#     for j in range(len(a)):
#      L=a[j]
#      if z==L:
#         c=c+A[j]
# print(c)

# x='THIS IS AK RAJ'
# a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# A="ABCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyz"
# c=''
# for i in range(len(x)):
#    z=x[i]
#    for j in range(len(a)):
#       l=a[j]
#       if z==l:
#          c=c+A[j]
# print(c)


# a="bRiJmohaNraNa"
# b="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# c="abCDEFGhiJKLmnoPQrSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# d=''
# for i in range(len(a)):
#    y=a[i]
#    for j in range(len(b)):
#       z=b[j]
#       if y==z:
#          d=d+c[j]
# print(d)

# #Questions


# x='RitiKShArMa'
# a='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# A='ABCDEFGHIJkLMNOPQRSTUVWXYZabcdefghijklmnopqRstuvwxyz'
# c=''
# for i in range(len(x)):
#     z=x[i]
#     for j in range(len(a)):
#      L=a[j]
#      if z==L:
#         c=c+A[j]
# print(c)

# x="RitiksharmA"
# a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# A="aBCDEFGhiJkLmNOPQrstUVWXYZAbcdefghijklmnopqRstuvwxyz"
# c=""
# for i in range(len(x)):
#    z=x[i]
#    for j in range(len(a)):
#       L=a[j]
#       if z==L:
#          c=c+A[j]
# print(c)

# sorting the list 
# a=[9,6,5,4,3,2,8,10,9,9,9,2,9]
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(a)):
#         y=a[j]
#         if a[i]<a[j]:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
# print(a)
    

# print sum of numbers which you entered
# a = input('eyn')
# c=0
# for i in range(len(a)):
#     c= c+ int(a[i])
# print(c)


# user_input=input('enter your number')
# c=0
# for i in range(len(user_input)):
#     c=c+int(user_input[i])
# print(c)

# a=[7,2,4,3,7,9,3,0,1]
# b=[7,2,4,9]
# for i in range(len(a)):
#     x=a[i]
#     if x not in b:
#         b.append(x)
# print(b)


# a=[2,5,6,7,8,8,0]
# b=[4,0,3]
# for i in range(len(b)):
#     x=b[i]
#     if x not in a:
#         a.append(x)
#         print(a)

#sorting of a list
# a=[9,2,4,5,12,6]
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(a)):
#         y=a[j]
#         if x<y:
#             c=a[i]
#             a[i]=a[j]
#             a[j]=c
# print(a)

# a=[2,5,6,7,8,8,0]
# b=[4,0,3]
# for i in range(len(b)):
#     x=b[i]
#     if x not in a:
#         a.append(x)
#         print(a)

# a=[1,2,3,7,10,1,12]
# for i in range(len(a)-2):
#     if a[i]+a[i+1] == a[i+2]:
#         print(a[i], a[i+1], a[i+2])

# a=[1,2,3,7,10,1,2,2,4]
# for i in range(len(a)-2):
#     if a[i]+a[i+1]==a[i+2]:
#         print(a[i], a[i+1],a[i+2])


# a=[4,7,9,2,5,3,9]
# for i in range(len(a)):
#     x=a[i]
#     if x%2 == 0:
#         print(x)

# a=[4,7,9,2,5,3,9]
# for i in range(len(a)):
#     x=a[i]
#     if x%2 !=0:
#         print(x)

# a=[4,-7,9,-2,5,-3,9]
# for i in range(len(a)):
#     x=a[i]
#     if x==x<0:
#         print(x)

# for i in range(1,500):
#     if i%2==0:
#         print(i)

# import random
# wining_number  =  random.randint(1,100)
# for i in range(1,4):
#    guess_number = input('enter your gussing number')
#    int_guess_number  = int(guess_number)
#    if int_guess_number == wining_number:
#       print('you win', wining_number)
#       break
#    else:
#       print('your numbrr is worn plzz')
#       if i  == 3:
#          print('game over',wining_number)


# a=[1,2,5,7,9,1,3,4]
# for i in range(len(a)-2):
#     if a[i]+a[i+1]==a[i+2]:
#         print(a[i], a[i+1], a[i+2])


# a=[2,1,3,9,5]
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(a)):
#         y=a[j]
#         if x>y:
#             z=x
#             x=y
#             y=z
#             print(a)

# nested loop

# for i in range(1,10):
#     for j in range(1,10):
#         print("j",end='')

# for i in range(1,10):
#    for j in range(1,10):
#       print("j", end='')

# a=['a','b','c','d']
# a.reverse()
# print(a)

# a =[(),'1','4',[]]
# b =[]
# for i in a :
#     if len(i) >0:
#         b.append(i)
# print(b)

#print number digits from list
# a=[(),'R',2,4]
# b=[]
# for i in range(len(a)):
#     x=a[i]
#     if len(x)>0:
#         b.append(x)

# a=[2,3,5,0,9]
# x=a[0]
# y=a[-1]
# a[0], a[1]=a[1], a[0]
# print(a)

#swapping the elements in a list
# a=[2,3,4,5]
# a[0], a[1]=a[1], a[0]
# print(a)
 
# list=[8,4,2,4,2,3,5,2,1,2,3]
# list.sort()
# print("smallest number", list[0])

# list=[1,2,3,3,9,5,4,4,4]
# list.sort()
# print("smallest number", list[-5])

# for even_numbers in range(2,34,2):
#     print(even_numbers)

# a=[i for i in range(2,18,2)]
# print(a)

# a=[1,2,3,4,5,6,7,8,9,10,12,14,16,18]
# for i in range(len(a)):
#     x=a[1:10:2]
#     b=len(x)
# print(b)

# a=[1,2,-3,-4,5,-5,-6,5,6]
# for i in range(len(a)):
#     x=a[i]
#     if x>0:
#         print(x)

# for i in range(-50,50):
#     if i<=0:
#         print(i)

# a=[1,2,-3,-4,5,-5,-6,5,6]
# for i in range(len(a)):
#     x=a[i]
#     if x>0:
#       print(x)

# a=[11,21,33,44,55,66,77,88,99]
# b=[i for i in range(len(a)) if i%2==0]
# print(b)


# a = [11, 5, 17, 18, 23, 50] 
# # Iterate each element in list
# # and add them in variable total
# for b in a:
#     if b % 2 == 0:
#         a.remove(b)
#         print(a)
 
# printing modified list
# print("New list after removing all even numbers: ", a)

# a=[1,2,3,4,5,6,7,8]
# for b in a:
#     if b%2==0:
#         a.remove(b)
# print(a)

# a=[(),'R',"1",(2,4)]
# b=[]
# for i in range(len(a)):
#     x=a[i]
#     if len(x)>0:
#         b.append(x)
# print(b)


# a=[7,3,4,5,1,5,6,7]
# a.sort()
# print(a)
# print(a[0],"smallest number")

# a=[1,2,3,-3,-4,-5]
# c=[]
# for i in range(len(a)):
#     x=a[i]
#     if x>0:
#         c.append(x)
#         b=len(c)
# print(b)

# # input numbers and get total of these numbers
# a= input("enter your number:")
# c=0
# for i in range(len(a)):
#     c=c+int(a[i])
# print(c)

# GET THE COMMON ELEMENT FROM THE LIST
# a=[1,2,3,4,5]  
# b=[3,4,5,6,7]
# c=[]         
# for i in range(len(a)):
#     x=a[i]
#     for j in range(len(b)):
#         y=a[j]
#         if a[i]==a[j]:
#             c.append(a[i])
# print(c)

# a=input("Enter your number:")
# c=0
# for i in range(len(a)):
#     c=c+int(a[i])
# print(c)

# sum of number of elements in a list
# a=[24,7,8,9,50]
# c=0
# for i in range(len(a)):
#     c=c+a[i]
# print(c)

# remove duplicates number from a list
# a=[4,7,9,4,7,0]
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)

# a=[1,2,3,3,4,5,5,6,7,7]
# b=[]
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(b)


# #reverse the element in a string of list
# a =  ['ritik','sharma','skater']
# b=[]
# for i in range(len(a)):
#     x =  a[i]
#     print(x[::-1])

# a =  ['ritik','sharma','skater']
# b=[]
# for i in range(len(a)):
#     x =  a[i]
#     c=x[::-1]
#     b.append(c)
# print(b)
    
# reverse the string in a list
# a=['raj', 'thakur', 'mehta']
# c=[]
# for i in range(len(a)):
#     x=a[i]
#     b=x[::-1]
#     c.append(b)
# print(c)

# if user enter a number 
# 5=1*2*3*4*5
# 10=ten times
 
# a=input('enter your number:')
# b=int(a)
# c=b+1
# x=1
# for i in range(1,c):
#     x=x*i
# print(x)


# make right angle triangle using for loop
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end="")
#     print("\n")














    






      
      



    
    




        
       
    









   

    









        
        



        
    






        



     
     



       
       
        



            




   
    





      
    











    
   
   

        
        




   

    
    
    





    
    

   
        
    
        
  




    

   
    


    
    
       

        




    



        








        
      


   


    
        
   
        
   
            
            




