# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
# При этом английские числительные должны заменяться на шведские. Новый блок строк должен записываться в новый текстовый файл.
import os,sys

with open(os.path.join(sys.path[0],"Task4.txt"),"r") as file:                           # Open file
    lines = file.read().splitlines()                                                    # Store lines in a list


replace_dict = {"One" : "En",                                                           # Dictionary to replace English words to Swedish
                "Two" : "Två",
                "Three" : "Tre",
                "Four" : "Fyra" }
result = []                                                                             # Variable to store the end result
for line in lines:                                                                      # Go through each line
    for key, value in replace_dict.items():                                             # Go through each dictionary key
        if key in line:                                                                 # If the key is in the line
            result.append(line.replace(key, value))                                     # Replace the english word(key) with swedish one(value) and add to the end result

with open(os.path.join(sys.path[0],"Task4_result.txt"), "w", encoding="utf-8") as file: # Open new file
    for line in result:                                                                 # Go through each line in the end result
        file.write(line)                                                                # Write the line
        file.write('\n')                                                                # Write new line
