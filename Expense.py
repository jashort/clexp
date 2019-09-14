#!/usr/bin/python
import datetime
import decimal
import re


class Expense():
    """
    Represents a single expense
    """

    def __init__(self, amount, category, description, date=None):
        """
        Creates new Expense object
        @param amount: Amount, string (with or without dollar sign - "$12.34") or a float (12.34)
        @param category: String, will be "Title Cased"
        @param description: String
        @param date: Date in MM/DD/YYYY format (optional, assumes today if None)
        """
        self.amount = self.calculate_amount(str(amount).replace('$', ''))
        self.category = category.title()
        self.description = description
        if date is None:
            self.date = datetime.datetime.now().date()
        else:
            self.date = datetime.datetime.strptime(date, "%m/%d/%Y").date()

    def __str__(self):
        """
        Returns a tab delimited string representing the current object:
        Date    Category    Description     $Amount
        @return: string
        """
        return str(self.date.strftime("%m/%d/%Y")) + "\t" + \
            self.category + "\t" + \
            self.description + "\t" + \
            "${:0.2f}".format(self.amount)

    @property
    def year(self):
        return self.date.year

    @property
    def month(self):
        return self.date.month

    @property
    def day(self):
        return self.date.day

    @staticmethod
    def calculate_amount(amount):
        """
        Given an input string, evaluates it and returns a decimal.
        @param amount: String, float or int
        @return: Decimal
        For example, "1.11+2.22" would return Decimal(3.33). This allows the expense object to accept
        mathematical formulae
        """
        try:
            # If the amount can be converted to a decimal, just return that to avoid unnecessary work
            return decimal.Decimal(amount)
        except decimal.InvalidOperation:
            # If that doesn't work, use regex to convert every number in the input to a decimal and
            # then evaluate it to get the result
            try:
                # Allow only numbers and operators. Even though input should be trusted here, I can't
                # bring myself to run eval on whatever comes in!
                valid_characters = re.compile(r"^[\d .+\-*/()]+$")
                number_pattern = re.compile(r"((\A|(?<=\W))(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?)")
                if valid_characters.match(amount) is not None:
                    result = eval(number_pattern.sub(r"decimal.Decimal('\1')", amount))
                    return result.quantize(decimal.Decimal('.01'))  # round result
                else:
                    raise ValueError("Invalid characters found in amount: {}".format(amount))
            except:
                raise ValueError("Error parsing amount: {}".format(amount))

