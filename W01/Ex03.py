class Cards:
    def __init__(self, customer, idCard, limit, balance=0):
        self._customer =customer
        self._idCard = idCard
        self._limit = limit
        self._balance = balance

    def charge(self, price):
        if price <= self._balance:
            self._balance -= price
            return True
        else:
            return False

    def make_deposit(self, amount):
        self._balance += amount

