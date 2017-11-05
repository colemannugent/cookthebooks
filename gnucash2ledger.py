#!/usr/bin/env python3

import argparse
import sys
import xml.etree.ElementTree as ET

from Split import *
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

# iterate through all transactions
for transaction in root.iterfind('gnc:book/gnc:transaction', ns):
	for split in transaction.find('trn:splits', ns).iterfind('trn:split', ns):
		temp = parse_split(split)
		temp.display()
		print()
