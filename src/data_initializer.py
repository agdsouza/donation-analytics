class DataInitializer:
	''' initializes and cleans data from donation analytics stream '''
	non_repeats = set()

	def __init__(self, filename):
		self.filename = filename

	def get_data(self):
		''' Yields generator of each line of data in filename, split by a pipe '''
		with open(self.filename, 'r') as file:
			for line in file:
				yield line.split('|')

	def filter_data(self, data_gen):
		''' Filters data and returns generator of dictionaries ignoring data that:
			- contains OTHER_ID (index 15)
			- has invalid TRANSACTION_DT, ZIP_CODE, or NAME (indexes 13, 10, 7)
			- has empty CMTE_ID or TRANSACTION_AMT cells (indexes 0, 14)
		'''
		for d in data_gen:
			if len(d[15]) == 0 and len(d[13]) == 8 and len(d[10]) == 9 and \
			len(d[7]) != 0 and len(d[0]) != 0 and len(d[14]) != 0:
				yield {"CMTE_ID": d[0], "NAME": d[7], "ZIP_CODE": d[10][:5], \
				"TRANSACTION_DT": d[13][-4:], "TRANSACTION_AMT": d[14]}

	def set_nonrepeat_donors(self, filter_gen):
		''' Finds non-repeat donors and returns their name-zipcode combination as a set'''
		for d in filter_gen:
			if (d["NAME"], d["ZIP_CODE"]) not in self.non_repeats:
				self.non_repeats.add((d["NAME"], d["ZIP_CODE"]))
			else:
				self.non_repeats.remove((d["NAME"], d["ZIP_CODE"]))

	def get_repeat_donors(self, filter_gen):
		''' Yields generator containing only the repeat donators '''
		for d in filter_gen:
			if (d["NAME"], d["ZIP_CODE"]) not in self.non_repeats:
				yield d





