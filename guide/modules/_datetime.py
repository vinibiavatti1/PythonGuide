"""
Datetime module

* Python has a module named datetime to work with dates and times
* Commonly used classes in the datetime module are:
  * date class
  * time class
  * datetime class
  * timedelta class

Strftime Formats
-------------------------------------------------------------------------------
Code        Meaning                                                 Example
-------------------------------------------------------------------------------
# Common
%m	        Month as a zero-padded decimal number.	                09
%d	        Day of the month as a zero-padded decimal number.	    30
%Y	        Year with century as a decimal number.	                2013
%H	        Hour (24-hour clock) as a zero-padded decimal number.	07
%M	        Minute as a zero-padded decimal number.	                06
%S	        Second as a zero-padded decimal number.	                05

# Not common
%a	        Weekday as locale’s abbreviated name.	                Mon
%A	        Weekday as locale’s full name.	                        Monday
%w	        Weekday as a decimal number, where 0 is Sunday and 6
            is Saturday.	                                        1
%-d	        Day of the month as a decimal number. (Platform
            specific)	                                            30
%b	        Month as locale’s abbreviated name.	                    Sep
%B	        Month as locale’s full name.	                        September
%-m	        Month as a decimal number. (Platform specific)	        9
%y	        Year without century as a zero-padded decimal number.	13
%-H	        Hour (24-hour clock) as a decimal number. (Platform     7
            specific)
%I	        Hour (12-hour clock) as a zero-padded decimal number.	07
%-I	        Hour (12-hour clock) as a decimal number. (Platform     7
            specific)
%p	        Locale’s equivalent of either AM or PM.	                AM
%-M	        Minute as a decimal number. (Platform specific)	        6
%-S	        Second as a decimal number. (Platform specific)	        5
%f	        Microsecond as a decimal number, zero-padded on the     000000
            left.
%z	        UTC offset in the form +HHMM or -HHMM (empty string
            if the the object is naive).
%Z	        Time zone name (empty string if the object is naive).
%j	        Day of the year as a zero-padded decimal number.	    273
%-j	        Day of the year as a decimal number. (Platform          273
            specific)
%U	        Week number of the year (Sunday as the first day of     39
            the week) as a zero padded decimal number. All days
            in a new year preceding the first Sunday are
            considered to be in week 0.
%W	        Week number of the year (Monday as the first day of     39
            the week) as a decimal number. All days in a new year
            preceding the first Monday are considered to be in
            week 0.
%c	        Locale’s appropriate date and time representation.	    Mon Sep 30
                                                                    07:06:05
                                                                    2013
%x	        Locale’s appropriate date representation.	            09/30/13
%X	        Locale’s appropriate time representation.	            07:06:05
%%	        A literal '%' character.	                            %
-------------------------------------------------------------------------------
* Reference: https://strftime.org/
"""
from datetime import date, datetime, timedelta
import time


# -----------------------------------------------------------------------------
# Date and datetime


# Get current date
current = date.today()
print(current)
# 2021-03-03


# Get current datetime
current = datetime.now()
print(current)
# 2021-03-03 17:05:28.886813


# Create date
my_date = date(2020, 3, 5)
print(my_date)
# 2020-03-05


# Create datetime
my_datetime = datetime(2020, 3, 5, 17, 30, 20)
print(my_datetime)
# 2020-03-05 17:30:20


# Get current timestemp
current_ts = time.time()
print(current_ts)
# 1614791610.5159419


# Get date from timestamp
ts_date = date.fromtimestamp(time.time())
print(ts_date)
# 2021-03-03


# Get date attributes
my_date = date(2020, 3, 5)
print(my_date.year)   # 2020
print(my_date.month)  # 3
print(my_date.day)    # 5


# Get datetime attributes
my_datetime = datetime(2020, 3, 5, 17, 30, 20, 500)
print(my_datetime.year)         # 2020
print(my_datetime.month)        # 3
print(my_datetime.day)          # 5
print(my_datetime.hour)         # 17
print(my_datetime.minute)       # 30
print(my_datetime.second)       # 20
print(my_datetime.microsecond)  # 500


# Get datetime timestemp
my_datetime = datetime(2020, 3, 5, 17, 30, 20, 500)
print(my_datetime.timestamp())
# 1583429420.0005


# -----------------------------------------------------------------------------
# Timedelta
# * A timedelta object represents the difference between two dates or times


# Difference between two dates
d1 = date(2020, 9, 15)
d2 = date(1994, 9, 15)
delta = d1 - d2
print(delta)        # 9497 days, 0:00:00
print(type(delta))  # <class 'datetime.timedelta'>
print(delta.days)   # 9497


# Difference between two timedeltas
t1 = timedelta(weeks=10, days=50, hours=18)
t2 = timedelta(days=5, hours=39)
delta = t1 - t2
print(delta)        # 114 days, 3:00:00
print(type(delta))  # <class 'datetime.timedelta'>
print(delta.days)   # 114


# Negative timedelta
t1 = timedelta(days=5)
t2 = timedelta(days=10)
delta = t1 - t2
print(delta)            # -5 days, 0:00:00
print(type(delta))      # <class 'datetime.timedelta'>
print(abs(delta.days))  # 5  NOTE: Used abs() to get absolute


# Time duration in seconds
t1 = timedelta(days=50)
print(t1.total_seconds())
# 4320000.0


# -----------------------------------------------------------------------------
# Format (strptime)
# * Syntax: date.strptime(format)


# Format date
my_date = date(2020, 3, 15)
formated = my_date.strftime('%d/%m/%Y')
print(formated)
# 15/03/2020


# Format datetime
my_datetime = datetime(2020, 3, 15, 17, 30, 45)
formated = my_datetime.strftime('%d/%m/%Y %H:%M:%S')
print(formated)
# 15/03/2020 17:30:45


# -----------------------------------------------------------------------------
# Parse string (strptime)
# * Syntax: strptime(string, format)


# Create datetime
date_str = '15/09/1994 17:30:25'
my_datetime = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
print(my_datetime)
# 1994-09-15 17:30:25


# Convert datetime to date
my_date = my_datetime.date()
print(my_date)
# 1994-09-15


# -----------------------------------------------------------------------------
# Timezone
