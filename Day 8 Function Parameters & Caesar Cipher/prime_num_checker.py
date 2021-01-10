#Write your code below this line 👇
#Prime number is only divisible by 1 and itself.
#EX: 7
#If any of these = 0 as remainder, then it is not a prime #
#Elif all of these have remainder, then it is a prime #
# 7 / 2 =
# 7 / 3 = 
# 7 / 4 = 
# 7 / 5 = 
# 7 / 6 =


#Checks all numbers starting from 2 to input num
#If divisible by any of the numbers, then not a prime #
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            #not a prime #
            is_prime = False
    if is_prime:
        print(f"\n{number} Is a prime number.")
    else:
        print(f"\n{number} Is not a prime number.")      
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
