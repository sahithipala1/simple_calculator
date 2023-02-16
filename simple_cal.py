counter = 0
while True:
    answer = int(input("enter a number: "))
    print("Adding it up")
    counter += answer
    print("current total is:", counter)
    add_another = input("Add another? :")

    if add_another == "no":
        break
print("Bye!")
