# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
# str.split(',') method converts string into a list
# EX: use commas
# str_input = "Hello, from, AskPython"
# operation = str_input.split(",")
# print(str_input)


# Prints second name in list
# print(names[1])


# Prints total # of items in list
# print(len(names))

num_people = len(names)

# generate random #s b/w 0 and last index
roulette = random.randint(0, num_people - 1)

person_who_will_pay = names[roulette]

print(person_who_will_pay + " is going to pay for everyone's meal today.")




# Could also just use random.choice
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to pay for everyone's meal today.")
