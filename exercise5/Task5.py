# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import os,sys
 
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]      # List of numbers

with open(os.path.join(sys.path[0], " Task5.txt"), "w") as file:    # Open file in write mode
    for i in numbers:                                               # For each number in the list write it to the file as string and append space
        file.write(str(i))
        file.write(" ")

with open(os.path.join(sys.path[0], " Task5.txt"), "r") as file:    # Open the file in read mode
    lines = file.read().splitlines()                                # Save contents as list of lines

for line in lines:                                                  # For each line
    line_sum = 0                                                    # Variable to store sum of the numbers
    for i in line.split():                                          # for each number in line, split by space and convert to integer
        line_sum += int(i)                                          # add to sum of the numbers

    print(line_sum)                                                 # print result