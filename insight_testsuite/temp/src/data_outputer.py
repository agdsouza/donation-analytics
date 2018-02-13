class DataOutputer:
	''' Takes calculated outputs and formats it into a text file '''

	def __init__(self, result_list, output_name):
		self.result_list = result_list
		self.output_name = output_name

	def format_line(self, record):
		''' Takes one record, delimits it with the | character, and returns that record as a string '''
		s = ''
		s += record["CMTE_ID"] + "|" + record["ZIP_CODE"] + "|"
		s += record["TRANSACTION_DT"] + "|" + record["PERCENTILE"] + "|"
		s += record["TOTAL_AMT"] + "|" + record["REPEATS"]
		return s

	def write_to_txt(self):
		# write each record to a given text file
		output = open(self.output_name, "w")
		for record in self.result_list:
			output.write(self.format_line(record))
			output.write('\n')
		output.close()
