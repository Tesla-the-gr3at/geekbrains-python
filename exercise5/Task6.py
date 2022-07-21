# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
import os,sys

file = open(os.path.join(sys.path[0], "Task6.txt"), "r", encoding="utf8")   # Open the file
lines = file.read().splitlines()                                            # store lines in a list
file.close()                                                                # Close the file

result = {}                                                                 # Variable to store end result
for line in lines:                                                          # Go through each line in the file
    line = line.split(":")                                                  # Use : as splitter for new list
    lections_types = line[1].split()                                        # Store each lection hours as a separate list item
    total_hours = 0                                                         # Total hours for the lesson

    for lection_type in lections_types:                                     # Go through each type of lection (lab, lesson, practice)
        hours = 0                                                           # hours for lab, lesson or practice
        hours_str = ""                                                      # variable to store temporary hours as string

        for character in lection_type.strip():                              # for each cahracter in the lection
            if character.isnumeric():                                       # Check if character is a figure
                hours_str += character                                      # if yes, add to hours_str

        if hours_str != "":                                                 # If hours_string is not empty
            hours = int(hours_str)                                          # Convert it to integer and store as number of hours for the lections
        else:
            hours=0                                                         # if there are no hours in the lection, set hours to 0
        
        total_hours += hours                                                # Add lab, lesson or practice to total number of hours for the subject
    result[line[0]] = total_hours                                           # Store subject and its total hours
    
print(result)