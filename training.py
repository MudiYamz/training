# string
print("Hello World")

# declare a variable
print("Please input btc donation to the experience:")

Btc = float(input("Btc: "))
print(str(Btc) + "Btc")

first_name = "Big"
is_online = False
print("Lets begin")

# receiving input from user
name = input("What is your name? ")
# string concatenation
print("Hello " + name)

# type conversions
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(age)
# number with decimal point
float()
# converting to boolean
bool()
# converting number to string
str()

int()
float()
bool()
str()

# Program to print the sum of the two numbers
print("Type 4 numbers")
First = float(input("First: "))
Second = float(input("Second: "))
sum = First + Second
print("Sum: " + str(sum))

# alternative way to code above calculation
third = float(input("Third: "))
fourth = float(input("Fourth: "))
sum = third + fourth
print("Sum: " + str(sum))

# cool things to do with strings
course = "Python for beginners"
# methods on the string
print(course.upper())
print("Position of 'y' in sentence: " + str(course.find("y")))
print("Replace 'for' with '4' in sentence: " + str((course.replace("for", "4"))))
print("Python" in course)

# arithmetics augmented assignment operators
x = 10
x += 3
print("If x = 10, what is x plus 3")
print(x)


# (//) will round up your division, (**) raises to the power and (%) gives you the remainder from division
# use parentheses to uphold BOD-MAS math rule

# comparison operators
x = 3 > 2
print("3 > 2")
print(x)
x = 3 == 2
print("3 = 2")
print(x)
x = 3 >= 2
print("3 > or = 2")
print(x)
x = 3 // 2
print("3 / 2 without the change")
print(x)
x = 3 != 2
print("3 is not 2")
print(x)

# the comparison operators are as follows: >, >=, <, <=, ==, !=

# logical operators, 3: and (both), or (at least one), not(if it rejects)
price = 25
print("25 > 10 and < 30")
print(price > 10 and price < 30)

price = 5
print("Inverse the reality of: 5 > 10")
print(not price > 10)

price = 5
print("5 < 3 or > 4")
print(price < 3 or price > 4)

# If statements, elif and else
temperature = 11
temperature = float(input("Temperature: "))
print("If the temperature is ^ Degrees.")
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: #[20, 30]
    print("It's a nice day")
elif temperature > 10: #[10, 20]
    print("It's a cold day")
else:
    print("It's cold")


weight = float(input("Weight: "))
unit = input("(k)g or (l)bs: ")
if unit.lower() == "k":
    converted = weight / 0.45
    print("Weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in kg: " + str(converted))

# while loops
i = 1
while i <= 5:
    print("Rpt 1 to 5")
    print(i)
    i = i + 1

print("1 to 20")
i = 1
while i <= 20:
    print(i)
    i = i + 1

i = 3
while i <= 8:
    print(i * '*')
    i = i + 2


# Lists
print("What are the names of the subjects")
names = ["John", "Mary", "Tom", "Osaze"]
print(names)
print("Change John to Jon")
names[0] = "Jon"
print(names)
print(Make )
print(names[2:3])
print("SUI")