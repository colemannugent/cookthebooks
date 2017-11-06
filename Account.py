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
		self.children = []
		self.fullname = ""

	def display(self):
		tree_print("Account", self, 0)

# TODO: Fix parsing for slots, commodity
def parse_account(xml_account):
	return Account(safety_text(xml_account.find('act:name', ns)),
			safety_text(xml_account.find('act:id', ns)),
			safety_text(xml_account.find('act:type', ns)),
			safety_text(xml_account.find('act:commodity/cmdty:id', ns)),
			safety_text(xml_account.find('act:commodity-scu', ns)),
			safety_text(xml_account.find('act:description', ns)),
			xml_account.findall('act:slots/slot', ns),
			safety_text(xml_account.find('act:parent', ns)))

def lookup_account(guid, accounts):
	for account in accounts:
		if account.guid == guid:
			return account
	return None

def get_fullname(account, accounts):
	if account.parent is None:
		return account.name
	else:
		return (get_fullname(lookup_account(account.parent, accounts), accounts) + ":" + account.name)
