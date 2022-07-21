# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
# Выполнить подсчет средней величины дохода сотрудников.
import os,sys

with open(os.path.join(sys.path[0],"Task3.txt"), "r", encoding="utf-8") as file:  # Open file
    lines = file.read().splitlines()                            # Read contents and remove \n

dicts = {}
for i in lines:                                                 # Iterate through each line
    i = i.split()                                               # Convert each line to a list
    dicts[i[0]] = float(i[1])                                   # Create a dictionary from last name and salary
    if float(i[1]) < 20000:                                     # Check if salary is less than 20 000
        print(f"{i[0]} has salary less than 20000")             # Print last name if salary is less than 20000


total_salary = 0                                                # Variable to calculate total salary
for item in dicts:                                              # Iterate through each dictionary                                      
    total_salary += dicts[item]                                 # Add salary to total amount

average_salary = total_salary / len(dicts)                      # Divide total amount by number of employees
print(f"Average salary is {average_salary}")