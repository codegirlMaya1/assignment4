#Objective:The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

new_list1= set(submitted)
new_list2= set(attended)

result= set(submitted) & set(attended)
print (list(result))

#Task 2: Check if the two lists are identical in terms of their content, regardless of order.

submitted.sort()
attended.sort()

print(submitted==attended)

#Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

attended.remove("Eve") 
attended.remove("Frank")
print(attended)