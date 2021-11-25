class Customer:

    def __init__(self, name, wallet, favourite_performer):
        self.name = name
        self.wallet = wallet
        self.favourite_performer = favourite_performer
    
    def decrease_wallet(self, amount):
        self.wallet -= amount
    
    def can_afford(self, amount):
        return self.wallet >= amount
    
    def buy_ticket(self, event):
        if self.can_afford(event.ticket_price):
