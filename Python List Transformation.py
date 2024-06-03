#Objective: The aim of this assignment is to practice advanced list operations and transformations.

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print(grades)

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.

sum_grades=sum( grades)
grades_average=sum_grades/len(grades)
print (grades_average)

#Task 3: Replace any grade below 80 with the value Failed.

new_grade=[85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
   
for i in range(len(new_grade)):
    
    if new_grade[2] ==78:
        
        new_grade [2] = "Failed"
        
    if new_grade[4] ==76:
        new_grade[4]  = "Failed"
        
    if new_grade[8] ==72:
        new_grade[8] = "Failed"

print (new_grade)
        
        
        
            