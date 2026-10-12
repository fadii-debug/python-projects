# simple quiz app


score = 0

answer = input("1. What is the capital of pakistan? ")
if answer.lower() == "Islamabad":
    print("okk!")
    score = score + 1

else:
    print("Wrong! Answer is Islamabad")

answer = input("2.  5+3")
if answer == "8":
    print("right")
    score = score + 1
else:
    print("wrong! answer is 8")

answer == input("3. whtat is python? (language/jarwer)")
if answer.lower() == "language":
    print("Right!")
    score = score + 1
else:
    print("wrong! answer is language")
print("Quiz finished! your score:", score, "/3")