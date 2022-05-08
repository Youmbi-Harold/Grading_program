student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}#initialising an empty dictionary 
#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores: #to treat each case in student_score dictionary I used the for loop with a key which signifies the students in student_score
  if student_scores[key] >= 91:#comparing the mark with a standard grading system
    student_grades[key] = "Outstanding"
  elif student_scores[key] >= 81 and  student_scores[key]<= 90:
    student_grades[key] =  "Exceeds Expectations"#and adding a new key to the student_grades dictionary
  elif student_scores[key] >= 71 and student_scores[key]<= 80:
    student_grades[key] =  "Acceptable"
  elif student_scores[key] <= 70:
    student_grades[key] =  "Fail"    
  
# 🚨 Don't change the code below 👇
print(student_grades)# prints the dictionary





