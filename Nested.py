print("Enter your number between 1 and 10")

input_value = input()
internal_number = int(input_value)
generated_number = internal_number // 2

if 1 <= internal_number <= 10:
    for i in range(1, internal_number + 1):
        print("The outer loop value is:", i)
        for j in range (1, generated_number + 1):
            print("The inner loop value is:", j)
        print()

else:
    print("You entered an invalid number")