CLExp Tutorial
=================

CLExp is a simple command line tool for keeping track of expenses by date,
amount and category, and reporting on that information. This is a quick
tutorial to get started, and assumes that CLExp is already installed.


Adding Expenses
----------------
To add expenses, use the add command. For example:

```shell
$ clexp add 5.95 food sandwich
Added:
01/15/2014	Food	sandwich	$5.95
```

Would add an entry in the category "Food" with the description "sandwich" and
the amount $5.95 and the current date. Categories and descriptions can also have
multiple words, if they're surrounded by quotes. For example:

```shell
$ clexp add 600 "new toys" "Motherboard, processor & memory"
Added:
01/15/2014	New Toys	Motherboard, processor & memory	$600.00
```

Would add an entry to the category "New Toys", with the description
"Motherboard, processor & memory". Categories are arbitrary, and you
can use any category structure you like. They are stored with the
first letter capitalized, so "new toys", "New Toys" and "NEW TOYS"
are all the same.

You can also add entries for a date in the past or future, by setting
the date as the fourth argument in MM/DD/YYYY format:

```shell
$ clexp add 5.95 food sandwich 01/25/2014
Added:
01/25/2014	Food	sandwich	$5.95

$ clexp add 751.37 rent "January Rent and water bill" 1/1/2014
Added:
01/01/2014	Rent	January Rent and water bill	$751.37

$ clexp add 749.18 rent "December rent and water bill" 12/1/2013
Added:
12/01/2013	Rent	December rent and water bill	$749.18
```

Adding Expenses - Advanced Usage
----------------
Calculations can be passed in to the amount field as well. For example, if you split
a $44 lunch bill evenly with two other people:
```shell
$ clexp add 44/3 Food "Lunch with Alice and Bob" 1/18/2014
Added:
01/18/2014	Food	Lunch with Alice and Bob	$14.67
```

Reporting
----------------
Several different reporting commands are available. Generally they work with the
format:
```shell
clexp <command> [year] [month] [category]
```
Year, month and category are all optional. You can specify year, year and month, or
year, month and category. If all three parameters are omitted, every entry in the
data file will be used.

Detail View
================
The detail command is used to give a total for each category:
```shell
$ clexp detail
Amount spent:
	Food                 $     26.57
	New Toys             $    600.00
	Rent                 $  1,500.55

	Total:               $  2,127.12
```

Or using the year to show only 2014:
```shell
$ clexp detail 2014
Amount spent in 2014:
	Food                 $     26.57
	New Toys             $    600.00
	Rent                 $    751.37

	Total:               $  1,377.94
```


Totals
================
The totals command shows the total amount spent each month:
```shell
$ clexp totals
Total Spent:
  12/2013: $  749.18
  01/2014: $1,377.94
```

List
================
To list individual expenses, use the list command. To list expenses in a given year, use:

```shell
$ clexp list 2014
01/01/2014	Rent	January Rent and water bill	$751.37
01/18/2014	Food	sandwich	$5.95
01/18/2014	New Toys	Motherboard, processor & memory	$600.00
01/18/2014	Food	Lunch with Alice and Bob	$14.67
01/25/2014	Food	sandwich	$5.95
```

List a specific month by adding the month number (1-12) with:

```shell
$ clexp list 2014 1
01/01/2014	Rent	Rent and water bill	$751.37
01/15/2014	Food	sandwich	$5.95
01/15/2014	New Toys	Motherboard, processor & memory	$600.00
01/25/2014	Food	sandwich	$5.95
```

Finally, you can list a certain category in a month:

```shell
$ clexp list 2014 1 food
01/18/2014	Food	sandwich	$5.95
01/18/2014	Food	Lunch with Alice and Bob	$14.67
01/25/2014	Food	sandwich	$5.95
```




Other Output Commands
----------------

Summary
================
The summary command will show the amount spent in the current month and
compare it to the previous month and year. It takes no arguments

```shell
$ clexp summary
Total spent:
             This month: $1,377.94
             Last month: $  749.18
   This month last year: $    0.00

Average spent per day:
             This month: $   76.55
             Last month: $   24.17
   This month last year: $    0.00
```



Categories
================
The categories command lists every category found in the data file. It takes no
arguments. For example:
```shell
$ clexp categories
Categories:
  Food
  New Toys
  Rent
```
