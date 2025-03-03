contacts=[]


while True:
    print("\nCONTACT BOOK APPLICATION")
    print("1.Add Contact")
    print("2.View Contacts")
    print("3.Update Contact")
    print("4.Delete Contact")
    print("5.Search Contact")
    print("6.Save and Exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        name=input("Enter the contact name: ")
        phone=int(input("Enter the phone number: "))
        email=input("Enter the email address of the contact: ")
        contact={"NAME: ": name , "PHONE NUMBER: ": phone , "EMAIL: ": email}
        contacts.append(contact)
        print(f"{name}'s contact has been updated successfully!" )

    elif choice==2:
        print("\n CONTACTS: ")
        for contact in contacts:
            print(f"Name: {contact['NAME: ']}, Ph.no: {contact['PHONE NUMBER: ']}, E-Mail: {contact['EMAIL: ']}")

    elif choice==3:
        name=input("Enter the name of the contact you want to update: ")

        if contact["NAME: "]==name:
            phone=int(input("Enter the new phone number: "))
            email=input("Enter the new email address: ")
            contact["PHONE NUMBER: "]=phone
            contact["EMAIL: "]=email
            print(f"Contact {name} has been updated successfully!")

    
    elif choice==4:
        name=input("Enter the name of the character you want to delete: ")

        for contact in contacts:
            if contact["NAME: "]==name:
                contacts.remove(contact)
                print("The contact has been deleted successfully!")
                break

    
    elif choice==5:
        name=input("Enter the name of the contact you want to search for: ")

        for contact in contacts:
            if contact["NAME: "]==name:
                print(f"Name: {contact['NAME: ']}, Ph.no: {contact['PHONE NUMBER: ']}, E-Mail: {contact['EMAIL: ']}")
                break
        else:
            print("Contact not found!")

    
    elif choice==6:
        print("Exiting.....")
        break

    else:
        print("Invalid choice! Please try again.")


        



