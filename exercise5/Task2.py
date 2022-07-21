# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
import os
import sys

with open(os.path.join(sys.path[0], "task2.txt"), 'r') as file:
    lines = file.readlines()
    print(f"File has {len(lines)} lines")                       # Count number of lines
    line_number = 0

    for line in lines:                                          # Go through each line
        line_number += 1                                        # Go to next line
        if len(line.strip()) == 0:                              # Remove spaces and check if the line is empty
            print(f"Line {line_number} has 0 words.")           # Print number of words
            
        else:                                                   # If the line is not empty
            line = line.split(" ")                              # Convert lne to a list
            print(f"Line {line_number} has {len(line)} words")  # Print number of words
        