from .Payment import Payment
from .Customer import Customer

class CreditCardPayment(Payment):
    def __init__(self, amount, created_at):
        super().__init__(amount, created_at)

        
    