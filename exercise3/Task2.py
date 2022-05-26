def user_data(name, surname, birth_year, user_city, user_email, phone) :
    print(name, end=" ")
    print(surname, end=" ")
    print(birth_year, end=" ")
    print(user_city, end=" ")
    print(user_email, end=" ")
    print(phone, end=" ")


user_data(
            name = input("Please enter user name : "),
            surname = input("Please enter user surname : "),
            birth_year = input("Please enter user birth year : "),
            user_city = input("Please enter city : "),
            user_email = input("Please enter user email : "),
            phone = input("Please enter user phone number : ")
    )