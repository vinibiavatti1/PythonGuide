"""
CSV

* The csv module is used to read and write CSV (Comma Separated Values) files.
* CSV files are used to store tabular data in a plain text format.
* The module provides two main ways to manipulate data in CSV files:
  * 1. Data as list (reader and writer)
  * 2. Data as dict (DictReader and DictWriter)
* NOTE: Since this module doesn't support in-memory operations, we will
  use a io.StringIO object as an in-memory file-like object.
"""


###############################################################################
# Module Import
###############################################################################


# Importing the module
# * We can import this module using the `import` statement as follows
# * NOTE: We will also import the io module to use StringIO as an in-memory
#   file-like object
import csv, io


###############################################################################
# Read & Write
###############################################################################


# Read and Write (List Format)
# * We will use a CSV file to demonstrate the read and write operations
# * The csv.reader and csv.writer functions can be used to read and write
#   data in the CSV file using lists
rows = [
    ['name', 'value'],
    ['example', 42],
    ['another_example', 100]
]
with io.StringIO() as x:
    csv_writer = csv.writer(x, delimiter=',')
    csv_writer.writerows(rows)  # Write rows (header + data)
    x.seek(0)  # Move to the beginning of the file-like object
    csv_reader = csv.reader(x, delimiter=',')
    for row in csv_reader:
        print(row)
# ['name', 'value']
# ['example', '42']
# ['another_example', '100']


# Read and Write (Dictionary Format)
# * We will use a CSV file to demonstrate the read and write operations using
#   the dictionary format
# * The csv.DictReader and csv.DictWriter classes can be used to read and write
#   data in the CSV file using dictionaries
# * NOTE: Note that the dictionary format already supports headers, so we
#   don't need to manage the header separately
header = ['name', 'value']
data = [
    {'name': 'example', 'value': 42},
    {'name': 'another_example', 'value': 100}
]
with io.StringIO() as x:
    csv_writer = csv.DictWriter(x, fieldnames=header, delimiter=',')
    csv_writer.writeheader()  # Write header
    csv_writer.writerows(data)  # Write rows (only data)
    x.seek(0)  # Move to the beginning of the file-like object
    csv_reader = csv.DictReader(x, delimiter=',')
    for row in csv_reader:
        print(row)
# {'name': 'example', 'value': '42'}
# {'name': 'another_example', 'value': '100'}
