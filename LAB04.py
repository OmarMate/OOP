import pickle
class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = 0.0
        self.credit_card = []
    def add_customer(self):
        self.cid = input("Enter Customer ID: ")
        self.cname = input("Enter Customer Name: ")
        self.acc_no = input("Enter Customer Account Number: ")
        self.balance = float(input("Enter Customer Balance: "))
    def display_customer(self):
        print("Customer ID: ", self.cid)
        print("Customer Name: ",  self.cname)
        print("Customer Account Number: ",  self.acc_no)
        print("Customer Balance: ", self.balance)
        print("Customer Credit Card: ",  self.credit_card)
class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0.0
    def add_card(self):
        self.card_no = input("Enter Card Number: ")
        self.cvv = input("Enter Card Verification Number: ")
        self.expiry_date = input("Enter Card Expiration Date: ")
        self.balance = float(input("Enter Card Balance: "))
    def display_card(self):
        print("Card Number: ", self.card_no)
        print("Card Verification Number: ", self.cvv)
        print("Card Expiry Date: ", self.expiry_date)
        print("Card Balance: ", self.balance)
#Main Code
def load_data(fname):
    try:
        file = open(fname, "rb")
        data = pickle.load(file)
        file.close()
        return data
    except FileNotFoundError:
        return []

def save_data(fname, data):
    file = open(fname, "wb")
    pickle.dump(data, file)
    file.close()

def find_customer(customers, cid):
    for c in customers:
        if c.cid == cid:
            return c

def find_card(cards, card_no):
    for card in cards:
        if card.card_no == card_no:
            return card
customers = load_data("myCustomers.txt")
cards = load_data("myCards.txt")

while True:
    print("1. Create Customer")
    print("2. Create Card")
    print("3. Transfer funds")
    print("4. Assign Card")
    print("5. Display Customer")
    print("6. Display Card")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        c = Customer()
        c.add_customer()
        customers.append(c)
        save_data("myCustomers.txt", customers)
    elif choice == "2":
        c2 = Card()
        c2.add_card()
        cards.append(c2)
        save_data("myCards.txt", cards)
    elif choice == "3":
        sender_id = input("Enter ID of sender: ")
        receiver_id = input("Enter ID of receiver: ")
        amount = float(input("Enter amount to transfer: "))
        sender = find_customer(customers, sender_id)
        receiver = find_customer(customers, receiver_id)
        sender.balance = sender.balance - amount
        receiver.balance = receiver.balance + amount
        save_data("myCustomers.txt", customers)

    elif choice == "4":
        cid = input("Enter Customer ID: ")
        card_no = input("Enter Card Number: ")
        customer = find_customer(customers, cid)
        card = find_card(cards, card_no)
        customer.credit_card.append(card.card_no)
        save_data("myCustomers.txt", customers)

    elif choice == "5":
        cid = input("Enter Customer ID: ")
        customer = find_customer(customers, cid)
        customer.display_customer()

    elif choice == "6":
        card_no = input("Enter Card Number: ")
        card = find_card(cards, card_no)
        card.display_card()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid input")
