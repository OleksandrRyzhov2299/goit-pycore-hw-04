def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "✅ Contact added."


def show_phone(name, contacts):
    phone_number = contacts.get(name[0])

    if not phone_number:
        return "❌ Contact does not exist"

    return phone_number


def change_contact(contact_for_change, contacts):
    if len(contact_for_change) < 2:
        return "❌ Invalid values"
    
    contact_name, contact_phone = contact_for_change
    for contact in contacts:
        if contact_name == contact:
            contacts[contact_name] = contact_phone
            return "✅ Contact updated"

    return "❌ Contact does not exist"


def show_all(contacts):
    if not contacts:
        return "❌ Phone book is empty"
    
    printed_contatcs = ''
    for key, value in contacts.items():
        printed_contatcs += f"📒: {key} 📱: {value}\n"
    return printed_contatcs

def main():
    phone_book = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *info = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(info, phone_book))
        elif command == "phone":
            print(show_phone(info, phone_book))
        elif command == "change":
            print(change_contact(info, phone_book))
        elif command == "all":
            print(show_all(phone_book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
