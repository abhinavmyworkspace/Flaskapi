from datetime import datetime

class Validation:

    def __init__(self, data:dict):
        self.CreditCardNumber = data.get('CreditCardNumber')
        self.CardHolder = data.get('CardHolder')
        self.ExpirationDate = data.get('ExpirationDate')
        self.Amount = data.get('Amount')
        self.SecurityCode = data.get('SecurityCode')

    def checkrequestdatatype(self) -> bool:
        """ Check data type of request json """
        check = {'CreditCardNumber': isinstance(self.CreditCardNumber, str),
                 'CardHolder': isinstance(self.CardHolder, str),
                 'ExpirationDate': isinstance(self.ExpirationDate, str),
                 'Amount': isinstance(self.Amount, float)}

        if self.SecurityCode:
            check['SecurityCode'] = isinstance(self.SecurityCode, str)
        validate = [k for k, v in check.items() if v is False]
        if len(validate) > 0 and validate:
            return False
        return True

    @staticmethod
    def valid_cc(creditcardnumber: str) -> bool:
        """ Function Check Validity of a credit Card Number
            1. Length of credit card number should be 16
            2. Only Digits allowed                          """
        creditcardnumber = creditcardnumber.replace('-', '')

        if len(creditcardnumber) is not 16 or not creditcardnumber.isdigit():
            return False
        return True

    def validate_params(self) -> bool:
        """ validate data  of request json """
        check = dict()

        check['CreditCardNumber'] = self.valid_cc(self.CreditCardNumber)

        check['ExpirationDate'] = True if datetime.now().date() < datetime.strptime(self.ExpirationDate,
                                                                                    "%d/%m/%Y").date() else False
        check['Amount'] = True if self.Amount > 0 else False
        if self.SecurityCode:
            check['SecurityCode'] = True if len(self.SecurityCode) is 3 else False

        validate = [k for k, v in check.items() if v is False]
        if len(validate) > 0 and validate:
            return False
        return True
