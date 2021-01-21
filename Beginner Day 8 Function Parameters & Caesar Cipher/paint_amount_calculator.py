#Write your code below this line 👇
import math


#Parameters are width, height, cover.
def paint_calc(width, height, cover):
    area = width * height
    num_cans = math.ceil(area / cover)
    print(f"You'll need {num_cans} cans of paint.")




#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_w = int(input("Width of wall: "))
test_h = int(input("Height of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
