bolLoop = True

while bolLoop:
    print("1. Science Fiction")
    print("2. Computers and Technology")
    print("3. Cooking")
    print("4. Business")
    print("5. Comics")
    print("6. Exit")

    print("Which category do you choose?")
    input_category = input()
    category = int(input_category)

    if category == 1:
        print("Science Fiction is a futuristic choice!")
    elif category == 2:
        print("Computers and Technology is a techy choice!")
    elif category == 3:
        print("Cooking is a delicious choice!")
    elif category == 4:
        print("Business is a smart choice!")
    elif category == 5:
        print("Comics is a nerdy choice!")
    elif category == 6:
        print("Exiting the program.")
        break
    else:
        print("You selected an invalid number")

    print()
    print()
