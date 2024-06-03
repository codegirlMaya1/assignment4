#Objective:The aim of this assignment is to master the art of slicing in Python lists.
#You have a list of daily temperatures for a month, and you'd like to extract specific data from it.
#Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

cal=temperatures

print(cal[7:14])

#Task 2: Extract all the temperatures above 100.

hot_days=temperatures

print (hot_days[23:30])

#Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
cal_dates=temperatures
cal_dates.sort(reverse=True)
print(cal_dates[4:10])

