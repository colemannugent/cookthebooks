#!/usr/bin/env python3

import argparse
import sys
import gzip
import os.path
import xml.etree.ElementTree as ET
from datetime import datetime

from Split import *
from Account import *
from Transaction import *
from Utils import *

# Create our argument parser object
parser = argparse.ArgumentParser(description='Convert gnucash files to ledger files')

# Add our arguments to the parser
parser.add_argument("file", help="Path to the gnucash file to convert")
parser.add_argument('-o','--outfile', dest='outfile',
		help="Output to a file instead of standard output")

# Make sure we have enough arguments, if not print the help message
if len(sys.argv) < 2:
	parser.print_help()
	sys.exit(1)

# Actually parse the arguments
arguments = parser.parse_args()

# Make sure the file exists before attempting to read it
if not os.path.exists(arguments.file):
	output(arguments.file, ": No such file exists", error=True)
	sys.exit(1)

# Alert the user if we need to output to a file and if that file already exists
if arguments.outfile and os.path.exists(arguments.outfile):
	output(arguments.outfile, "already exists, appending...", error=True)

# Check if the file is compressed or not and parse it
try:
	tree = ET.parse(gzip.open(arguments.file, 'r'))
except OSError:
	output("Assuming the file is not compressed, see the README for more info", error=True)

	tree = ET.parse(arguments.file)

# Get the root of our XML document
root = tree.getroot()

# Summon a list from the void
accounts = []

# Iterate through all account tags in the XML and parse them into Account objects
for account in root.iterfind('gnc:book/gnc:account', ns):
	temp = parse_account(account)

	# Add our new account to the list of all accounts
	accounts.append(temp)

output("Found", len(accounts), "accounts", error=True)

# Obtain the full name for each account
for account in accounts:
	account.fullname = get_fullname(account, accounts)

# Iterate through all XML transaction tags and build a list of Transaction objects
transactions = []
for transaction in root.iterfind('gnc:book/gnc:transaction', ns):
	temp = parse_transaction(transaction)

	# Convert the date given in the date_posted tag to the format ledger uses
	temp.date = datetime.strptime(temp.date_posted, "%Y-%m-%d %H:%M:%S %z")

	transactions.append(temp)

output("Found", len(transactions), "transactions", error=True)

# Sort transactions by date
# Note that if two transactions have the same date we rely on gnucash keeping them
# in the correct order as there is no way to tell which transaction came first
transactions.sort(key=lambda item: item.date)

# Iterate over our sorted transactions and translate them to the ledger format
for transaction in transactions:
	translate_to_ledger(transaction, accounts, fileout=arguments.outfile)
