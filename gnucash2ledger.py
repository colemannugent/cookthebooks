#!/usr/bin/env python3

import argparse
import sys
import xml.etree.ElementTree as ET
from Split import *

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

def safety_text(element):
	if hasattr(element, 'text'):
		return element.text
	else:
		return None

# Define our XML namespaces for easy translation
ns = {  'gnc': 'http://www.gnucash.org/XML/gnc',
	'act': 'http://www.gnucash.org/XML/act',
	'book': 'http://www.gnucash.org/XML/book',
	'cd': 'http://www.gnucash.org/XML/cd',
	'cmdty': 'http://www.gnucash.org/XML/cmdty',
	'price': 'http://www.gnucash.org/XML/price',
	'slot': 'http://www.gnucash.org/XML/slot',
	'split': 'http://www.gnucash.org/XML/split',
	'sx': 'http://www.gnucash.org/XML/sx',
	'trn': 'http://www.gnucash.org/XML/trn',
	'ts': 'http://www.gnucash.org/XML/ts',
	'fs': 'http://www.gnucash.org/XML/fs',
	'bgt': 'http://www.gnucash.org/XML/bgt',
	'recurrence': 'http://www.gnucash.org/XML/recurrence',
	'lot': 'http://www.gnucash.org/XML/lot',
	'addr': 'http://www.gnucash.org/XML/addr',
	'billterm': 'http://www.gnucash.org/XML/billterm',
	'bt-days': 'http://www.gnucash.org/XML/bt-days',
	'bt-prox': 'http://www.gnucash.org/XML/bt-prox',
	'cust': 'http://www.gnucash.org/XML/cust',
	'employee': 'http://www.gnucash.org/XML/employee',
	'entry': 'http://www.gnucash.org/XML/entry',
	'invoice': 'http://www.gnucash.org/XML/invoice',
	'job': 'http://www.gnucash.org/XML/job',
	'order': 'http://www.gnucash.org/XML/order',
	'owner': 'http://www.gnucash.org/XML/owner',
	'taxtable': 'http://www.gnucash.org/XML/taxtable',
	'tte': 'http://www.gnucash.org/XML/tte',
	'vendor': 'http://www.gnucash.org/XML/vendor'}

# Parse our XML file and get the root
tree = ET.parse(args.file)
root = tree.getroot()

# iterate through all transactions
for transaction in root.iterfind('gnc:book/gnc:transaction', ns):
	for split in transaction.find('trn:splits', ns).iterfind('trn:split', ns):
		temp = Split(safety_text(split.find('split:id', ns)),
				safety_text(split.find('split:memo', ns)),
				safety_text(split.find('split:reconciled-state', ns)),
				safety_text(split.find('split:reconcile-date', ns)),
				safety_text(split.find('split:value', ns)),
				safety_text(split.find('split:quantity', ns)),
				safety_text(split.find('split:account', ns)),
				safety_text(split.find('split:slot', ns)))
		temp.display()
		print()
