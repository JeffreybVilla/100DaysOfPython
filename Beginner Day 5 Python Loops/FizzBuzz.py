#Write your code below this row 👇

#Problem in this logic
#The if, elif statements will stop once it finds 1 statement true

# for number in range(1, 101):
#   if number % 3 == 0:
#     #Divisible by 3
#   elif number % 5 == 0:
#     #Divisible by 5
#   elif number % 3 == 0 and number % 5 == 0:
#     #Divisible by both 3 & 5


#First check if number is divisible by 3 & 5
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
