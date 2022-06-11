user_data = ""
special_character = "!"
result = 0

def summ_numbers(user_data:str, special_character:str):
    """
    Prompts for an array of numbers, separated by space and calculates their sum until user enters a special character.
    :param user_data: String of numbers, separated by space
    :param special_character: Special character used to break the function execution
    :return: Integer - sum of numbers passed in user_data argument
    """
    result = 0
    user_data = user_data.split(" ")                    # Convert string to a list

    # Check if item in the list is not the special character and add to the result
    for i in user_data:
        if i != special_character:
            try:
                result += int(i)
            except:
                print(f"{i} is not a number. Skipping...")
        else:
            break
    return result


while special_character not in user_data :
    user_data = input("Please enter numbers:")
    result += summ_numbers(user_data,"!")
    print(result)
