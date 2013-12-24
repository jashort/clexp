#!/usr/bin/env python
import datetime
import sys
import os

from ExpenseList import ExpenseList
from Expense import Expense


# Where to store data
DATA_FILE = './data.csv'

commands = {}
expenses = ExpenseList()


def print_help(args=None):
    if not args: args = []
    print("clexp.py")
    print("Usage: ")
    print("   clexp.py <command>")
    print("   clexp.py add <amount> <category> <description> [date]")
    print("             Add the given item to the data file. If date is not passed, ")
    print("             assumes today")
    print("   clexp.py summary")
    print("            Show a summary of expenses in recent months")
    print("   clexp.py list [year] [month] [category]")
    print("            Show all items for the given year, month, and category")
    #    print("   exp show year")
    print("   clexp.py total [year] [month] [category]")
    print("            Show total for the given year, month, and category")
    print(" ")


def add(args, filename=None):
    """
    Add expense to the data file
    """
    if filename is None:
        filename = DATA_FILE
    e = None
    if len(args) < 3 or len(args) > 4:
        print("Error - add requires 3 or 4 parameters:")
        print("    exp add amount category description [date]")
        return False
    elif len(args) == 3:
        e = Expense(args[0], args[1], args[2])
    elif len(args) == 4:
        e = Expense(args[0], args[1], args[2], args[3])

    # Also add a header row if the file doesn't exist
    header = None
    if not os.path.isfile(filename):
        header = "Date\tCategory\tDescription\tAmount\n"

    with open(filename, 'a') as f:
        if header is not None:
            f.write(header)
        f.write(str(e))
        f.write("\n")
    print ("Added:")
    print str(e)
    return True


def total(args):
    """
    Print the total amount spent in the given time period
    """
    if len(args) > 0:
        year = int(args[0])
    else:
        year = None
    if len(args) > 1:
        month = int(args[1])
    else:
        month = None
    if len(args) > 2:
        category = str(args[2])
    else:
        category = None
    load_data()
    if year is not None and month is not None and category is not None:
        print "Total spent in {}/{} on {}: ${:8,.2f}".format(month, year, category,
                                                             expenses.get_total(year, month, category))
    elif year is not None and month is not None:
        print "Total spent in {}/{}: ${:8,.2f}".format(month, year, expenses.get_total(year, month, category))
    elif year is not None:
        print "Total spent in {}: ${:8,.2f}".format(year, expenses.get_total(year, month, category))
    else:
        print "Total spent: ${:8,.2f}".format(expenses.get_total(year, month, category))


def show(args):
    """
    Print all expenses in the given time period
    """
    if len(args) > 0:
        year = int(args[0])
    else:
        year = None
    if len(args) > 1:
        month = int(args[1])
    else:
        month = None
    if len(args) > 2:
        category = str(args[2])
    else:
        category = None
    load_data()
    items = list(expenses.get_expenses(year, month, category))
    items.sort(key=lambda expense: expense.date)
    for item in items:
        print item


def summary(args):
    """
    Print a summary of the current month
    """
    load_data()
    today = datetime.datetime.now()
    last_month = today.replace(day=1) - datetime.timedelta(days=1)
    last_year = today.replace(day=1) - datetime.timedelta(days=365)
    print "Total spent:"
    print "             This month: ${:8,.2f}".format(expenses.get_total(today.year, today.month))
    print "             Last month: ${:8,.2f}".format(expenses.get_total(last_month.year, last_month.month))
    print "   This month last year: ${:8,.2f}".format(expenses.get_total(last_year.year, last_month.month))
    print " "
    print "Average spent per day: "
    print "             This month: ${:8,.2f}".format(expenses.get_average_per_day(today.year, today.month))
    print "             Last month: ${:8,.2f}".format(expenses.get_average_per_day(last_month.year, last_month.month))
    print "   This month last year: ${:8,.2f}".format(expenses.get_average_per_day(last_year.year, last_month.month))
    print " "

    return True


def load_data(filename=None):
    """
    Load data from the given filename, default to the one defined in DATA_FILE
    """
    if filename is None:
        filename = DATA_FILE
    with open(filename) as f:
        f.readline()    # skip header row
        for line in f:
            if line.strip() != "":
                line = line.strip().split("\t")
                # Note - file is stored date, category, description, amount
                # but add_expense is expecting amount first and date last
                # (because date is optional)
                tmp = line[3]
                line[3] = line[0]
                line[0] = tmp
                expenses.add_expense(line)


def main():
    """
    Parse command line arguments for command and run the appropriate function
    """
    if len(sys.argv) == 1:
        print_help()
        return 1
    command = commands.get(sys.argv[1])
    if command is None:
        print_help()
        return 1
    if not command(sys.argv[2:]):
        return 1
    return 0

# Map command line arguments to functions.
commands["-h"] = print_help
commands["-?"] = print_help
commands["--help"] = print_help
commands["help"] = print_help
commands["add"] = add
commands["summary"] = summary
commands["sum"] = summary
commands["total"] = total
commands["show"] = show
commands["list"] = show

if __name__ == "__main__":
    sys.exit(main())




