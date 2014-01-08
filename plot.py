import datetime

import matplotlib.pyplot as pyplot
from matplotlib.dates import MonthLocator, DateFormatter

import clexp


def temp_plot(dates, mean_temps):

    year_start = dates[0]
    days = [(d - year_start).days + 1 for d in dates]
    plot = pyplot.figure()
    fig, ax = plot.subplots(1)
    pyplot.title('Money Spent')
    pyplot.ylabel('Amount $')
    pyplot.xlabel('Month')
    padding = datetime.timedelta(days=21)
    pyplot.xlim([min(dates) - padding, max(dates) + padding])
    months = MonthLocator(range(1,13), bymonthday=1, interval=1)
    months_format = DateFormatter("%b '%y")
    ax = pyplot.axes()
    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(months_format)
    ax.xaxis.grid(False, 'major')
    ax.xaxis.grid(True, 'minor')
    ax.grid(True)
    fig.autofmt_xdate()
    ax.autoscale_view()

    #pyplot.plot(days, range(len(days)), marker='o')
    pyplot.plot(days, mean_temps, color='red', label='total')
    pyplot.legend(loc='upper right')
    return fig

def make_plot(dates, data):
    o = pyplot
    o.title('Money Spent')
    o.ylabel('Amount')
    o.xlabel('Month')
    o.gca().xaxis.set_major_formatter(DateFormatter('%b %Y'))
    o.gca().xaxis.set_major_locator(MonthLocator())
    o.gca().grid(False, 'major')
    o.gca().grid(True, 'minor')
    o.gca().grid(True)

    o.plot(dates, data, label='Total', linewidth=3)
    o.gcf().autofmt_xdate()
    o.xticks(rotation=45)
    o.fill_between(dates, data, [0]*len(data), facecolor='blue', alpha=0.2)
    return o


expenses = clexp.load_data('/data/expense/Expenses - US.csv')
data = expenses.get_month_totals()




dates = [q[0] for q in data]
totals = [q[1] for q in data]

width = 20       # the width of the bars

fig = make_plot(dates, totals)

c = 0
for category in expenses.categories:
    c += 1
    if c < 5:
        ls = 'solid'
    else:
        ls = 'dashed'
    linedata = []
    for year in expenses.get_years():
        for month in expenses.get_months(year):
            linedata.append(expenses.get_total(year, month, category))
    fig.plot(dates, linedata, label=category, linewidth=1, linestyle=ls)
fig.legend(loc='upper right')
fig.show()


#print linedata
    #rects.append(ax.bar(dates, linedata, width, align='center'))

#rects.append(ax.bar(dates, totals, width, align='center'))
#rects.append(ax.bar(dates, totals, width, align='center', bottom=totals))
#padding = datetime.timedelta(days=21)
#plt.xlim([min(dates) - padding, max(dates) + padding])
#ax.xaxis.set_major_locator(months)
#ax.xaxis.set_major_formatter(monthsFmt)

#ax.autoscale_view()
#ax.xaxis.grid(False, 'major')
#ax.xaxis.grid(True, 'minor')
#ax.grid(True)

#fig.autofmt_xdate()

#plt.show()