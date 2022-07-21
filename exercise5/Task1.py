# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

user_data = input("Please enter some text : ")      # Prompt for input
file = open("user_input.txt", "w")                  # Open the file in write mode

while user_data.replace(" ", "") != "":             # Keep working while entered text is not an empty line
    file.write(f"{user_data}\n")                    # Write the text to the file and append new line
    user_data = input("Please enter some text : ")  # Prompt for new input
    continue
else:                                               # If entered text is an empty line, close file
    print("You entered an empty line. Exiting")
    file.close()


for line in open("user_input.txt", "r").readlines():# Print the file contents line by line
    print(line, end="")