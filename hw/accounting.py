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
import calendar

def parse_command_line(raw_command_line):
    return raw_command_line[1:]

def parse_csv(filename):
    """
    Reads the csv file corresponding to filename,
    then iterates over the entries tracking total
    revenue, revenue by client, and revenue by
    month. Finally, printing this information.
    """
    client_to_rvnu = dict()
    agg_rvnu = 0
    month_to_rvnu = dict()

    with open(filename) as f:
        f.readline()
        for line in f.readlines():
            # rsplit is used, and the number of splits is limited in
            # order to remove the delimiting commas while accounting
            # for the use of commas in the corporate name, legal status syntax
            client, qnty, price, date = line.rsplit(",", 3)
            client = client.strip(' " ').lower() # standardize client names
            rvnu = float(qnty)*float(price)
            month = date[:7]

            # add new revenue to client_to_rvnu
            if client in client_to_rvnu.keys():
                client_to_rvnu[client] += rvnu
            else:
                client_to_rvnu[client] = rvnu

            agg_rvnu += rvnu
            # add new revenue to month-end sales
            if month in month_to_rvnu.keys():
                month_to_rvnu[month] += rvnu
            else:
                month_to_rvnu[month] = rvnu

    largest_client = max(client_to_rvnu, key=lambda x: client_to_rvnu[x])
    print(f"Largest Client by revenue: {largest_client.title()}")
    print(f"Aggregate sales revenue: {agg_rvnu}")
    print("Month-end sales revenue:")
    for month in sorted(month_to_rvnu):
        last_day = calendar.monthrange(int(month[:4]), int(month[5:]))[1]
        print(f"{month}-{last_day},\t{month_to_rvnu[month]}")


if __name__ == "__main__":
    files_to_parse = parse_command_line(sys.argv)
    last_file = files_to_parse[-1]
    print("Beginning parse of", last_file)
    parse_csv(last_file)
