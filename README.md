CLExp
=====

Command Line Expense Tracker - track and report expenses from the command line

CLExp is designed as a simple expense tracker. It stores data in a human
readable (tab delimited) format, and is meant to be synced between devices
via another service ([Spideroak](http://www.spideroak.com/),
[Dropbox](http://www.dropbox.com/), automated rsync, etc).


Usage:
-------------
    clexp.py [-f filename] <command> [arguments]

Examples:

    clexp.py add 8.95 food Lunch
(adds an expense for $8.95 to the Food category, with the description "Lunch"
and today's date)

    clexp.py add 8.95 food Lunch 12/20/2013
(adds an expense for $8.95 to the Food category, with the description "Lunch"
and the date 12/20/2013)

    clexp.py total
(shows the total amount spent in all time)

    clexp.py total 2013
(shows the total amount spent in 2013)

    clexp.py total 2013 12
(shows the total amount spent in December 2013)

    clexp.py totals
(shows the total amount spent by month)

    clexp.py categories
(shows categories currently found in the data file)

    clexp.py plot
(plots total amount spent by month using matplotlib)


Settings:
-------------
Data is read from/saved to the file specified by the -f parameter, or defaults
to data.csv in the current directory.