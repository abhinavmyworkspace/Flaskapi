
class Payment:
    def __init__(self, data: dict):
        """Initialize variable for payment"""
        self.CreditCardNumber = data.get('CreditCardNumber')
        self.CardHolder = data.get('CardHolder')
        self.ExpirationDate = data.get('ExpirationDate')
        self.Amount = data.get('Amount')
        self.SecurityCode = data.get('SecurityCode')

    def CheapPaymentGateway(self) -> dict:
        """ Cheap Payment method"""

        return {'ok': 1}


    def ExpensivePaymentGateway(self) -> dict:
        """ Expensive Payment method"""

        return {'ok': 1}


    def PremiumPaymentGateway(self) -> dict:
        """ Premium Payment method
        Implement logic
        """

        return {'ok': 1}
