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
# # total  = 0  
# for i in bill:
#     it_ind =  item_number.index(i)
#     # total+= item_price[it_ind]
#     print(f'your item number is {i} your  item name is {item_name[it_ind]} price  {item_price[it_ind]}')
# # print(f'your toal price is {total} peise dedo bhai')

# item_number=['100','200','300','400','500']
# item_name=['sugar', 'rice', 'potato', 'biscuit', 'colddrink']
# item_price=[40,70,25,20,40]
# bill=[]
# while True:
#     user_number=input("enter your item number or quit with q")
#     if user_number=="q":
#         break
#     if user_number not in item_number:
#         print('enter a valid item number')
#     elif user_number in item_number:
#         bill.append(user_number)
#         total=0
#         for i in bill:
#             indx=item_number.index(i)
#             total=total+item_price[indx]
#             print(f'your item number is {i} and its name is {item_number[indx]} and its price is {item_price[indx]}')
# print(f'your total price is {total}')


# # program to print item details
# item_number =['100', '101', '102', '103', '104']
# item_name =['sugar', 'rice', 'potato', 'biscuit', 'colddrink']
# item_price=[40,70,25,20,40]

# bill=[]
# while True:
#     get_item_number = input('enter your item number or quit with q')
#     if get_item_number=='q':
#         break

#     if get_item_number not in item_number:
#         print('please enter a valid item numbers')
#     elif get_item_number in item_number:
#         bill.append(get_item_number)
#         total=0
#         for i in bill:
#             it_ind=item_number.index(i)
#             total+=item_price[it_ind]
#             print(f'your item number is {i} your item name is {item_name[it_ind]} price{item_price[it_ind]}')
#             gst=total/100*18+total
# print(f'your total price is {gst} paise dedo bhai')



#program to print item details in dictionary
# item_number={
#     "101":{'name':'sugar',
#            'price':100
#            },
#            "102":{"name":"rice",
#                   "price":200},
#                   "103":{"name":"maggie",
#                          "price":200}
# }
# b=[]
# user_number=input("enter your item number:")
# if user_number in item_number:
#     print("your item is", item_number.get(user_number).get('name'), "and its price is", item_number.get(user_number).get('price'))

# a={
#     '101':{'name':'rice',
#            'price':20
#            },
#            '102':{'name':'sugar',
#                   'price':40}        
# }
# user_input=input('enter your item numver')
# if user_input in a:
#     print(f'your item name is {a.get(user_input).get('name')} and its price is {a.get(user_input).get('price')}')


# # program to print item details
# item_number=['5','10','15','20','25','30','34','56','78','90']
# product=['maggie','rice','potato','tomato', 'colddrink', 'pulses', 'wheat', 'shampoo', 'cream','sugar']
# price=[20,40,30,20,30,40,80,70,50,40]

# bill=[]
# while True:
#     get_item_number=input('enter your number:')
#     if get_item_number=='q':
#         break
#     if get_item_number not in item_number:
#         print('please enter a valid item numbers')
#     elif get_item_number in item_number:
#         bill.append(get_item_number)
#         total=0
#         for i in bill:
#             it=item_number.index(i)
#             total+=price[it]
#             print(f'your total price is {i} and your item name is {product[it]} and its price is{price[it]}')
# print(f'your total price is {total}. Make Payment')


# program to print class data
# Roll_No=['1','2','3','4']
# Name=['Raj','Prince','Rohit','Ritik']
# Class=[12,11,11,12]
# Result=[81,88,89,90]
# numbers=[]
# while True:
#     get_roll_no=input('enter your roll no.:')
#     if get_roll_no=='q':
#         break
#     if get_roll_no not in Roll_No:
#         print('Please enter a valid roll no.')
#     elif get_roll_no in Roll_No:
#         numbers.append(get_roll_no)
        
#         for i in numbers:
#             it_ind=Roll_No.index(i)
#             print(f'Student Name {Name[it_ind]} class{Class[it_ind]} Roll No. {i}')
#             print(f'Student Result {Result[it_ind]}')


# # take a input from the user and check we have value or item with the name
# a={
#     'apple': '20',
#     'mango':'30',
#     'banana': '40'
# }


# b=input('enter your key or value:')
# kye_list  =  list(a.keys())

# value_list  =  list(a.values())

# if b in kye_list :
#     # indx =  kye_list.index(b)
#     # print(value_list[indx]) 
#     # print(a[b])
#     print(a.get(b))
  

# elif b in value_list:
#     indx =  value_list.index(b)
#     print(kye_list[indx])

     
# else:
#     print('no')

#take a input from the user and check we have a value or item with the name
# fruits={
#         "apple":'20',
#         'mango':'30',
#         'grapes':'40'
#     }
# b=list(fruits.keys())
# c=list(fruits.values())

# user_input=input('enter your number:')
# if user_input in b:
#     print(fruits.get(user_input))
# elif user_input in c:
#     indx=c.index(user_input)
#     print(b[indx])
# else:
#     print('no')



# #take a input from the user and check we have a value or item with the name
# grocerry={
#     'sugar':30,
#     'salt':50,
#     'rice':60,
#     'wheat':90
# }
# keys_list=list(grocerry.keys())
# values_list=list(grocerry.values())
# user_input=input('enter your item name or item value:')
# if user_input.isnumeric():
#     user_input =  int(user_input)
# if user_input in keys_list:
#     # print(grocerry.get(user_input))
#     indx=keys_list.index(user_input)
#     print(values_list[indx])
# elif user_input in values_list:
#     indx=values_list.index(user_input)
#     print(keys_list[indx])
# else:
#     print('your item or value is not found')

# # take a input from the user and check we have value or item with the name
# a={
#         'apple':'20',
#         'mango':'30',
#         'grapes':'40'
#     }
# b=input('enter your number:')

# c=list(a.keys())
# d=list(a.values())
# if b in c:
#     print(a.get(b))
# elif b in d:
#     int_indx=d.index(b)
#     print(c[int_indx])

# else:
#     print('not found')
    


# # take a input from the user and check we have value or item with the name
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


# # program if entered value is not present than update it in a dictionary
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

#program if entered value is not present than update it in a dictionary
# items={
#     'apple': '20',
#     'mango':'30',
#     'banana': '40'
# }
# user_input=input('enter your item:')
# if user_input in items:
#     print(items.get(user_input))
# else:
#     user_value=input('enter the required value:')
#     items.update({user_input:user_value})
# print(items)

#nested dictionary program
# a ={
#     '101': {
#                 'name':'cold drink',
#                 'price':20
#             },
#     '102':{
#                 'name':'sugar',
#                 'price':200
#             },
# }
# user_input=input('enter the value:')
# if user_input in a:
#     print(f'{a.get(user_input).get('name')} and {a.get(user_input).get('price')}')


# # nested dictionary program
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


# a  ={
#     'name':'ramesh',
#     'age':20,
#     'city':'hyderabad',
#     'hobbies':['reading','painting'],
#     'address':{
#         'house_no':123,
#         'road':'abc',
#         'city':'hyderabad',
#         'pin_code':500001
#     }
# }


# homework print duplicates value how many times
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


# a={
#     'sugar':50,
#     'salt':70,
#     'rice':80,
#     'wheat':90,
#     'pu3lses':70,
#     'pulse7s':70,
#     'prtru3elses':70,
#     'pu3lsrees':70,
#     'pu3erlreses':70,
#     'purerrer3lses':70,
#     'pu3rerlses':70,
#     'pu3lsuues':70,
#     'macroni':80

# }
# d=list(a.values())

# l={}
   
# for i in range(len(d)):
#     n=d[i]
#     m=d.count(d[i])
#     k=l.setdefault(d[i],m)
# print(l)

# program to print duplicate values occur how many times
# a={
#     'sugar':50,
#     'salt':70,
#     'rice':80,
#     'wheat':90,
#     'pu3lses':70,
#     'pulse7s':70,
#     'prtru3elses':70,
#     'pu3lsrees':70,
#     'pu3erlreses':70,
#     'purerrer3lses':70,
#     'pu3rerlses':70,
#     'pu3lsuues':70,
#     'macroni':80

# }
# d=list(a.values())
# l={}
# for i in range(len(d)):
#     n=d[i]
#     m=d.count(d[i])
#     if m>1:
#         l.setdefault(d[i],m)
# print(l)


# b={
#     'sugar':50,
#     'salt':70,
#     'rice':80,
#     'wheat':90,
#     'pu3lses':70,
#     'pulse7s':70,
#     'prtru3elses':70,
#     'pu3lsrees':70,
#     'pu3erlreses':70,
#     'purerrer3lses':70,
#     'pu3rerlses':70,
#     'pu3lsuues':70,
#     'macroni':80

# }
# d=list(b.values())
# e={}
# for i in range(len(d)):
#     x=d[i]
#     count=d.count(x)
#     e.setdefault(x,count)
# print(e)
#     if count>1:
#         e.setdefault(x,count)
# print(e)

    

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





        


     
      
#         f=f+y
# print(d)
# print(f)



        



# a={
    # 'ramesh':50,
    # "rajat":60,
    # "kamlesh":40,
    # "rajesh":50,
    # "suresh":40
# }
# d=a.values()
# print(d)
  

    



# { '1':2,'2':3,'3':}
# home work 





# a = { '101': {'name':'lagel','price':20}}




# b  = '101'  input leke kerna hai 


# print(a.get(b).get('name'))

#python program to make simple calculator
# a=int(input('enter first numbedr:'))
# b=int(input('enter second number'))
# c=(input('enter the operation you want to perform'))
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="/":
#     print(a/b)
# elif c=="%":
#     print(a%b)
# elif c=="^":
#     print(a**b)

# a=int(input('enter no. '))
# b=int(input('enter no.'))
# c=input('enter the operation you want to perform')
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=='*':
#     print(a*b)
# elif c=="/":
#     print(a/b)
# elif c=="%":
#     print(a%b)



        








































# # # nested dictionary statement
# # a={
# #     '101':{
# #         'name':'cold drink',
# #         'price':20
# #     },
# #     '102':{'name':'sugar',
# #            'price':200},
    
# # }

# # print(a.get('101').get('name'))
# # print(a.get('102'))




 



            

        
  





# # a=['apple', 'banana', 'cherry']
# # x=a.index('banana')
# # print(x)

# # a=['apple', 'banana', 'cherry']
# # b=[1,2,3,4,5,6,7]
# # c=0
# # x=a.index('banana')
# # c+=b[x]
# # print(f'your item is {b[x]} your item name is {a[x]}')




        


        


# import dictionary


# print(dictionary.ritik,'----------------------------------------------------')


# print(dictionary.raffi,'----------------------------------------------------')