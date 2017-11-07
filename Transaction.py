import math
from decimal import *

# Attempt to import the money library
translate_currency_codes = True
try:
	from money import Money
except ImportError:
	print("Unable to import Money library. gnucash2ledger will be unable to translate")
	print("currency codes into the correct unicode symbol and will subsequently try to")
	print("treat all amounts as USD. ")
	print("To enable support for currency code translation, please ensure you have")
	print("installed the Money library: https://pypi.python.org/pypi/money/1.3.0")
	translate_currency_codes = False

from Utils import *
from Split import *
from Account import *

class Transaction:
	def __init__(self, guid, currency, date_posted, date_entered, description, slots, splits):
		self.guid = guid
		self.currency = currency
		self.date_posted = date_posted
		self.date_entered = date_entered
		self.description = description
		self.slots = slots
		self.splits = splits
		self.date = None

	def display(self):
		tree_print("Transaction", self, 0)

# Not yet implemented:
# Slots
def parse_transaction(xml_transaction):
	splits = []
	for xml_split in xml_transaction.iterfind('trn:splits/trn:split', ns):
		splits.append(parse_split(xml_split))

	return Transaction(safety_text(xml_transaction.find('trn:id', ns)),
			safety_text(xml_transaction.find('trn:currency/cmdty:id', ns)),
			safety_text(xml_transaction.find('trn:date-posted/ts:date', ns)),
			safety_text(xml_transaction.find('trn:date-entered/ts:date', ns)),
			safety_text(xml_transaction.find('trn:description', ns)),
			xml_transaction.findall('trn:slots/slot', ns),
			splits)

# Given a string representing the fractional quanity and the currency, return a
# nicely formatted string
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
def translate_to_ledger(transaction, accounts):
	length = 40

	# Find an appropriate length based on the length of the longest split
	for split in transaction.splits:
		name = get_fullname(lookup_account(split.account, accounts), accounts)
		if len(name) > length:
			length = int(math.ceil(len(name) / 10.0)) * 10

	print(transaction.date.strftime("%Y/%m/%d") + " * " + transaction.description)
	for split in transaction.splits:
		name = get_fullname(lookup_account(split.account, accounts), accounts)
		quantity = translate_quantity(split.quantity, transaction.currency)

		print('{0:<{width}} {1:>10}'.format(name, quantity, width=length))
	print()
