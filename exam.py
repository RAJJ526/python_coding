# a = {
#     '1': {
#         'question-1': "pm of indai",
#         'answer':'a',
#         'options': {
#             'a':'nm',
#             'b' : 'raj',
#             'c' : 'ritik',
#             'd' : 'brij',
#         }
    
# }


# a={
#     '1':{
#         "question":
#             "Who is the president of India?"
#             "\n"

#             '(a)-amitabh bachan' "\n" '(b)-draupdi murmu' "\n" '(c)-narendra modi' "\n" '(d)-ramnath kovind'
#     ,
#     "answer":"b",},
#     '2':{
#         "question":
#             "What is the name of the weak zone of the earth's crust?"
#             "\n"

#             '(a)-Seismic' "\n" '(b)-Cosmic' "\n" '(c)-Formic' "\n" '(d)-Anaemic'
#     ,
#     "answer":"a",},
#     '3':{
#         "question":
#             "Where was India\'s first national Museum?"
#             "\n"
#             '(a)-Delhi' "\n" '(b)-Hyderabad' "\n" '(c)-Rajasthan' "\n" '(d)-Mumbai'
#     ,
#     "answer":"d",},
# }

# b=0
# total = 0
# while b<3:
#     user_input=input('enter the question')
#     if user_input in a:
#         print(a.get(user_input).get("question"))
#         new_val=input("choose the correct answer")
#         z=a.get(user_input).get('answer')
#         if new_val==z:
#             print("your answer is correct ")
#             total=total+1
#         else:
#             print('your answer is incorrect')
#             total= total-0.5
#         b=b+1
# print(total)

#program to find percentage of value and then add it
# amount=int(input("enter the amount"))
# percent=int(input("what percent you want of the amount"))
# percentage=amount/100*percent
# add=amount+percentage
# print(percentage)
# print(f'your amount is {amount} and you get {add} amount of money with {percent} percent gst')

# amount=int(input("enter the amount "))
# percent=int(input('what percent you want '))
# percentage=amount/100*percent
# total=amount+percentage
# print(f'your total amount is {total} with {percent} percent gst')

# #find the age

# # percentage 
# # find the age 

# function intro

# def add(a,b,c):
#     print(a+b+c)

# add(2,3,5)
# add(23,33,5)
# add(32,33,5)
# add(42,34,5)
# add(24,43,9)

# function without param



# def add():
#     a  =input("i")
#     v  = input("v")
#     print(a+v)

# add()
# add()
# add()
# add()
# add()
# add()
# add()
# add()
# add()
# add()
# add()
# add()


# def nrij(name , age, last):
#     print(f'my name is {name } {last} anfa ge is  {age}')


# nrij(name='rityi',last = 'shar,a', age  = 24) 

# a =  0
# while a < 10:
#     if a == 5:
#         a=a+1
#         continue
#     print(a, end='\n')
#     a = a + 1


# a = {'a':50, 'b':50, 'c':50, 'd':50, 'e':70, 'f':50, 'g':50, 'h':70}
# h = {}
# b  =  list(a.values())
# for i   in range(len(b)):
#     x = b.count(b[i])
#     h.setdefault(b[i],x)
# print(h)

# a= {}
# b={}


# a.setdefault('a',20)


# print(a)

