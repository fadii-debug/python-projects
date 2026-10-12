# # tuple, exception handling 
# # indexing (slicing), mutable (change)
# # tuple------immutable
# tup1=(1,2,3,4,5,6)
# print(type(tup1))
# # concatination------add
# tup2=(2,4,6,8,)
# print(tup1+tup2)
# # repetition 
# print(tup1*5)


# # tuple destructuring/unpaking
# subject=("python", "jc", "c++")
# # var1=subject[0]
# # var2=subject[1]
# # var3=subject[3]
# var1, var2, var3, =subject
# print(var1, var2)

primary_colors = [("red", "#FF0000"), ("green", "#00FF00"), ("blue", "#0000FF")]
var=primary_colors[0]
print(var)

a,b=var
print(a)
print(b)

try:
    user={
        "name":"fahad"
    }
    print(user["age"])
except KeyError:
    print("Key doesn't exist")    