from unittest import TestCase
import datetime

from Expense import Expense


class TestExpense(TestCase):
    def test_create_expense(self):
        e = Expense("$2.53", "Living Expenses", "Rent and utilities", "12/1/2013")
        self.assertEqual(float(e.amount), 2.53)
        self.assertEqual(e.category, "Living Expenses")
        self.assertEqual(e.description, "Rent and utilities")
        self.assertEqual(e.date, datetime.date(2013, 12, 1))
        self.assertEqual(e.day, 1)
        self.assertEqual(e.month, 12)
        self.assertEqual(e.year, 2013)
        self.assertEqual(str(e), "12/01/2013	Living Expenses	Rent and utilities	$2.53")

    def test_create_expense_from_decimal(self):
        e = Expense(2.53, "Living Expenses", "Rent and utilities", "12/1/2013")
        self.assertEqual(float(e.amount), 2.53)

    def test_create_expense_without_date(self):
        today = datetime.datetime.now()
        e = Expense(2.53, "Living Expenses", "Rent and utilities")
        self.assertEqual(e.date, today.date())

    def test_create_expense_with_formula(self):
        e = Expense('5+4', 'Test', 'Test')
        self.assertEqual(int(e.amount), 9)

    def test_create_expense_with_complicated_formula(self):
        e = Expense('5.50 - 2.13 + 27/(3*2)', 'Test', 'Test')
        self.assertEqual(float(e.amount), 7.87)

    def test_create_expense_with_division_formula(self):
        e = Expense('44/3', 'Test', 'Test')
        self.assertEqual(float(e.amount), 14.67)

    def test_create_expense_with_characters_in_formula(self):
        self.assertRaises(ValueError, Expense, '5*a', 'Test', 'Test')

    def test_create_expense_with_invalid_formula(self):
        # Missing parenthesis in formula
        self.assertRaises(ValueError, Expense, '(3-2', 'Test', 'Test')

