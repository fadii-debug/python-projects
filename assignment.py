# car={
#     "brand":"BMW",
#     "model":"M5",
#     "year":2026
# }
# print(car)
# print(car["brand"])
# # add
# car["colour"]="black"
# # update
# car["year"]=2020
# print(car)

user={
    "name":"fahad",
    "age":18,
    "id":3.8
}
# loop on dictionaries
# keys, values, key-value-pair
# key
for i in user:
    print(i)

# values
for i in user.values():
    print(i)

# key-value-pair
for i, j in user.items():
    print(f"{i}. {j}")        
