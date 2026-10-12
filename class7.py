# local variable-----global variable

x=10      #global

def greet():
    global y
    y=3    #local
    print(x)
    print(y)

greet()
print(x)
print(y)




# dictionaries-----data store, key-value pair
# list-----data store, indexing-value
# key-----unique
user={
    "name":"fahad",
    "age":18,
    "id":3.2
}
print(user)
print(user["name"])


# subject={
#     "maths":"beta",
#     "marks":89,
#     "percentage":85
# }
# print(subject)
# print(subject["maths"])

# add, update, delete
# add
user["email"]="abc@gmail.com"
# update
user["name"]="fadii"
# del
del user["id"]
print(user)