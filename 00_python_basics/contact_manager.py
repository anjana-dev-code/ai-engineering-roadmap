class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def to_line(self):
        return f"{self.name},{self.phone}\n"


def save_contact(contact):
    with open("contacts.txt", "a") as f:
        f.write(contact.to_line())


def show_contacts():
    try:
        with open("contacts.txt", "r") as f:
            lines = f.readlines()
            if not lines:
                print("No contacts yet.")
            for line in lines:
                name, phone = line.strip().split(",")
                print(f"{name}: {phone}")
    except FileNotFoundError:
        print("No contacts yet.")


# Main loop
while True:
    print("\n1. Add contact  2. Show contacts  3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contact = Contact(name, phone)
        save_contact(contact)
        print("Saved!")
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")