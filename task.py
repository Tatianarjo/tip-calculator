# #subscripting
# print("hello"[0])
# print("hello"[4])

# #String 
# print("123" + "345")

# #integer = whole number
# print(123 + 456)

# #Large Integers
# print(123_456_789)

# #Float
# print(3.14159)

# #Boolean
# print(True)
# print(False)

# len("hey")
# print(type("hello"))
# print(type(1))

# int("123")

# print(int("123") + int("456"))

# name_of_the_user = input("Enter your name")
# length_of_name = len(name_of_the_user)

# print(type("Number of letters in your name: "))
# print(type(length_of_name))

# print("Number of letters in your name " +str(length_of_name) )

#Mathematical Operations
# print(3 * 3 + 3 / 3 - 3)

# bmi = 84 / 1.65 ** 2
# print(bmi)

# print(int(bmi))
# print(round(bmi))
# print(round(bmi, 2))

# Assignment 

# score = 0
# # User scores a point
# height = 1.8
# is_winning = True
# print(score + int("2"))


# # f-strings
# print(f"Your score is = {score}, your height is {height}. You are winning is{is_winning}")
# print("Your score is " + str(score))

print("Welcome to the tip calculator!")
bill = float(input("what was the total of the bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
# bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
