# Temoerature converter

print("1. celsius to fahrenheit")
print("2. fahrenheit to celsius")

choice = input("write number")

if choice == "1":
    c = float(input("write celsius"))
    f = (c * 9/5) + 32
    print("Fahrenheit =", c)

else:
    print("wrong answer")