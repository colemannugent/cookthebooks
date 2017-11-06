#!/usr/bin/env python3

import argparse
import sys
import xml.etree.ElementTree as ET

from Split import *
from Account import *
from Transaction import *
from Utils import *

# Create our argument parser object
parser = argparse.ArgumentParser(description='Convert gnucash files to ledger files')

# Add our arguments to the parser
parser.add_argument("file", help="Path to the file to convert")

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

# iterate through all accounts
for account in root.iterfind('gnc:book/gnc:account', ns):
	temp = parse_account(account)
	temp.display()
	print()

# iterate through all transactions
for transaction in root.iterfind('gnc:book/gnc:transaction', ns):
	temp = parse_transaction(transaction)
	temp.display()
	print()

# TODO:
# Iterate through all accounts
#	- Generate a list of Account objects
#	- Be able to translate guids to account names
# Sort transactions by time
#	- Which time? 
# Start building translation layer to ledger format
#	- Identify main parts of ledger format
