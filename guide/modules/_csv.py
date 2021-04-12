"""
CSV module

* The CSV module provides tools to work with CSV files
* This module has two ways to manipulate data in CSV files:
  * 1. Data as list (reader and writer)
  * 2. Data as dict (DictReader and DictWriter)
"""
import csv
import sys
import os


###############################################################################
# File Paths
###############################################################################
CSV_FILE_READ = os.path.join(sys.path[0], '../../resources/data_read.csv')
CSV_FILE_WRITE = os.path.join(sys.path[0], '../../resources/data_write.csv')


###############################################################################
# Read
###############################################################################


# Read data using reader
# * The reader function in csv module reads the csv file and put each line
#   separated by the delimiter into a list iterator
# * NOTE: To remove the header just go next to the next item in iterator
# * NOTE: The default value for the delimiter is the comma
with open(CSV_FILE_READ) as f:
    csv_reader = csv.reader(f, delimiter=',')
    next(csv_reader)  # Remove header
    for line in csv_reader:
        print(line)
# ['1', 'Tildie', 'Cavan', 'tcavan0@ning.com', 'Genderqueer', '66.118.5.70']
# ['2', 'Jenna', 'Youngs', 'jyoungs1@oracle.com', 'Bigender', '232.125.225.71']
# ['3', 'Ellene', 'Hick', 'ehick2@ustream.tv', 'Bigender', '19.69.158.33']
# ...


# Read data using DictReader
# * The DictReader class in csv module reads the csv file and put each line
#   separated by the delimiter into a dict iterator
# * NOTE: For this example the header does not need to be removed manually
#   cause the DictReader will use this to create the dict values
with open(CSV_FILE_READ) as f:
    csv_reader = csv.DictReader(f, delimiter=',')
    for dct in csv_reader:
        print(dct)
# {'id': '1', 'first_name': 'Tildie', 'last_name': 'Cavan', 'email': ...}
# {'id': '2', 'first_name': 'Jenna', 'last_name': 'Youngs', 'email': ...}
# {'id': '3', 'first_name': 'Ellene', 'last_name': 'Hick', 'email': ...}


###############################################################################
# Write
###############################################################################


# Write data using writer
# * The write function in csv module creates a writer object to write lines in
#   the CSV file by list
# * NOTE: For values that contains commas (,), the writer put the values inside
#   double quotes
# * NOTE: The newline was put in open() function to prevent blanklines during
#   the processing of the file
header = ('id', 'first_name', 'last_name')
data = [
    [1, 'Tildie,Cavan', 'tcavan0@ning.com'],
    [2, 'Jenna,Youngs', 'jyoungs1@oracle.com'],
]
with open(CSV_FILE_WRITE, 'w', newline='') as f:
    csv_writer = csv.writer(f, delimiter=',')
    csv_writer.writerow(header)  # Write single line
    csv_writer.writerows(data)   # Write multiple lines
# File content:
# id,first_name,last_name
# 1,"Tildie,Cavan",tcavan0@ning.com
# 2,"Jenna,Youngs",jyoungs1@oracle.com


# Write data using DictWriter
# * The DictWriter class in csv module creates a writer object to write lines
#   in the CSV file by dict
# * The delimiter was changed to (;) char in this example
# * NOTE: For values that contains commas (,), the writer put the values inside
#   double quotes
# * NOTE: The newline was put in open() function to prevent blanklines during
#   the processing of the file
header = ('id', 'first_name', 'last_name')
data = [
    dict(id=1, first_name='Tildie,Cavan', last_name='tcavan0@ning.com'),
    dict(id=2, first_name='Jenna,Youngs', last_name='jyoungs1@oracle.com'),
]
with open(CSV_FILE_WRITE, 'w', newline='') as f:
    csv_writer = csv.DictWriter(f, header, delimiter=';')
    csv_writer.writeheader()    # Write header
    csv_writer.writerows(data)  # Write data
# File content:
# id;first_name;last_name
# 1;Tildie,Cavan;tcavan0@ning.com
# 2;Jenna,Youngs;jyoungs1@oracle.com
