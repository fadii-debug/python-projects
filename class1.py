# syntax, comments(descriptions),variable(data store), data types
# string"abc123"
# integer--2,4,6
# float----3.4.5
# boolean-----True, False
new_name="fahad"
age=18
id=3.3
learning=True
city="swabi"
education="fsc"
print("new_name, age, learning, city, education")
# my name is fahad and i am 18 years old having id 3.3
print("my name is", new_name, "and i am", age, "years old having id",id)
# f-string------formatted string
print(f"my name is { new_name } and i am {age} years old.")
# input function, arthematic operators
Name=input(" Enter your name: ")
age=int(input("Enter your age: "))
print("name,age")
num1= int(input( "Enter the number" ))
num2= int(input( "Enter the number " ))
print(f"addition; {num1+num2}")
print(f"division;{num1//num2}")
try: 
    num1=4
    num2=0
    print(num1/num2)
except ZeroDivisionError:
    print("Denomenator can't be zero")    
# assignment operators ==,<,> <=,>=.!=
num=1
num=2
print ( num1==num2)
# loop-------repetitive task 
# for loop------- number of itterations known
# while loop-------number of itteration unknown 
count=0
while count<=10:
    print(count)
    count+=1