# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

min_score = 101
for score in student_scores:
    if score <= min_score:
        min_score = score
print(f"The highest score is : {max_score} and the lowest score is : {min_score}")