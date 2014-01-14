from unittest import TestCase
import datetime
from Expense import Expense


class TestExpense(TestCase):
    def testCreateExpense(self):
        e = Expense("$2.53", "Living Expenses", "Rent and utilities", "12/1/2013")
        self.failUnless(float(e.amount) == 2.53)
        self.failUnless(e.category == "Living Expenses")
        self.failUnless(e.description == "Rent and utilities")
        self.failUnless(e.date == datetime.date(2013, 12, 1))
        self.failUnless(e.day == 1)
        self.failUnless(e.month == 12)
        self.failUnless(e.year == 2013)
        self.failUnless(str(e) == "12/01/2013	Living Expenses	Rent and utilities	$2.53")

    def testCreateExpenseDecimal(self):
        e = Expense(2.53, "Living Expenses", "Rent and utilities", "12/1/2013")
        self.failUnless(float(e.amount) == 2.53)

    def testCreateExpenseWithoutDate(self):
        today = datetime.datetime.now()
        e = Expense(2.53, "Living Expenses", "Rent and utilities")
        self.failUnless(e.date == today.date())
