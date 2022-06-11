def my_func(some_text:str):
    return some_text.lower().capitalize()

print(my_func("text"))


text = "test text for the task"
result = []
for i in text.split(" "):
    result.append(my_func(i))
print(' '.join(result))