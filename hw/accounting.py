# 50 pts.
# You are the data scientist at an accounting firm.
# A new client gives you their inventory logs,
# but they are in horrible condition.
# No two files match!
#
# Your task is to write a generic parser that
# can extract relevant data.
#
# There are a few constants.  Phew!
# Assume every file is comma-separated.
# And that the headers use the same words:
# "Clientname"
# "Quantity"
# "Price"
# "Date"

# But, the casing is sometimes different (!!!).
# This means "date" and "dAte" sometimes
# appear.  And!
# client names also have random capitalization.

# Your script will be run from the command line.
# python accounting.py old_file0312202.csv
# with the script and the csv file.

# Your task is to print:
# largest client by revenue = quantity*price (20 pts.)
# aggregate sales revenue (20 pts.)
# month-end sales revenue (10 pts.)

# Note that month-end sales revenue includes all transactions
# for one month only, and should be dated the last day of the month.
# You are given three test files.
# Your code will have to correctly complete the task for the three csv's
# in this folder,
# and a secret fourth file of the same type.

# Bonus (+10pts)
# Have your script accept any number of inputs:
# python accounting.py old_data0312202.csv old_data032231d.csv new_data231.csv 
# and print the first three tasks on the aggregate parsed data.
# What else needs to change?
#
# Bonus (+10pts)
# If you can implement the bonus by adding
# one line of code and marginally modifying another line
# you get 10 more points.
# use comments to tell me about your design.
#
# Good luck!


import sys

def parse_command_line(raw_command_line):
    return raw_command_line[1:]

def parse_csv(filename):
    raise NotImplementedError

if __name__ == "__main__":
    files_to_parse = parse_command_line(sys.argv)
    last_file = files_to_parse[-1]
    print("Beginning parse of", last_file)
    parse_csv(last_file)
    
