
def input_error_1(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "The entered data is incorrect."
        except ValueError:
            return "Enter the argument for the command."
        except IndexError:
            return "The entered data is incorrect."
    return inner





def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error_1
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error_1
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return "Contact does not exist!\nUse command 'add [name] [phone]' to add a new contact."
    else:
        contacts[name] = phone
        return "Contact changed."

@input_error_1
def show_phone(args, contacts):
    if args[0] not in contacts:
        return "Contact does not exist!\nUse command 'add [name] [phone]' to add a new contact."
    else:
        return contacts[args[0]]

@input_error_1
def show_all(contacts):
    values = []
    for key, value in contacts.items():
        values.append([key,value]) # Я б тут використав "Print(key, value)", але умова забороняє.
    return values



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

# Перевірка вхідних запитів та виклик функцій
#-------------------------------------------------------------------
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
#-------------------------------------------------------------------


if __name__ == "__main__":
    main()
