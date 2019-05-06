'''
Created on May 2, 2019

@author: 16605
'''
import pandas
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn
data = pandas.read_csv("C:/Users/16605/Desktop/uber-raw-data-apr14.txt")

dt = "4/30/2014 23:22:00"

dt = pandas.to_datetime(dt)
print()
print(dt)
print(dt.week)
print(dt.day)
print(dt.month)
print(dt.year)

data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)
def get_dom(dt):
    return dt.day
data['dom'] = data['Date/Time'].map(get_dom)
def get_weekday(dt):
    return dt.weekday()
data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)

plt.bar(range(1, 31), by_date)
plt.show()
for k, rows in data.groupby('dom'):
    print(k, rows)
plt.hist(data.dom, bins=30, rwidth=0.8, range=(0.5, 30.5))
plt.xlabel('date of month')
plt.ylabel('frequency')
plt.title('Frequency by DOM - Uber - April 2014')
plt.show()

data['hour'] = data['Date/Time'].map(get_hour)

plt.hist(data.weekday, bins = 7, range = (-0.5, 6.5), rwidth = 0.8, color = '#AA6666', alpha=0.4)
plt.xticks(range(7), 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split())
plt.show()

by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()
seaborn.heatmap(by_cross)
plt.show()