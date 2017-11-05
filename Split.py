from Utils import *

class Split:
	def __init__(self, guid, memo, reconciledstate, reconciledate, value, quantity, account, slots):
		self.guid = guid
		self.memo = memo
		self.reconciledstate = reconciledstate
		self.reconciledate = reconciledate
		self.value = value
		self.quantity = quantity
		self.account = account
		self.slots = slots

	def display(self):
		print("split:", self.guid)
		print("-->memo:", self.memo)
		print("-->reconciled-state:", self.reconciledstate)
		print("-->reconcile-date:", self.reconciledate)
		print("-->value:", self.value)
		print("-->quantity:", self.quantity)
		print("-->account:", self.account)
		print("-->slots:", self.slots)

def parse_split(xml_split):
		return Split(safety_text(xml_split.find('split:id', ns)),
				safety_text(xml_split.find('split:memo', ns)),
				safety_text(xml_split.find('split:reconciled-state', ns)),
				safety_text(xml_split.find('split:reconcile-date', ns)),
				safety_text(xml_split.find('split:value', ns)),
				safety_text(xml_split.find('split:quantity', ns)),
				safety_text(xml_split.find('split:account', ns)),
				safety_text(xml_split.find('split:slot', ns)))
