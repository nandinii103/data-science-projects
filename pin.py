class Account:

    def __init__(self, username, pin):
        self.username = username
        self.__pin = pin   # private attribute

    # Show PIN status (fixed name)
    def show_pin_status(self):
        print("User:", self.username)
        print("Your PIN is stored securely and cannot be accessed directly.")

    # Setter method to safely update the PIN
    def set_pin(self, new_pin):
        if new_pin.isdigit() and len(new_pin) == 4:
            self.__pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Error: PIN must be a 4 digit number.")

    # Special function used by print()
    def __str__(self):
        return "Account User: " + self.username



my_account = Account("Alex", "4321")


print(my_account)


my_account.show_pin_status()


my_account.__pin = "9999"
print("Tried changing PIN directly from outside.")

my_account.set_pin("9999")


print("All tasks completed successfully.")


