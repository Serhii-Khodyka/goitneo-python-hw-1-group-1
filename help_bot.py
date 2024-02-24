

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def show_phone(args, contacts):
    name = args[0]
    if name in contacts.keys():
        print(contacts[name])
    else:
        print(f"No {name} in contacts.")

def show_all(contacts):
    for name, number in contacts.items():
        print(f"{name} {number}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("""
          HELP:
          add name number => add phone number
          change name number => change phone number
          phone name => show phone
          all => show all contacts
          close or exit
          """)
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts)) 
        elif command == "all":
            show_all(contacts) 
        elif command == "phone":
            show_phone(args, contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()