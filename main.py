# Output Function
print ('Hello World')

# Input function

# Name =input("Enter your name:")
# FullName=input("Enter your full name:")
# Age=input("Enter your age:")
# School=input("Enter your school name:")
# College=input("Enter your college name:")
# University=input("Enter your university name:")
# FatherName=input("Enter your father name:")
# MotherName=input("Enter your mother name:")
# yourphoneNumber=input("Enter Your Phone Number")

# Variable Practice

# Name = "Anik"
# user="My"
# user1="Name"
# user2="is"
#
# print(user , user1 , user2 , Name)
#
# anikIsBigMan="Who"
# print(anikIsBigMan,"is Big Man?")

# Multiple Assignment
# A,B,C,D=34,40,50,60
# print(A)
# print(B)
# print(C)
# print(D)

# Chained Assignmen

# A=B=C=5000
# print(A)
# print(B)
# print(C)
# print(D)

# String Practice

# String Slicing (Slice from the start)
s= "Welcome to python language with django";
print(s[0:7])
print(s[0:10])

# String Slicing (Slice to the end)

s="Welcome to python language with django";
print(s[7:])
print(s[8:])

# String Slicing (Range)

A=" Sabbir Hossain Anik"
print(A[3:8])
print(A[16:20])

#String Modify
#Upper case

s="Welcome to python language with django"
Name= "Sabbir Hossain Anik"
print(s.upper())
print(Name.upper())

#Lower case

print(s.lower())
print(Name.lower())

# Remove Whitespace

s="Welcome to python language"
print(s.strip())
Name= "  Sabbir Hossain Anik  "
print(Name.strip())

#Replace String

Name= "Sabbir Hossain Anik"
print(Name.replace("Anik","Likhon" ))
print(s.replace("language","language with Django"))

#Split String (List Akare Banano)

s="Welcome to python language with django "
Name= "Sabbir Hossain Anik"
print(Name.split())
print(s.split())

# String Concatention ( String Add kora)


s="Welcome to python language with django "
Name= "Sabbir Hossain Anik"
print(Name,s)

#Count Method (Word koyta ase dekha)

s="Welcome to python language with django "
Name= "Sabbir Hossain Anik"
print(s.count("o"))
print(Name.count("o"))
print(Name.count("Anik"))

#Length Function

s="Welcome to python language with django "
print(len(s))
print(len(Name))
