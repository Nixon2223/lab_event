class Performer:

    def __init__(self, name):
        self.name = name
        self.earnings = 0

    def increase_earnings(self, amount):
        self.earnings += amount