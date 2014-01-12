#!/usr/bin/python
import datetime
import string
import decimal


class Expense():
    """
    Represents a single expense
    """

    def __init__(self, amount, category, description, date=None):
        """
        Creates new Expense object
        @param amount: Amount, can be a string (with or without) dollar sign ("$12.34") or a float (12.34)
        @param category: String, will be "Title Cased"
        @param description: String
        @param date: Date in MM/DD/YYYY format (optional, assumes today if None)
        """
        self.amount = decimal.Decimal(string.replace(str(amount), "$", ""))
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
               self.description + "\t$" + \
               "{:0.2f}".format(self.amount)

    @property
    def year(self):
        return self.date.year

    @property
    def month(self):
        return self.date.month

    @property
    def day(self):
        return self.date.day



