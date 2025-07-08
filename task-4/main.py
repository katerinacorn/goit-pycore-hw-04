from messages import MESSAGES


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return MESSAGES["add_fail"]
    name, phone = args
    contacts[name] = phone
    return MESSAGES["add_success"]


def change_contact(args, contacts):
    if len(args) != 2:
        return MESSAGES["change_fail_args"]
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return MESSAGES["change_success"]
    else:
        return MESSAGES["contact_not_found"]


def show_phone(args, contacts):
    if len(args) != 1:
        return MESSAGES["phone_fail_args"]
    name = args[0]
    if name in contacts:
        return MESSAGES["phone_found"](name, contacts[name])
    else:
        return MESSAGES["contact_not_found"]


def show_all(contacts):
    if not contacts:
        return MESSAGES["all_empty"]
    result = [MESSAGES["all_header"]]
    for name, phone in contacts.items():
        result.append(MESSAGES["all_entry"](name, phone))
    return "\n".join(result)


def show_help():
    return MESSAGES["help"]


def main():
    contacts = {}
    print(MESSAGES["welcome"])

    while True:
        user_input = input(MESSAGES["prompt"])
        command, args = parse_input(user_input)

        if not command:
            continue

        if command in ["close", "exit"]:
            print(MESSAGES["goodbye"])
            break
        elif command == "hello":
            print(MESSAGES["greeting"])
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command in ["help", "-h"]:
            print(show_help())
        else:
            print(MESSAGES["invalid"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋🤖 Good bye!")
