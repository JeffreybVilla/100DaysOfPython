"""
Carl Gauss exercise
1 + 2 + 3 + 5 + ... 96 + 97 + 98 + 99 + 100
flip numbers around
100 + 99 + 98 + 97 + 96 ... + 5 + 4 + 3 + 2 + 1


100 + 1 = 101
99 + 2 = 101
98 + 3 = 101
97 + 4 = 101
96 + 5 = 101

There is 50 pairs of 101
50*101 = 5050
"""



#Add up all numbers from 1 to 100
#Add will add every number in this range to sum
#starting from 0
sum = 0
for number in range(1, 101):
    sum += number
print(sum)
