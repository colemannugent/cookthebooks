from Utils import *

class Split:
	def __init__(self, memo, value, quantity, account, slots):
		self.memo = memo
		self.value = value
		self.quantity = quantity
		self.account = account
		self.slots = slots

	def display(self):
		tree_print("Split", self, 0)

# Fix parsing for slots
def parse_split(xml_split):
		return Split(safety_text(xml_split.find('split:memo', ns)),
				safety_text(xml_split.find('split:value', ns)),
				safety_text(xml_split.find('split:quantity', ns)),
				safety_text(xml_split.find('split:account', ns)),
				safety_text(xml_split.find('split:slot', ns)))
