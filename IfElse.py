# if statements in Python
print("Enter the grade from 0 to 100")
input_grade = input()

grade = int(input_grade)

if 90 <= grade <= 100:
    print("You got an A grade")
elif 80 <= grade <= 89:
    print("You got a B grade")
elif 70 <= grade <= 79:
    print("You got a c grade")
elif 60 <= grade <= 69:
    print("You got a D grade")
elif 0 <= grade <= 59:
    print("You got an F grade")
else:
    print("You entered an invalid grade")