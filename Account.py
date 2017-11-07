from Utils import *

class Account:
	def __init__(self, name, guid, commodity, description, parent):
		self.name = name
		self.guid = guid
		self.commodity = commodity
		self.description = description
		self.parent = parent
		self.fullname = None

	def display(self):
		tree_print("Account", self, 0)

# Create an Account object from an XML account tag
def parse_account(xml_account):
	return Account(safety_text(xml_account.find('act:name', ns)),
			safety_text(xml_account.find('act:id', ns)),
			safety_text(xml_account.find('act:commodity/cmdty:id', ns)),
			safety_text(xml_account.find('act:description', ns)),
			safety_text(xml_account.find('act:parent', ns)))

# Given the guid and a list of accounts return the account that matches the guid or None if no account is found
def lookup_account(guid, accounts):
	for account in accounts:
		if account.guid == guid:
			return account
	return None

# Recursively build a full name for the account using the name of its parent
def get_fullname(account, accounts):
	if account.parent is None:
		return account.name
	else:
		parent_account = lookup_account(account.parent, accounts)
		# Check to see if parent already has a fullname and simply append to that
		if parent_account.fullname is None:
			return (get_fullname(parent_account, accounts) + ":" + account.name)
		else:
			return (parent_account.fullname + ":" + account.name)
