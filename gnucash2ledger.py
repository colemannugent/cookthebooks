#!/usr/bin/env python3

import argparse
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

from Split import *
from Account import *
from Transaction import *
from Utils import *

# Create our argument parser object
parser = argparse.ArgumentParser(description='Convert gnucash files to ledger files')

# TODO: Add arguments for output to file or to stdout
# Add our arguments to the parser
parser.add_argument("file", help="Path to the file to convert")

# TODO: Check to see if the file is gzipped and take care of it
# Make sure we have enough arguments, if not print the help message
if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

# Actually parse the arguements
args = parser.parse_args()

#TODO: Make sure the file exists before attempting to read it
print("File:", args.file)

# Parse our XML file and get the root
tree = ET.parse(args.file)
root = tree.getroot()

# list of all accounts
accounts = []

# iterate through all accounts
for account in root.iterfind('gnc:book/gnc:account', ns):
	temp = parse_account(account)
	accounts.append(temp)

# TODO: Pre-generate accounts at top of ledger file and impose assertions: http://ledger-cli.org/3.0/doc/ledger3.html#Command-Directives

print("Found", len(accounts), "accounts")

# Obtain the full name for each account
for account in accounts:
	account.fullname = get_fullname(account, accounts)

# Display the root account
#accounts[0].display()

# iterate through all transactions and build a list
transactions = []
for transaction in root.iterfind('gnc:book/gnc:transaction', ns):
	temp = parse_transaction(transaction)
	temp.date = datetime.strptime(temp.date_posted, "%Y-%m-%d %H:%M:%S %z")
	transactions.append(temp)

# Sort transactions by date
#for transaction in transactions:
	#transaction.display()

transactions.sort(key=lambda item: item.date)
for transaction in transactions:
	translate_to_ledger(transaction, accounts)
