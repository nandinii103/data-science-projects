class Account:
    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin

    def set_pin(self, new_pin):
        if len(str(new_pin)) == 4 and str(new_pin).isdigit():
            self.__pin = new_pin
            print("PIN updated successfully!")
        else:
            print("INVALID PIN! Must be 4 digits")

    def __str__(self):
        return f"Account holder: {self.name}, PIN: ****"


account1 = Account("Maria", 1234)

print(account1)

try:
    print(account1.__pin)
except AttributeError:
    print("CANNOT ACCESS PRIVATE ATTRIBUTE")

account1.set_pin(5678)

print(account1)
