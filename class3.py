# loop-------repetitive task 
# for loop------- number of itterations known
# while loop-------number of itteration unknown 
# count=0
# while count<=10:
#     print(count)
#     count+=1
# for loop
# list 
# name=["ali", "haider", "haseeb", "fahad"]  
# marks=[2,3,4,5,6]  
# for f in marks:
#     print (f+10)
# number=[2,4,7,9,2,7,2,8,7,8]

# # break, continue
# for f in number:
#     if f==7:
#         print(f)
#         break
#     else:
#         print(f)



# number=[2,4,7,9,2,7,2,8,7,8]
# for f in number:
#     if f==7:
#         # print(f)
#         continue
#     else:
#         print(f)



while True: 
    name=input("enter your name:")
    if len(name)<=5:
        print("Enter your name with lenth greater then 5")
        continue
    else:
        print (name)
        break
         

