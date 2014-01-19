CLExp
=====

Command Line Expense Tracker - track and report expenses from the command line

CLExp is designed as a simple expense tracker. It stores data in a human
readable (tab delimited) format, and is meant to be synced between devices
via another service ([Spideroak](http://www.spideroak.com/),
[Dropbox](http://www.dropbox.com/), automated rsync, etc).


Usage:
-------------
    clexp [-f filename] <command> [arguments]

Examples:

    clexp add 8.95 food Lunch
(adds an expense for $8.95 to the Food category, with the description "Lunch"
and today's date)

    clexp add 8.95 food Lunch 12/20/2013
(adds an expense for $8.95 to the Food category, with the description "Lunch"
and the date 12/20/2013)

    clexp add 45.30/3 food Lunch
(Evalate the expression "45.30/3" and add the result to the Food category with the description "Lunch")

    clexp total
(shows the total amount spent in all time)

    clexp total 2013
(shows the total amount spent in 2013)

    clexp total 2013 12
(shows the total amount spent in December 2013)

    clexp detail
(Shows total spent for each category for all time)

    clexp detail 2013 12
(Shows total spent for each category for December 2013)

    clexp totals
(shows the total amount spent by month)

    clexp categories
(shows categories currently found in the data file)

    clexp plot
(plots total amount spent by month using matplotlib)


Settings:
-------------
Data is read from/saved to the file specified by the -f parameter, or defaults
to data.csv in the current directory.