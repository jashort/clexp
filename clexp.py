#!/usr/bin/env python
import datetime
import sys
import os
import argparse

from ExpenseList import ExpenseList
from Expense import Expense


def add_expense(args):
    """
    Add expense to the data file
    @param args: Command Line Arguments
    """
    e = Expense(args.amount, args.category, args.description, args.date)

    # Also add_expense a header row if the file doesn't exist
    header = None
    if not os.path.isfile(args.file):
        header = "Date\tCategory\tDescription\tAmount\n"

    with open(args.file, 'a') as f:
        if header is not None:
            f.write(header)
        f.write(str(e))
        f.write("\n")
    print ("Added:")
    print str(e)
    return True


def total_expenses(args):
    """
    Print the total_expenses amount spent in the given time period
    """
    expenses = load_data(args.file)
    if args.year is not None and args.month is not None and args.category is not None:
        print "Total spent in {}/{} on {}: ${:8,.2f}".format(args.month, args.year, args.category,
                                                             expenses.get_total(args.year,
                                                                                args.month,
                                                                                args.category))
    elif args.year is not None and args.month is not None:
        print "Total spent in {}/{}: ${:8,.2f}".format(args.month,
                                                       args.year,
                                                       expenses.get_total(args.year,
                                                                          args.month,
                                                                          args.category))
    elif args.year is not None:
        print "Total spent in {}: ${:8,.2f}".format(args.year,
                                                    expenses.get_total(args.year,
                                                                       args.month,
                                                                       args.category))
    else:
        print "Total spent: ${:8,.2f}".format(expenses.get_total(args.year,
                                                                 args.month,
                                                                 args.category))


def list_expenses(args):
    """
    Print all expenses in the given time period
    """
    expenses = load_data(args.file)
    items = list(expenses.get_expenses(args.year, args.month, args.category))
    items.sort(key=lambda expense: expense.date)
    for item in items:
        print item


def summary(args):
    """
    Print a summary of the current month
    """
    expenses = load_data(args.file)
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


def load_data(filename):
    """
    Load data from the given filename, returns ExpenseList object
    """
    expenses = ExpenseList()

    with open(filename) as f:
        f.readline()    # skip header row
        for line in f:
            if line.strip() != "":
                line = line.strip().split("\t")
                # Note - file is stored date, category, description, amount
                # but add_expense is expecting amount first and date last
                # (because date is optional)
                line[0], line[3] = line[3], line[0]
                expenses.add_expense(line)
    return expenses


def main():
    """
    Parse command line arguments for command and run the appropriate function
    """

    parser = argparse.ArgumentParser(description='Track expenses from the command line')
    parser.add_argument("-f", "--file", help="Data File", default="./data.csv")
    subparsers = parser.add_subparsers(help='')
    # Parser for add_expense command
    a_add = subparsers.add_parser('add', help='Add Expense')
    a_add.add_argument('amount', type=str, help='Dollar amount')
    a_add.add_argument('category', type=str, help='Category')
    a_add.add_argument('description', type=str, help='Description')
    a_add.add_argument('date', nargs='?', type=str, default=None,
                       help="Date in MM/DD/YYYY format (default: today's date)")
    a_add.set_defaults(func=add_expense)
    # Parser for list command
    a_list = subparsers.add_parser('list', help='List Expenses')
    a_list.add_argument('year', type=int, default=None, nargs='?', help="Year (optional)")
    a_list.add_argument('month', type=int, default=None, nargs='?', help="Month (optional)")
    a_list.add_argument('category', default=None, nargs='?', help='Category (optional)')
    a_list.set_defaults(func=list_expenses)
    # Parser for total_expenses command
    a_total = subparsers.add_parser('total', help='Show total amount of matching expenses')
    a_total.add_argument('year', type=int, default=None, nargs='?', help="Year (optional)")
    a_total.add_argument('month', type=int, default=None, nargs='?', help="Month (1 - 12, optional)")
    a_total.add_argument('category', type=str, default=None, nargs='?', help='Category (optional)')
    a_total.set_defaults(func=total_expenses)
    a_summary = subparsers.add_parser('summary', help='Show summary of current and previous months')
    a_summary.set_defaults(func=summary)

    args = parser.parse_args()
    args.func(args)
    #print args


    return 0


if __name__ == "__main__":
    sys.exit(main())




