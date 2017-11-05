from Utils import *

class Account:
	def __init__(self, name, guid, account_type, commodity, commodity_scu, description, slots, parent):
		self.name = name
		self.guid = guid
		self.account_type = account_type
		self.commodity = commodity
		self.commodity_scu = commodity_scu
		self.description = description
		self.slots = slots
		self.parent = parent

	def display(self):
		print("Account:", self.guid)
		print("-->name:", self.name)
		print("-->account_type:", self.account_type)
		print("-->commodity:", self.commodity)
		print("-->commodity-scu:", self.commodity_scu)
		print("-->description:", self.description)
		print("-->slots:", self.slots)
		print("-->parent:", self.parent)

# TODO: Fix parsing for slots, commodity
def parse_account(xml_account):
	return Account(safety_text(xml_account.find('act:name', ns)),
			safety_text(xml_account.find('act:id', ns)),
			safety_text(xml_account.find('act:type', ns)),
			safety_text(xml_account.find('act:commodity', ns)),
			safety_text(xml_account.find('act:commodity-scu', ns)),
			safety_text(xml_account.find('act:description', ns)),
			safety_text(xml_account.find('act:slots', ns)),
			safety_text(xml_account.find('act:parent', ns)))
