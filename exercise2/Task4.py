# Пользователь вводит строку из нескольких слов, разделённых пробелами. 
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать. 
# Если в слово длинное, выводить только первые 10 букв в слове.

text = input("Please enter text with some spaces:")     # Ask for user input
text = text.split(" ")                                  # Split string into list by space

start_line = 1                                          # Initial line number

for word in text:
    if len(word) >= 10:                                 # If word length is more than 10 characters, shorten it
        word = word[:9]
    print(f"{start_line}. {word}")                      # Print line number and word
    start_line += 1                                     # Increment line number