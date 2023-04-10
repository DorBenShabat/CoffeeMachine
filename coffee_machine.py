from time import sleep


class CoffeeMachine:
    def __init__(self):
        with open("Prices.txt", "r") as file:
            self.mapping = dict(line.strip().split("=") for line in file)

    def order(self):
        print("Welcome to Coffee system!")
        is_off = False
        while not is_off:
            choice = input("What would you like to drink? \n(1) latte (2) cappuccino"
                           " (3) americano (4) espresso\nPlease select by number:")
            if choice in self.mapping:
                price = int(self.mapping[choice])  # Brings the price of the drink.
                choice = input("Would you like something else? Y/N: ")
                if choice.upper() == "N":  # User don't want another drink.
                    payment = self.process_payment(price)
                    if payment >= price:
                        self.make_coffee()
                        is_off = True
                elif choice.upper() == "Y":  # User wants another drink.
                    sec_choice = input("Please choose another drink: ")
                    if sec_choice in self.mapping:
                        price += int(self.mapping[sec_choice])  # Calculates new price.
                        payment = self.process_payment(price)
                        if payment >= price:  # If the payment is enough, make coffee.
                            self.make_coffee()
                            is_off = True
                else:
                    print("Your choice is incorrect")

            else:
                is_off = True

    def process_payment(self, price):
        """
        :param price: Price of the product.
        :return: The change for the client.
        """
        is_off = False
        customer_payment = 0
        customer_payment = int(input(f"Your bill is: {price}\nEnter the coins: "))
        while not is_off:
            if customer_payment < price:
                customer_payment += int(input(f"You need to add: {price - customer_payment}\nEnter more coins: "))
            elif customer_payment > price:
                print(f"Thank you! Here is your excess: {customer_payment - price}")
                is_off = True
            elif customer_payment == price:
                is_off = True
        return customer_payment

    def make_coffee(self):
        print("The machine is making your coffee...")
        sleep(1)
        print("Thank you! Here is your coffee ☕")
