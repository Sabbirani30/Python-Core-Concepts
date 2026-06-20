Firstlist = [1,2,3,4,5,6,7,8,9,10]
print(Firstlist)
print(type(Firstlist))

secondlist = ["anik","Anik","Sabbir","Anki","Likhon",1,2,3,4,5,6,7,8,9,10]
print(secondlist)
print(type(secondlist))
print(secondlist[0])
print((secondlist[6]))

Thirdlist = [1,2,3,4,5,6,7,8,9,10]
print(Thirdlist)
print(type(Thirdlist))
print(Thirdlist[0])

Course=["Machine Learning","Django","FastApi","Python","RestApi"]
print(Course)
print(len(Course))  #The length of a list is measured using the len() function. (length Mapa hoy)
print(Course[2]) # Access List (Nirdishto kono item dekhte chaile eivabe lekhte hoy)
print(Course[:5]) # Range Of Index ( Range nirdharon kora hoy , koto Numer index theke koto number porjonto dekha jabe)
print(Course[0:3])


Business=["Chips","Noodles", "Ice-cream","Drinks",]
print(Business)
print(type(Business))
print(Business[3])
print(Business[:3])
print(Business[::2]) #(Start,Stop,Step)
print(Business[-1]) # Range of Negative Indexes ( Pichon theke Shamne ashe)

SchoolName=["Monipur","Bangabandhu","Sher-E-Bangla","Mohammadpur Govt." ,294,299,298,314]
print(SchoolName)
print(type(SchoolName))
print(SchoolName[2])
print(SchoolName[3])
print(SchoolName[2:])
print(SchoolName[0:2])
print(SchoolName[-7:-3])

CollegeName=["Dhaka" , "Dhanmondi Ideal", "Mirpur Girls" , "BAF", "Adamjee" ,10,11,12,13,14,]
print(CollegeName)
print(type(CollegeName))
print(CollegeName[0])
print(CollegeName[1])
print(CollegeName[2])
print(CollegeName[0:])
print(CollegeName[0::2])
print(CollegeName[-5:-1])
print(CollegeName[-3:])
print(CollegeName[:-1])
print(CollegeName[-1:])

#Item Change
CollegeName=["Dhaka" , "Dhanmondi Ideal", "Mirpur Girls" , "BAF", "Adamjee" ,10,11,12,13,14,]
CollegeName[0]="Mirpur"
CollegeName[3]="National"
print(CollegeName)

#Insert Function
Business=["Chips","Noodles", "Ice-cream","Drinks",]
Business.insert(2,"Motijeel Ideal")
print(Business)
Business.insert(0,"Potato")
print(Business)
Business.insert(1,"Juice")
print(Business)

#Append Function: (New Item Add)
Business=["Chips","Noodles", "Ice-cream","Drinks",]
Business.append("Potato")
print(Business)

#Remove Function
Course=["Machine Learning","Django","FastApi","Python","RestApi"]
Course.remove("RestApi")
print(Course)

#Pop() Function:
List=["Banana","Mango","Apple"]
List.pop()
print(List)
List.pop(0)
print(List)

# del Keyword:
List=["Banana","Mango","Apple"]
del List[0]
print(List)

#Clear() Function:
List=["Banana","Mango","Apple"]
List.clear()
print(List)

#Sort() Function:
Alphabetic=["Django","HTML","CSS","Java","Python"]
Alphabetic.sort()
print(Alphabetic)






