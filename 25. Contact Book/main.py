import json

FILE_NAME = "contacts.json"

def save_contact(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file)

def load_contact():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def show_contact(contacts):
    if len(contacts) == 0:
            print("No Contact yet.")
            return
    
    for num, contact in enumerate(contacts, start=1):
        print(f"{num}. Name: {contact['name']} | Phone Number: {contact['phone']} | Email: {contact['email']}")

def add_contact(contacts):
    name = input("enter the name: ").strip().title()
    phone = input("enter the phone number: ").strip()
    email = input("enter the email: ").strip().lower()

    if name == "" or phone == "" or email == "":
        print("Fields cannot be empty.")
        return
    contacts.append({"name": name, "phone": phone,"email": email })
    save_contact(contacts)
    print("Contact added.")

def search_contact(contacts):
    search = input("Search by name: ").strip().lower()

    if search == "":
        print("Please enter a name to search.")
        return

    found = False

    for n, contact in enumerate(contacts, start=1):
        if search in contact["name"].lower():
            print(f"{n}. Name: {contact['name']} | Phone Number: {contact['phone']} | Email: {contact['email']}")
            found = True

    if not found:
        print("Contact not found.")

def edit_contact(contacts):
    show_contact(contacts)

    if len(contacts) == 0:
        print("No Contact yet.")
        return

    try:
        number = int(input("Enter the number of Contact to Edit: "))
        if number < 1 or number > len(contacts):
            print("That number is not in the list.")
            return

        choose = int(input("Choose: (1) Name (2) Phone Number (3) Email "))
        if choose == 1:
            new_name = input("enter the name: ").strip().title()
            if new_name == "":
                print("Contact cannot be empty.")
                return
            contacts[number - 1]["name"] = new_name
        elif choose == 2:
            new_phone = input("enter the phone number: ").strip()
            if new_phone == "":
                print("Contact cannot be empty.")
                return
            contacts[number - 1]["phone"] = new_phone
        elif choose == 3:
            new_email = input("enter the email: ").strip().lower()
            if new_email == "":
                print("Contact cannot be empty.")
                return
            contacts[number - 1]["email"] = new_email
        else:
            print("That number is not in the list.")
            return
        save_contact(contacts)
        print("Contact updated!")
    except ValueError:
        print("Please type a number.")


def delete_contact(contacts):
    show_contact(contacts)

    if len(contacts) == 0:
        print("No tasks yet.")
        return

    try:
        number = int(input("Enter the number of Contact to Delete: "))
        if number < 1 or number > len(contacts):
            print("That number is not in the list.")
            return

        removed = contacts.pop(number - 1)
        print("Deleted: ", removed["name"])
        save_contact(contacts)
    except ValueError:
        print("Please type a number.")


def main():
    contacts = load_contact()
    while True:
        print("--- Contact Book ---")
        print("1. Show all contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Delete contact")
        print("6. Quit")

        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            show_contact(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            edit_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            break
        else:
            print("Please choose 1 to 6.")

main()
