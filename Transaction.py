import math
from decimal import *

from Utils import *

# Attempt to import the money library
translate_currency_codes = True
try:
	from money import Money
except ImportError:
	output("Unable to import Money library. gnucash2ledger will be unable to translate currency codes into the correct unicode symbol and will subsequently try to treat all amounts as USD.  To enable support for currency code translation, please ensure you have installed the Money library: https://pypi.python.org/pypi/money/1.3.0", error=True)
	translate_currency_codes = False

from Utils import *
from Split import *
from Account import *

class Transaction:
	def __init__(self, guid, currency, date_posted, description, splits):
		self.guid = guid
		self.currency = currency
		self.date_posted = date_posted
		self.description = description
		self.splits = splits
		self.date = None

	def display(self):
		tree_print("Transaction", self, 0)

# Given an XML transaction, return a Transaction object
def parse_transaction(xml_transaction):
	splits = []
	for xml_split in xml_transaction.iterfind('trn:splits/trn:split', ns):
		splits.append(parse_split(xml_split))

	return Transaction(safety_text(xml_transaction.find('trn:id', ns)),
			safety_text(xml_transaction.find('trn:currency/cmdty:id', ns)),
			safety_text(xml_transaction.find('trn:date-posted/ts:date', ns)),
			safety_text(xml_transaction.find('trn:description', ns)),
			splits)

# Given a string representing the fractional quanity and the currency, return a nicely formatted string
def translate_quantity(string, currency):
	seperator = string.index("/")
	numerator = Decimal(string[:seperator])
	denominator = Decimal(string[seperator + 1:])

	if translate_currency_codes: 
		value = Money(numerator / denominator, currency)
		return value.format('en_US')
	else:
		return ("$" + (numerator / denominator))

# Actually translate the transactions
def translate_to_ledger(transaction, accounts, fileout=None):
	length = 40

	# Find an appropriate length based on the length of the longest split
	for split in transaction.splits:
		name = get_fullname(lookup_account(split.account, accounts), accounts)
		if len(name) > length:
			length = int(math.ceil(len(name) / 10.0)) * 10

	# Output the transaction header
	output(transaction.date.strftime("%Y/%m/%d") + " * " + transaction.description, outfile=fileout)

	# Iterate through each split in the transaction and output it
	for split in transaction.splits:

		name = get_fullname(lookup_account(split.account, accounts), accounts)
		quantity = translate_quantity(split.quantity, transaction.currency)

		if split.memo:
			output('  {0:<{width}} {1:>10} ;{2}'.format(name, quantity, split.memo, width=length), outfile=fileout)
		else:
			output('  {0:<{width}} {1:>10}'.format(name, quantity, width=length), outfile=fileout)

	# Output a blank line to separate the transactions
	output(outfile=fileout)
