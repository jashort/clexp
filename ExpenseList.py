import calendar
import datetime

from Expense import Expense


class ExpenseList():
    def __init__(self):
        self.expenses = {}
        self.categories = []

    def add_expense(self, array):
        """
        Add an expense. If date is not passed, assumes the current day
        @param array: [amount, category, description, (optional) date]
        """
        if len(array) != 4:
            raise ValueError("Error adding expense: " + str(array))

        expense = Expense(array[0], array[1], array[2], array[3])
        year = expense.year
        month = expense.month

        if year not in self.expenses.keys():
            self.expenses[year] = {}

        if month not in self.expenses[year].keys():
            self.expenses[year][month] = []

        self.expenses[year][month].append(expense)

        if expense.category not in self.categories:
            self.categories.append(expense.category)

    def get_expenses(self, year=None, month=None, category=None):
        """
        Returns a iterable matching the given criteria
        @param year: Year (optional)
        @param month: Month (1 - 12, Optional)
        @param category: string (Optional, not case sensitive)
        @return: iterator
        """
        if category is not None:
            category = category.title()

        if year is None:
            years = self.expenses.keys()
        elif year in self.expenses.keys():
            years = [year]
        else:
            raise StopIteration

        for y in years:
            for m in self.expenses[y].keys():
                if month is None:
                    for expense in self.expenses[y][m]:
                        if category is None:
                            yield (expense)
                        else:
                            if expense.category == category:
                                yield (expense)
                elif m == month:
                    for expense in self.expenses[y][m]:
                        if category is None:
                            yield (expense)
                        else:
                            if expense.category == category:
                                yield (expense)

    def get_total(self, year=None, month=None, category=None):
        """
        Returns the total of expenses matching the given criteria. Missing criteria will be
        ignored. For example, get_total(2013) returns the total for 2013. get_total(month=1)
        would return the total for expenses in January of every year.
        @param year: Year (optional)
        @param month: Month (1 - 12) (optional)
        @param category: string (optional, not case sensitive)
        @return: float
        """

        expenses = self.get_expenses(year, month, category)
        total = sum(expense.amount for expense in expenses)
        return round(total, 2)

    def get_average_per_day(self, year, month, category=None):
        """
        Returns the mean amount spent per day for the matching criteria.
        @param year: Year (required)
        @param month: Month (1 - 12, required)
        @param category: string
        """
        total = self.get_total(year, month, category)
        days = calendar.monthrange(year, month)[1]
        return round(total / days, 2)

    def get_years(self):
        """
        Returns a list of available years
        @return: list
        """
        return self.expenses.keys()

    def get_months(self, year):
        """
        Returns a list of months available in the given year, or an empty list
        if the year doesn't exist
        @param year: Year
        @return: list
        """
        if year in self.expenses.keys():
            return self.expenses[year].keys()
        else:
            return []

    def get_month_totals(self):
        """
        Get the total amount spent for each month, returns a list of tuples:
        (datetime, amount)
        """
        output = []
        for year in self.get_years():
            for month in self.get_months(year):
                output.append((datetime.datetime(year, month, 1), self.get_total(year, month)))

        return output

