"""
Datetime module

* Python has a module named datetime to work with dates and times
* Commonly used classes in the datetime module are:
  * date class
  * time class
  * datetime class
  * timedelta class

Strftime Formats
###############################################################################
Code        Meaning                                                 Example
###############################################################################
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
###############################################################################
* Reference: https://strftime.org/
"""
from datetime import date, datetime, timedelta, MAXYEAR, MINYEAR
import time


###############################################################################
# Constants
###############################################################################


# Min Year
# * Contains the min year allowed to work with datetime module
print(MINYEAR)
# 1


# Max year
# * Contains the max year allowed to work with datetime module
print(MAXYEAR)
# 9999


###############################################################################
# Date
###############################################################################


# Current date
# * Create a date using the current date
current = date.today()
print(current)
# 2021-03-03


# Create date
# * Create a date specifing the values for the date attributes
# * Syntax
#   date(year, month, day)
my_date = date(2020, 3, 5)
print(my_date)
# 2020-03-05


# Get date attributes
# * Get the attributes from a date (year, month, day)
my_date = date(2020, 3, 5)
print(my_date.year)   # 2020
print(my_date.month)  # 3
print(my_date.day)    # 5


# Replace date attributes
# * Replace the attributes for some date
my_date = date(2020, 3, 5)
my_date = my_date.replace(year=1994, month=9, day=15)
print(my_date)
# 1994-09-15


###############################################################################
# Datetime
###############################################################################


# Current datetime
# * Create a datetime using the current date and time
current = datetime.now()
print(current)
# 2021-03-03 17:05:28.886813


# Create datetime
# * Create a datetime specifing the values for the date and time attributes
# * Syntax
#   datetime(year, month, day[, hour[, minute[, second[, microsecond]]]])
my_datetime = datetime(2020, 3, 5, 17, 30, 20)
print(my_datetime)
# 2020-03-05 17:30:20


# Get datetime attributes
# * Get the attributes from a datetime
#   (year, month, day, hour, minute, second, microsecond)
my_datetime = datetime(2020, 3, 5, 17, 30, 20, 500)
print(my_datetime.year)         # 2020
print(my_datetime.month)        # 3
print(my_datetime.day)          # 5
print(my_datetime.hour)         # 17
print(my_datetime.minute)       # 30
print(my_datetime.second)       # 20
print(my_datetime.microsecond)  # 500


# Replace datetime attributes
# * Replace the attributes for some datetime
my_datetime = datetime(2020, 9, 15, 10, 30, 00)
my_datetime = my_datetime.replace(year=1994, hour=17, minute=30)
print(my_datetime)
# 1994-09-15 17:30:00


###############################################################################
# Timestemp
###############################################################################


# Current timestemp
# * Return the current timestemp as float
current_ts = time.time()
print(current_ts)
# 1614791610.5159419


# Create date from timestamp
# * Create a date from timestemp (float)
current_ts = time.time()
my_date = date.fromtimestamp(current_ts)
print(my_date)
# 2021-03-03


# Get timestemp from datetime
# * Get the timestemp (float) from datetime object
my_datetime = datetime(2020, 3, 5, 17, 30, 20, 500)
ts = my_datetime.timestamp()
print(ts)
# 1583429420.0005


###############################################################################
# Timedelta
###############################################################################


# Difference between two dates
# * A timedelta object represents the difference between two dates or times
# * The Python aritmetic operators can be used to generate a timedelta
d1 = date(2020, 9, 15)
d2 = date(1994, 9, 15)
delta = d1 - d2
print(delta)        # 9497 days, 0:00:00
print(type(delta))  # <class 'datetime.timedelta'>
print(delta.days)   # 9497


# Difference between two timedeltas
# * Get the difference between two timedeltas using '-' operator
t1 = timedelta(weeks=10, days=50, hours=18)
t2 = timedelta(days=5, hours=39)
delta = t1 - t2
print(delta)        # 114 days, 3:00:00
print(type(delta))  # <class 'datetime.timedelta'>
print(delta.days)   # 114


# Negative timedelta
# * The timedelta can return negative values if the second date is far the the
#   first date
# * To get the absolute value, the abs() function can be used
t1 = timedelta(days=5)
t2 = timedelta(days=10)
delta = t1 - t2
print(delta)            # -5 days, 0:00:00
print(type(delta))      # <class 'datetime.timedelta'>
print(abs(delta.days))  # 5  NOTE: Used abs() to get absolute


# Time duration in seconds
# * Get the time duration in seconds (float) from a timedelta
t1 = timedelta(days=50)
print(t1.total_seconds())
# 4320000.0


# Incrementing the date
# * To add days, hours or any value for the date, the timedelta can be used
# * The operator '+' was used to add
my_date = date(2020, 1, 1)
add = timedelta(days=14)
my_date = my_date + add
print(my_date)
# 2020-01-15


# Decrementing the date
# * To subtract days, hours or any value for the date, the timedelta can be
#   used
# * The operator '-' was used to subtract
my_date = date(2020, 1, 1)
add = timedelta(days=14)
my_date = my_date - add
print(my_date)
# 2019-12-18


###############################################################################
# Format (strftime)
###############################################################################


# Format datetime
# * Create a string version of the datetime by a format
# * NOTE: The formats on the top of this file can be used
# * Syntax: datetime_obj.strptime(format)
my_datetime = datetime(2020, 3, 15, 17, 30, 45)
formated = my_datetime.strftime('%d/%m/%Y %H:%M:%S')
print(formated)
# 15/03/2020 17:30:45


# Format date
# * Create a string version of the date by a format
# * NOTE: The formats on the top of this file can be used
# * Syntax: date_obj.strptime(format)
my_date = date(2020, 3, 15)
formated = my_date.strftime('%d/%m/%Y')
print(formated)
# 15/03/2020


###############################################################################
# Parse string (strptime)
# * Syntax: strptime(string, format)
###############################################################################


# Parse datetime
# * Create a datetime version of the string by a format
# * NOTE: The formats on the top of this file can be used
# * Syntax: date.strftime(format)
date_str = '15/09/1994 17:30:25'
my_datetime = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
print(my_datetime)
# 1994-09-15 17:30:25


# Parse date
# * NOTE: There is no way to parse only a date using strptime(). For this, we
#   must create the datetime object and then, convert to date
date_str = '15/09/1994'
my_datetime = datetime.strptime(date_str, '%d/%m/%Y')
my_date = my_datetime.date()
print(my_date)
# 1994-09-15


###############################################################################
# Timezone
###############################################################################
# TODO
