from unittest import TestCase
import datetime

from ExpenseList import ExpenseList


class TestExpenseList(TestCase):
    def setUp(self):
        self.el = ExpenseList()
        # passing amount as a float is valid
        self.el.add_expense([2.11, "Food", "Candy Bar", "12/01/2013"])
        # so is a string
        self.el.add_expense(["53.32", "Living Expenses", "Electric bill", "12/02/2013"])
        # so is a string with a $ in front
        self.el.add_expense(["$11.74", "Fun", "Party Hats", "11/30/2013"])
        self.el.add_expense([33.24, "Living Expenses", "Work hats", "11/29/2013"])

    def test_add_expense(self):
        e = ExpenseList()
        e.add_expense([1.75, "Food", "Candy Bar", "12/01/2013"])
        item = e.expenses[2013][12][0]
        self.assertEqual(item.amount, 1.75)
        self.assertEqual(item.category, "Food")
        self.assertEqual(item.date, datetime.datetime(2013, 12, 01).date())
        self.assertEqual(len(e.expenses), 1)

    def test_get_expenses(self):
        results = self.el.get_expenses(2013, 12)
        self.assertEqual(len(results), 2)
        results = self.el.get_expenses(2013)
        self.assertEqual(len(results), 4)
        results = self.el.get_expenses(2013, 11, "Fun")
        self.assertEqual(len(results), 1)

    def test_get_total(self):
        self.assertEqual(self.el.get_total(), 100.41)
        self.assertEqual(self.el.get_total(2013), 100.41)
        self.assertEqual(self.el.get_total(2013, 11), 44.98)
        self.assertEqual(self.el.get_total(2013, 12, "Food"), 2.11)

    def test_get_average_per_day(self):
        self.assertEqual(self.el.get_average_per_day(2013, 11), 1.5)


    def test_get_years(self):
        self.assertEqual(self.el.get_years(), [2013])

    def test_get_months(self):
        self.assertEqual(self.el.get_months(2013), [11, 12])