# a='ritik'
# y=a.capitalize()
# print(y)
      
# a="banana"
# b=a.center(60)  
# print(b)    

# a="this is my friend my friend is very good"
# b=a.count("frien")
# print(b)

# a="My name is Stale"
# b=a.encode()
# print(b)

# a="hello this is raj"
# b=a.endswith("r")
# print(b)

# a="my\tname\tis\traj"
# b=a.expandtabs(7)
# print(b)

# a="my name is raj"
# b=a.find("name")
# print(b)

# a="the price of my computer is {cost: 5f}"
# b=a.format(cost=78)
# print(b)

# a="here is raj"
# print(a.index("is"))

# a="33343jkj"
# b=a.isalnum()
# print(b)

# a="fdkfk11fk"
# b=a.isalpha()
# print(b)

# a="fdkfk11fk323232#$%^"
# b=a.isascii()
# print(b)

# a="293939fjf"
# b=a.isdecimal()
# print(b)

# a="8888"
# b=a.isdigit()
# print(b)

# a="my name is raj"
# c=" "
# for i in range(len(a)):
#     c=c+a[i]
#     if a[i]==" ":
#         c= ''
#         print(c) 

# a={'Rohit':'rr', 'raj': 'beat', 'akash':'maruti', 'aman':'dkd'}
# b=a.keys()
# c=a.items()
# h=a.values()
# l=a.get("rahul", "not found")
# a.update({"ritik": "verna"})

# print(l)
# print(h)
# print(c)
# print(b)
# print(a)


# a={'brij':'mca','rohan':'bca','raj':'btech','ashish':'mba'}
# b=a.keys()
# c=a.items()
# g=a.values()
# h=a['raj']
# print(b)
# print(c)
# print(g)
# print(h)


# x={'Rohit':'audi', 'neha':'mercedes', 'jack':'range rover', 'aman':'verna'}
# x.update({'rohan':'maruti'})
# print(x)

# x={'Rohit':'audi', 'neha':'mercedes', 'jack':'range rover', 'aman':'verna'}
# x.clear()
# print(x)

# x={'Rohit':'audi', 'neha':'mercedes', 'jack':'range rover', 'aman':'verna'}
# y=x.copy()
# print(x)

# x={"key1", "key2", "key3", "key4"}
# y=0
# z=dict.fromkeys(x,y)
# print(z)

# update method in dictionary
# car={
#     'brand':'ford',
#     'model':'mustang',
#     'year':'1994'

# }
# car.update({'color':'white'})
# print(car)

# fromkeys method in dictionary
# x={'key1', 'key2', 'key3'}
# y=7
# z=dict.fromkeys(x,y)
# print(z)

# get method in dictionary
# car={
#     'brand':'ford',
#     'model':'mustang',
#     '87':'1994'

# }
# y='87'
# z=car.get(y)
# print(z)

#setdefault method
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("year")

# print(x)



# x={'Rohit':'audi', 'neha':'mercedes', 'jack':'range rover', 'aman':'verna'}
# x.pop('Rohit')
# print(x)

# x={'Rohit':'audi', 'neha':'mercedes', 'jack':'range rover', 'aman':'verna'}
# x.popitem()
# print(x)

# x={'Rohit':'audi', 'neha':'mercedes', 'jack':'range rover', 'aman':'verna'}
# y=x.setdefault("Rohit")
# print(y)

#get method in python
# a={
#     'raj':'mca', 
#     'neha':'bca',
#     'aman':'btech',}

# b=a.get("ashish",'not found')
# print(b)

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


# for i in range(1,100):
#     a={108:'[maggie - 20]', 109:'[rice - 100]', 110:'[potato - 50]', 111:'biscuit - 60'}
#     input_number=input('enter your number:')
#     int_input_number=int(input_number)
#     y=a.setdefault(int(input_number))
#     print(y)



# take a input from the user and check we have value or item with the name
# a={
#     'apple': '20',
#     'mango':'30',
#     'banana': '40'
# }
# b=input('enter your key or value:')
# kye_list  =  list(a.keys())
# value_list  =  list(a.values())
# if b in kye_list :
#     indx =  kye_list.index(b)
#     print(value_list[indx]) 
#     print(a[b])
#     print(a.get(b))
# elif b in value_list:
#     indx =  value_list.index(b)
#     print(kye_list[indx]) 
# else:
#     print('no')


# a={
#     'apple': '20',
#     'mango':'30',
#     'banana': '40'
# }
# b=input("enter your number or value:")
# key_list=list(a.keys())
# value_list=list(a.values())
# if b in key_list:
#     indexi=key_list.index(b)
#     print(value_list[indexi])
# elif b in value_list:
#     indexi=value_list.index(b)
#     print(key_list[indexi])
# else:
#     print("not found")

# a={
#     'apple': 20,
#     'mango':30,
#     'banana': 40
# }
# value_list=list(a.values())
# print(value_list)
# a={
#     'apple':'50',
#     'banana':'60',
#     'grapes':'30',
# }
# b=list(a.keys())
# c=list(a.values())
# user_input=input('enter fruit name:')

# if user_input in b:
#   # indxi=b.index(user_input)
#   # print(c[indxi])
#   print(a.get(user_input))
# elif user_input in c:
#   indxi=c.index(user_input)
#   print(b[indxi])
# else:
#   print('not found')


# take a input from the user and check we have value or item with the name
# a={
#  "cold drink":"100",
#  "hot drink":"300",
#  "coffee":"400",
#  "tea":"350"
# }

# key_list=list(a.keys())
# values_list=list(a.values())

# user_input=input('enter fruit name')
# if user_input in key_list:
#   print(a.get(user_input))
# elif user_input in values_list:
#   indxi=values_list.index(user_input)
#   print(key_list[indxi])
# else:
#   print('not found')



# enter the name to check value and also update value if not any
# a={
#     'apple': '20',
#     'mango':'30',
#     'banana': '40'
# }

# user_input  =  input('enter fruit name ')

# if user_input in a:
#     print(' yees we have and price is ' ,a.get(user_input) )
# else:
#     new_val = input('we dont have any value plzz enter value ')
#     a.update({user_input:new_val})

# print(a)

# enter the name to check value and also update value if not any
# a={
#     'apple':'20',
#     'mango':'30',
#     'banana':'40'
# }
# user_input=input('enter fruit name:')
# if user_input in a:
#     print('yes we have this item and its price is ',a.get(user_input))
# else:
#     new_val=input('we dont have any value please enter value')
#     a.update({user_input:new_val})
# print(a)


# a ={
#     '101': {
#                 'name':'cold drink',
#                 'price':20
#             },
#     '102':{
#                 'name':'suger',
#                 'price':200
#             },
# }

# print(a.get('101').get('name'))
# print(a.get('101').get('price')+ a.get('102').get('price'))


#nested dictionary
# a={
#     "101":{
#         'name':'cold drink',
#         'price':20
#     },
#     "102":{'name':'soda',
#           'price':40 }
    
# }

# print(a.get("101").get('price')+a.get('102').get('price'))


#print duplicate values and add duplicates values of a set
# a={
#     'ramesh':70,
#     'ganesh':50,
#     'suresh':70,
#     'mahesgh':70,
#     'surefh':50,
# }
# b=list(a.values())
# d=0
# c=[]
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
#     else:
#         d=d+b[i]
#         print(b[i],'is duplicate')
# print(d)

#print duplicate values and add duplicates values of a set
# a={
#     'ramesh':70,
#     'suresh':90,
#     'rishav':90,
#     'keshav':80,
#     'kamlesh':70
    
# }
# b=list(a.values())
# c=[]
# d=0
# for i in range(len(b)):
#     x=b[i]
#     if b[i] not in c:
#         c.append(b[i])
#     else:
#         d=d+b[i]
#         print(b[i])
# print(d)

#print sum of values in dictionary
# a={
#     "ramesh":50,
#     "suresh":80,
#     "rajesh":90
# }
# c=0
# for i in a:
#     c=c+a[i]
# print(c)
        


# # print sum of values in a dictionary
# a={
#     'ramesh':70,
#     'ganesh':50,
#     'gandfdsfesh':70,

# }
# c=0
# for i in a:
#     c+=a[i]
# print(c)

# # setdefault method
# a={'raj':'audi','rohan':'swift'}
# a.setdefault('raj','null')
# print(a)

# #print duplicates value in dictionary and how many times it come
# a ={
#     "a":1,
#     "b":1,
#     "c":2,
#     "d":3,
#     "e":2,
#     "f":2,
#     "k":3
# }

# c=[]
# d=[]
# z={}
# f=0
# x=list(a.values())

# for i in range(len(x)):
#     y=x[i]
#     if y not in c:
#         c.append(y)
#     elif y not in d:
#         d.append(y)
#         for i in range(len(d)):
#             m=x.count(d[i])
#             n=z.setdefault(d[i],m)
# print(z)
# print(d)

# a={
#     "a":1,
#     "b":2,
#     "c":7,
#     "d":2,
#     "e":9,
#     "f":7,
# }
# c=[]
# d=[]
# h=0

# z=list(a.values())
# for i in range(len(z)):
#     x=z[i]
#     if x not in c:
#         c.append(x)
#     elif x not in d:
#         d.append(x)
#         h=h+x
# print(h)


#program to sort dictionary
# a={
#     "kamlesh":1,
#     "ajay":2,
#     "rajesh":7,
#     "arun":2,
#     "ely":9,
#     "chirstian":7,
# }
# d=list(a.items())
# d.sort()
# c=dict(d)
# print(c)

# a={
#     "a":20,
#     "b":30,
#     "c":40,
#     "d":50,
#     "q":90
# }
# if "q" in a:
#     print(a["d"])
# else:
#     print("Key not found")



#python program to handle missing keys in dictionaries
# country_code = {'India' : '0091',
#                 'Australia' : '0025',
#                 'Nepal' : '00977'}
 
# # search dictionary for country code of India
# print(country_code.get('India', 'Not Found'))
 
# # search dictionary for country code of Japan
# print(country_code.get('Japan', 'Not Found'))

# a={
#     "ramesh":60,
#     "suresh":90,
# }
# print(a.get('ramesh', 'nor found'))
# print(a.get('rajesh',"not found"))

# dict = {}
 
# # Insert first triplet in dictionary
# x, y, z = 10, 20, 30
# dict[x, y, z] = x + y - z;
 
# # Insert second triplet in dictionary
# x, y, z = 5, 2, 4
# dict[x, y, z] = x + y - z;
 
# print the dictionary
# print(dict)

#program to print multiple keys and values
# a={}
# x=20
# y=60
# a[x,y]=80,90
# a[y]=90
# print(a)

#sum of all items in a dictionary
# a={
#     "ramesh":60,
#     "suresh":90,
#     "kamlesh":40
# }
# c=0
# for i in a:
#     c=c+a[i]
# print(c)

# import sys
# my_dict = {"apple": 1, "banana": 2, "cherry": 3}
# size = sys.getsizeof(my_dict)
# print("Size of dictionary:", size, "bytes")

#get size of the dictionary
# import sys
# a={
#     "apple":10,
#     "banana":30,
#     "cherry":40
# }
# b=sys.getsizeof(a)
# print("size of dictionary",b)

# item_number=['12','13','15','16','17']
# item_name=['rice','wheat','fruits','vegetables','sweets']
# item_price=[12,34,56,67,77]
# b=[]
# while True:
#     user_input=input('enter item number:')
#     if user_input=='q':
#         break
#     if user_input not in item_number:
#         print('enter a valid item number')
#     elif user_input in item_number:
#         b.append(user_input)
#         total=0
#         for i in b:
#             indx=item_number.index(i)
#             total+=item_price[indx]
#             print(f'your item number is {i} and item name is {item_name[indx]} and its item price is {item_price[indx]}')
# print(f'your total price is {total}')


#real program of count  elements in a dictionary
# a={
#     'ramesh':30,
#     'anita':40,
#     'mohit':60,
#     'ankita':90,
#     'mukesh':60,
#     'aryan':40,
#     'suresh':40,
# }
# x=list(a.values())
# c=[]
# d=[]
# u={}
# for i in range(len(x)):
#     y=x[i]
#     if y not in c:
#         c.append(y)
#     elif y not in d:
#         d.append(y)
        
#         for i in range(len(d)):
#             n=d[i]
#             m=x.count(d[i])
#             g=u.setdefault(n,m)
# print(u)


# accurate program to print count of duplicate elements in a dictionary 
# a={
#     'ramesh':'30',
#     'anita':'40',
#     'mohit':'60',
#     'ankita':'90',
#     'mukesh':'60',
#     'aryan':'40',
#     'suresh':'40',
#     'suresh':'40',
# }
# d=list(a.values())
# l={}
# for i in range(len(d)):
#     n=d[i]
#     m=d.count(d[i])
# print(m)
# if m>1:
#     l.setdefault(d[i],m)
# print(l)


# get values by using while loops
# a={
#     "apple":'40',
#     "banana":'50',
#     "grapes":'60'
# }
# b=list(a.values())
# c=list(a.keys())

# while True:
   
#    user_input=input("enter user input")

#    if user_input in c:

#     print(a.get(user_input))
   
#    elif user_input in b:
#     indx=b.index(user_input)
#     print(c[indx])
   
#    else:
#     print("not found")


#dictionary important property
# item={"sbi-101":100,"sbi-102":200,"sbi-103":300,"sbi-104":400}
# if "sbi-101" in item:
#     item["sbi-103"]=item["sbi-103"]+20
# print(item) 



























































    







 








        


 


    
       
  



   










