# my_name_is='Ritik'
# my_name_is_raj="rajesh"
# print(my_name_is)
# MyNameIs='vikas'
# print(MyNameIs)
# a=b=c=d=23
# print(c)
# x,y,z=['a','b','c']
# print(y)
# print(z)
# a='raj'
# print(a)
# b="aman"
# print(b)
# c="this is raj"
# print(c)

# a=2
# b=2
# c=str(a)
# d=str(b)
# e=c+d
# print(e)

# a=str(2)
# b=str(2)
# c=a+b
# print(c)

# a=55
# b=66
# c=88
# d=str(a)
# f=str(c)
# x=d+f
# print(x)

# str1="ekrkr"
# str2="dkfdk"
# c=str1+str2
# print(c)

# str
# a="fhdhvlihdkhvhndhvhdvhnodhnvokhodhnfvohrodhvohndfhnvdhnvhdnhvklndklvkrdfkvnkfnvkrnkvnkrnvkrnfvnkrfnvknrkfnvkrfnvknkfnvknfkvnkfnvknfknvkfkvnkfnkvnkfdnvkfndkvnkfdnvknfdkvnkfnvknfkdnv kfnkvfknvkfnvkfdknvk,fnkvnfknvldknvldnvldnvlnvldnvldnlvndlvnldnvldnvldnlvndlvnldnvkldnvklndlvnldnvkldnvlnvlnvldnlvfndlfnfvfldfnvlnldfnvlkdnvkl"
# print(a)


# a="my name is ritik"
# b=a[-3]
# print(b)

# b="This is the best place to live in"
# b=a[-4]
# print(b)

#string casting
a='2'
b=2
c=str(b)
d=a+c
print(d)
e=int(a)+b
print(e)

#indexing
a="Ritik"
b=a[::]
print(b)

#indexing
a="Ritik"
b=a[1:2:1]
print(b)

#slicing
a="1r1r1r1r"
c=a[0:4:3]
print(c)

#slicing
d="rr1rr1rr1rr1"
e=a[3:5:2]
print(e)

#indexing
a="12R3R4PQR8N23"
b=(a[0],a[1],a[3],a[5],a[9],a[11],a[12])
c=(a[2],a[4],a[6],a[6],a[7], a[8], a[10])
print(b)
print(c)

#indexing
char="dkjj@idl#jdk$jk**&lkfjg"
c=(char[4],char[8],char[12],char[16],char[17])
d=(char[1],char[2],char[3],char[4],char[6],char[7], char[8],char[9],char[10],char[11])
print(c)

#indexing
a="12R3R4PQR8N23"
c=(a[-1],a[-2],a[-4],a[-8],a[-10],a[-12],a[-13])
d=(a[-3],a[-5],a[-6],a[-7],a[-9],a[-11])
print(d)
print(c)

#indexing
a="1 2 3 4 5 5"
c=(a[1],a[3],a[5],a[7],a[9])
print(c)

#slicing
a="22r22r22r22r22r"
b=a[5:9:1]
print(b)

#slicing
a="1R2a3j4"
b=a[1:6:2]
print(b)

#string casting
a="36737"
b=4949
c=4848
d=int(a)
print(b+d)

#string casting
a="36737"
b="38383"
c=48484
d=int(a)
g=int(b)
sum=c+d+g
print(sum)

#slicing
a="mynameisritik"
b=a[ : :-1]
print(b)

a="mynameisritik"
b=a[ 3: 1:-1]
print(b)

a="my name is raj"
c=" "
for i in range(len(a)):
    c=c+a[i]
    if a[i]==" ":
        c=" "
        print(c) 


a="this is raj"
b=a[::-1]
print(b)

#find the index of second same element in a string
a="12345278"
b=a.find("2",2)
print(b)

a="123452728"
b=a.find("2",6)
print(b)


#find the index of second same element in a string
a="12342567"
c=list(a)
b=[]
for i in range(len(c)):
    if c[i]=="2":
        b.append(i)
print(b)


#program to reversing the string
# def string(num):
#     d=num[::-1]
#     return d
# my_string="hello this is Raj"
# print(string(my_string))


#check whether the string is palindrome or not
# string="madam"
# b=string[::-1]
# if b==string:
#     print("string is palindrome")
# else:
#     print("not palindrome")

#program to check whether string is anagrams
# a="this"
# b="isht"
# if sorted(a)==sorted(b):
#     print("a is anagrams")
# else:
#     print("a is not anagrams")

#program to print sum of digits in a string
# a="strin345gj6l7l8"
# count=0
# for i in a:
#     if i.isnumeric():
#         count=count+int(i)
# print(count)

#replace method to convert capital to small and small to capital letters or replace one word with another word

# x="this is raj"
# # z=x.upper()
# # print(z)
# Y=x.replace("i", "H", 2)
# print(Y)

# a=[1,2,3,4,4,5,5,6,7,8,8,9,9,9,9,]
# c=[]
# for i in a:
#     if i not in c:
#         c.append(i)
# print(c)

