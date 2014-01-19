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

    def testCreateExpenseFromDecimal(self):
        e = Expense(2.53, "Living Expenses", "Rent and utilities", "12/1/2013")
        self.failUnless(float(e.amount) == 2.53)

    def testCreateExpenseWithoutDate(self):
        today = datetime.datetime.now()
        e = Expense(2.53, "Living Expenses", "Rent and utilities")
        self.failUnless(e.date == today.date())

    def testCreateExpenseWithFormula(self):
        e = Expense('5+4', 'Test', 'Test')
        self.failUnless(int(e.amount) == 9)

    def testCreateExpenseWithComplicatedFormula(self):
        e = Expense('5.50 - 2.13 + 27/(3*2)', 'Test', 'Test')
        self.failUnless(float(e.amount) == 7.87)

    def testCreateExpenseWithDivisionFormula(self):
        e = Expense('44/3', 'Test', 'Test')
        self.failUnless(float(e.amount) == 14.67)

    def testCreateExpenseWithCharactersInFormula(self):
        self.assertRaises(ValueError, Expense, '5*a', 'Test', 'Test')

    def testCreateExpenseWithInvalidFormula(self):
        # Missing parenthesis in formula
        self.assertRaises(ValueError, Expense, '(3-2', 'Test', 'Test')

