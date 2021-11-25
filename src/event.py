class Event:

    def __init__(self, name, ticket_price):
        self.name = name
        self.ticket_price = ticket_price
        self.revenue = 0
        self.performer_list = []
        self.customer_list = []
    
    def adjust_revenue(self, amount):
        self.revenue += amount
        
    def performer_count(self):
        return len(self.performer_list)

    