# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆

# sum_of_hight = sum(student_heights)
# number_of_student =len(student_heights)
# average_hight = round(sum_of_hight/number_of_student,2)
# print(average_hight)

sum_hight = 0
for hight in student_heights:
    sum_hight+=hight
print(sum_hight)

number_students = 0
for student in student_heights:
    number_students+=1
print(number_students)
average = sum_hight/number_students
print(average)
#Write your code below this row 👇
