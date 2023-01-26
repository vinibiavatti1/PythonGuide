"""
Time module

* The time module is principally for working with unix time stamps
* The datetime module can support many of the same operations, but provides a
  more object oriented set of types, and also has some limited support for time
  zones
"""
import time


###############################################################################
# General
###############################################################################


# time()
# * The time() function returns the number of seconds passed since epoch
# * For Unix system, January 1, 1970, 00:00:00 at UTC is epoch (the point where
#   time begins).
seconds = time.time()
print(seconds)
# 1615286635.3070834


# ctime(seconds)
# * The time.ctime() function takes seconds passed since epoch as an argument
#   and returns a string representing local time.
seconds = 1615286635.3070834
local_time = time.ctime(seconds)
print(local_time)
# Tue Mar  9 10:43:55 2021


# sleep(seconds)
# * The sleep() function suspends (delays) execution of the current thread for
#   the given number of seconds
time.sleep(1)


###############################################################################
# Struct time class
# * Several functions in the time module such as gmtime(), asctime() etc.
#   either take time.struct_time object as an argument or return it
###############################################################################
# Index	        Attribute	        Values
###############################################################################
# 0	            tm_year	            0000, ...., 2018, ..., 9999
# 1	            tm_mon	            1, 2, ..., 12
# 2	            tm_mday	            1, 2, ..., 31
# 3	            tm_hour	            0, 1, ..., 23
# 4	            tm_min	            0, 1, ..., 59
# 5	            tm_sec	            0, 1, ..., 61
# 6	            tm_wday	            0, 1, ..., 6; Monday is 0
# 7	            tm_yday	            1, 2, ..., 366
# 8	            tm_isdst            0, 1 or -1
###############################################################################


# struct_time(time_tuple)
# * Creates struct time
time_tuple = (2018, 12, 27, 6, 35, 17, 3, 361, 0)
struct = time.struct_time(time_tuple)
print(struct)
# time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, tm_hour=6, tm_min=35,
# tm_sec=17, tm_wday=3, tm_yday=361, tm_isdst=0)


# localtime(seconds)
# * The localtime() function takes the number of seconds passed since epoch as
#   an argument and returns struct_time in local time
seconds = 1615286635.3070834
struct = time.localtime(seconds)
print(struct)
# time.struct_time(tm_year=2021, tm_mon=3, tm_mday=9, tm_hour=10, tm_min=43,
# tm_sec=55, tm_wday=1, tm_yday=68, tm_isdst=0)


# gmtime(seconds)
# * The gmtime() function takes the number of seconds passed since epoch as an
#   argument and returns struct_time in UTC
seconds = 1615286635.3070834
struct = time.gmtime(seconds)
print(struct)
# time.struct_time(tm_year=2021, tm_mon=3, tm_mday=9, tm_hour=10, tm_min=43,
# tm_sec=55, tm_wday=1, tm_yday=68, tm_isdst=0)


# mktime(struct_time or time_tuple)
# * The mktime() function takes struct_time (or a tuple containing 9 elements
#   corresponding to struct_time) as an argument and returns the seconds passed
#   since epoch in local time. Basically, it's the inverse function of
#   localtime()
time_tuple = (2018, 12, 27, 6, 35, 17, 3, 361, 0)
seconds = time.mktime(time_tuple)
print(seconds)
# 1545892517.0


# asctime(struct_time or time_tuple)
# * The asctime() function takes struct_time (or a tuple containing 9 elements
#   corresponding to struct_time) as an argument and returns a string
#   representing it
time_tuple = (2018, 12, 27, 6, 35, 17, 3, 361, 0)
representation = time.asctime(time_tuple)
print(representation)
# Thu Dec 27 06:35:17 2018


# strftime(format, struct_time or time_tuple)
# * The strftime() function takes struct_time (or tuple corresponding to it) as
#   an argument and returns a string representing it based on the format code
#   used
# NOTE: Check the _datetime.py file for strftime formats
time_tuple = time.localtime()  # Get struct time for now
representation = time.strftime('%d/%m/%Y %H/%M/%S', time_tuple)
print(representation)
# 09/03/2021 11/03/58


# strptime(time_string, format)
# * The strptime() function parses a string representing time and returns
#   struct_time
time_string = '09/03/2021 11/03/58'
struct = time.strptime(time_string, '%d/%m/%Y %H/%M/%S')
print(struct)
# time.struct_time(tm_year=2021, tm_mon=3, tm_mday=9, tm_hour=11, tm_min=3,
# tm_sec=58, tm_wday=1, tm_yday=68, tm_isdst=-1)
