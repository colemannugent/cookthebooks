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

# Check to see if an element has a text attribute. If the element does have a
# text attribute, return it, else return none
def safety_text(element):
	if hasattr(element, 'text'):
		return element.text
	else:
		return None
