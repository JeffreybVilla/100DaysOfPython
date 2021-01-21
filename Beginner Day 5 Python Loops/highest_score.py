# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
#NOT allowed to use max or min functions
# print(f"\nHighest student score is {max(student_scores)}")
# print(f"\nLowest student score is {min(student_scores)}")


#if current score is greater than highest score
#set highest score = to the greatest current score
#loop until all scores are checked inside student_scores list
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"\n\nThe highest score is {highest_score}")


