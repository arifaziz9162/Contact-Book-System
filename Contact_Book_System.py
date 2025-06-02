import logging

# File handler and stream handler setup
logger = logging.getLogger("Expense_Logger")
logger.setLevel(logging.DEBUG)

if logger.hasHandlers():
    logger.handlers.clear()

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)  
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler("expense_tracker.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


class ContactBook:
    def __init__(self):
        self.contacts = {}


    def create_contact(self):
        name = input("Enter your name = ")
        if name in self.contacts:
            print(f"Contact {name} already exists!")
            logger.warning(f"Create failed: {name} already exists.")

        else:
            try:

                age = int(input("Enter the age = "))
                email = input("Enter the email = ")
                mobile_no = int(input("Enter the mobile number = "))
                self.contacts[name] = {'age': age, 'email': email, 'mobile_no': mobile_no}
                print(f"Contact {name} has been created successfully!")
                logger.info(f"Contact {name} created.")

            except ValueError as ve:
                logger.error(f"Invalid input while creating contact: {ve}")
                print(str(ve))


    def view_contact(self):
        name = input("Enter contact name to view = ")
        if name in self.contacts:
            self.display_contact(name)
            logger.info(f"Viewed contact {name}.")

        else:
            print("Contact not found!")
            logger.warning(f"View failed: {name} not found.")


    def update_contact(self):
        name = input("Enter contact name to update = ")
        if name in self.contacts:
            try:

                age = int(input("Enter the updated age = "))
                email = input("Enter the updated email = ")
                mobile_no = int(input("Enter the updated mobile number = "))
                self.contacts[name] = {'age': age, 'email': email, 'mobile_no': mobile_no}
                print(f"Contact {name} updated successfully!")
                logger.info(f"Contact {name} updated.")

            except ValueError as ve:
                print("Invalid input! Age and mobile number must be integers.")
                logger.error(f"Invalid input while updating contact: {ve}")

        else:
            print("Contact not found!")
            logger.warning(f"Update failed: {name} not found.")


    def delete_contact(self):
        name = input("Enter contact name to delete = ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} has been deleted successfully!")
            logger.info(f"Contact {name} deleted.")

        else:
            print("Contact not found!")
            logger.warning(f"Delete failed {name} not found.")


    def search_contact(self):
        search_name = input("Enter name to search = ")
        found = False
        for name, contact in self.contacts.items():
            if search_name.lower() in name.lower():
                self.display_contact(name)
                found = True

        if not found:
            print("No contact found with that name!")
            logger.info(f"No contact found with name like '{search_name}'")


    def count_contacts(self):
        print(f"Total contacts in your book: {len(self.contacts)}")
        logger.info(f"Total contact count: {len(self.contacts)}")


    def display_contact(self, name):
        contact = self.contacts[name]
        print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile No: {contact['mobile_no']}")


    def run(self):
        while True:
            print("\nContact Book System")
            print("1. Create Contact")
            print("2. View Contact")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Search Contact")
            print("6. Count Contact")
            print("7. Exit")

            try:

                choice = int(input("Enter your choice = "))

                if choice == 1:
                    self.create_contact()
                    
                elif choice == 2:
                    self.view_contact()

                elif choice == 3:
                    self.update_contact()

                elif choice == 4:
                    self.delete_contact()

                elif choice == 5:
                    self.search_contact()

                elif choice == 6:
                    self.count_contacts()

                elif choice == 7:
                    print("Closing the program...")
                    logger.info("Program exited by user.")
                    break

                else:
                    print("Invalid input! Enter a number between 1 and 7.")
                    logger.warning(f"Invalid menu choice: {choice}")

            except ValueError as ve:
                logger.error(f"Invalid input : {ve}")
                print(str(ve))

            except Exception as e:
                logger.error(f"Unexpected error while choosing : {e}")
                print(str(e))


if __name__ == "__main__":
    ContactBook().run()