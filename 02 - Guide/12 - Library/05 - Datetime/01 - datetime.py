"""
Datetime

* The datetime module provides date and time operations
* It includes classes for manipulating dates and times in both simple and
  complex ways
* The module has two main functions to parse and format dates:
  * datetime.strptime(date_str, format) = Parse string to datetime
  * date.strftime(format) = Format datetime to string
* The parse and format functions have directives to specify the datetime format
  These directives are listed below:
###############################################################################
Code  Meaning                                Example
###############################################################################
Standard
%a    Weekday abbreviated name               Sun, Mon, Sat
%A    Weekday full name                      Sunday, Monday, Saturday
%w    Weekday number                         0, 1, 6
%d    Day of the month                       01, 02, 31
%b    Month abbreviated name                 Jan, Feb, Dec
%B    Month full name                        January, February, December
%m    Month                                  01, 02, 12
%y    Year without century                   00, 01, 99
%Y    Year with century                      0001, 2025, 9999
%H    Hour (24)                              00, 01, 23
%I    Hour (12)                              01, 02, 12
%p    AM or PM                               AM, PM
%M    Minute                                 00, 01, 59
%S    Second                                 00, 01, 59
%f    Microsecond                            000000, 000001, 999999
%z    UTC offset                             (empty), +0000, -0400
%Z    Time zone name                         (empty), UTC, GMT
%j    Day of the year                        001, 002, 366
%U    Week number of the year (Sun first)    00, 01, 53
%W    Week number of the year (Mon first)    00, 01, 53
%c    Date and time repr                     Tue Aug 16 21:30:00 1988
%x    Date repr                              08/16/1988
%X    Time representation                    21:30:00
%%    Literal '%' character                  %
###############################################################################
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
from datetime import datetime, timedelta, timezone


###############################################################################
# Parse & Format
###############################################################################


# Parsing a datetime (string to datetime)
# * To parse a string to a datetime object, we can use the `strptime()`
#   function
# * The first argument is the string to parse and the second argument is the
#   format to use
# * It also works with only dates or times
# * The directives on the top of this file can be used to specify the format
x = '15/09/1994 17:30:25'
y = datetime.strptime(x, '%d/%m/%Y %H:%M:%S')
print(y)
# 1994-09-15 17:30:25


# Formatting a datetime (datetime to string)
# * To format a datetime object to a string, we can use the `strftime()`
#   function
# * The argument is the format to use
# * The directives on the top of this file can be used to specify the format
x = datetime(1994, 9, 15, 17, 30, 25)
y = x.strftime('%d/%m/%Y %H:%M:%S')
print(y)
# 15/09/1994 17:30:25


###############################################################################
# Datetime Object
###############################################################################


# Creating a datetime object
# * We can create a datetime object using the `datetime()` constructor
# * The arguments are the values for the date and time attributes
x = datetime(2020, 3, 5, 17, 30, 20)
print(x)
# 2020-03-05 17:30:20


# Creating a datetime object (with current date and time)
# * We can use the `today()` method to create a datetime object with the
#   current date and time
# * The `now()` method can also be used to create a datetime object with the
#   current date and time, but it allows setting a timezone
x1 = datetime.today()
x2 = datetime.now(tz=timezone.utc)
print(x1, x2)
# 2021-03-03 17:05:28.886813
# 2021-03-03 17:05:28.886813+00:00


# Attributes
# * The datetime object has attributes to access the date and time values
x = datetime(2020, 3, 5, 17, 30, 20, 500)
print(x.year)         # 2020
print(x.month)        # 3
print(x.day)          # 5
print(x.hour)         # 17
print(x.minute)       # 30
print(x.second)       # 20
print(x.microsecond)  # 500


# Week day
# * To retrieve the week day from a datetime object, we can use the
#   `weekday()` or `isoweekday()` methods
# * weekday:    Monday is 0 and Sunday is 6
# * isoweekday: Monday is 1 and Sunday is 7
x = datetime(2020, 3, 5, 10, 30)
y1 = x.weekday()
y2 = x.isoweekday()
print(y1, y2)
# 3, 4


# Updating a datetime object
# * We can update the attributes of a datetime object using the `replace()`
#   method
# * The method returns a new datetime object with the updated attributes
x = datetime(2020, 3, 5, 17, 30, 20)
y = x.replace(year=1994, hour=12, minute=0)
print(y)
# 1994-03-05 12:30:20


###############################################################################
# Timedelta Object
###############################################################################


# Difference between two datetimes
# * A timedelta object represents the difference between two datetimes
# * The Python arithmetic operators can be used to generate a timedelta
# * NOTE: The timedelta can return negative values if the second datetime is
#   far from the first datetime
x1 = datetime(2020, 9, 15, 10, 30, 25)
x2 = datetime(1994, 5, 12, 12, 2, 50)
delta = x1 - x2
print(delta)
# 9497 days, 22:27:35


# Incrementing a datetime
# * To add days, hours or any value for the datetime, the timedelta can be
#   used
# * We have to use the operator '+' to add the timedelta to the datetime
x = datetime(2024, 1, 1, 2, 30, 15)
y = timedelta(years=1, months=8, days=14, hours=5, minutes=15, seconds=30)
z = x + y
print(z)
# 2025-09-15 07:45:45


# Decrementing a datetime
# * To subtract days, hours or any value for the datetime, the timedelta can
#   be used
# * We have to use the operator '-' to subtract the timedelta from the datetime
x = datetime(2024, 1, 1, 2, 30, 15)
y = timedelta(years=1, months=8, days=14, hours=5, minutes=15, seconds=30)
z = x - y
print(z)
# 2022-04-17 21:14:45


###############################################################################
# Timezone Object
###############################################################################


# Creating a timezone object
# * A timezone object represents a fixed offset from UTC
# * The timezone can be created using the `timezone()` class
# * The argument for timezone must be a timedelta object
x = timezone(timedelta(hours=-5))
print(x)
# UTC-05:00


# Setting a timezone to a datetime object
# * To set a timezone to a datetime object, we can use the `astimezone()`
#   method
# * The argument for the method must be a timezone object
x = timezone(timedelta(hours=-5))
y = datetime(2021, 4, 22, 14, 34, 38)
z = y.astimezone(x)
print(z)
# 2021-04-22 09:34:38-05:00


# Getting the current datetime with timezone
# * To get the current datetime with a specific timezone, we can use the
#   `now()` method with the `tz` argument set to the timezone object
x = timezone(timedelta(hours=-5))
y = datetime.now(tz=x)
print(y)
# 2021-04-22 09:34:38.290535-05:00
