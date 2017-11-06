from Utils import *
from Split import *

class Transaction:
	def __init__(self, guid, currency, date_posted, date_entered, description, slots, splits):
		self.guid = guid
		self.currency = currency
		self.date_posted = date_posted
		self.date_entered = date_entered
		self.description = description
		self.slots = slots
		self.splits = splits

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
			safety_text(xml_transaction.find('trn:slots', ns)),
			splits)
