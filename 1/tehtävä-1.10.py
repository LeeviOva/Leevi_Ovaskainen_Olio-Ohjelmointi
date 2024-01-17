def user_interface():
    user_input = input("command (1 search, 2 add, 3 quit): ")
    user_input = int(user_input)
    return user_input

def search_phone(phonebook):
    name = input("Name: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("no number.")

def add_phone(phonebook):
    user_name = input("name:")
    user_number = input("number:")
    phonebook[user_name] = user_number
    print("Ok!")


phonebook = {
    "leevi": "12346",
}

while True:
    user_input = user_interface()
    if user_input == 3:
        print("Quitting...")
        break
    elif user_input == 1:
        search_phone(phonebook)
    elif user_input == 2:
        add_phone(phonebook)

