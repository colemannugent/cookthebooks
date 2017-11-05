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

