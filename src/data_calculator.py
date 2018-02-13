from math import ceil

class DataCalculator:
	''' Takes in cleaned data of repeat donors and prepares data for output '''
	repeats = set()
	data_dict = []
	result_dict = []

	def __init__(self, data_gen, percent_file):
		''' Initializes data generator for the class '''
		self.data_gen = data_gen
		with open(percent_file, 'r') as f:
			self.percentile = int(f.readline())

	def get_transac_list(self, donation_list):
		return [round(int(rec["TRANSACTION_AMT"])) for rec in donation_list]

	def find_transac_sum(self, donation_list):
		''' Finds the sum of transactions for repeat donors in the same area for the same candidate '''
		transactions = [round(rec) for rec in self.get_transac_list(donation_list)]
		return int(sum(transactions))

	def find_num_repeats(self, donation_list):
		''' Finds number of repeated donors to a candidate in a specific zip code '''
		return len(donation_list)

	def find_percentile(self, donation_list):
		''' Computes percentile using the nearest rank method '''
		transactions = sorted(self.get_transac_list(donation_list))
		N = len(transactions)
		ind = int(ceil((self.percentile/100) * N))
		return ind - 1


	def process_data(self):
		''' Goes through all repeated transactions, performing percentile, summing, and repeat
			counts for all repeated elements, and returns all results in a list of dictionaries
		'''
		for d in self.data_gen:
			self.data_dict.append(d)
			if (d["NAME"], d["ZIP_CODE"]) not in self.repeats:
				self.repeats.add((d["NAME"], d["ZIP_CODE"]))

			else: #
				# check for any contributions made by this donor for recipient C, zip of z for this year y
				relevant_donors = [rec for rec in self.data_dict if rec["CMTE_ID"] == d["CMTE_ID"] and rec["ZIP_CODE"] == d["ZIP_CODE"] and rec["TRANSACTION_DT"] == d["TRANSACTION_DT"]]

				stat_labels = ["CMTE_ID", "ZIP_CODE", "TRANSACTION_DT", "PERCENTILE", "TOTAL_AMT", "REPEATS"]
				donation_stats = {k: None for k in stat_labels}

				transac_list = self.get_transac_list(relevant_donors)
				transaction_sum = self.find_transac_sum(relevant_donors)
				percentile_ind = self.find_percentile(relevant_donors)
				num_repeats = self.find_num_repeats(relevant_donors)

				donation_stats["CMTE_ID"] = d["CMTE_ID"]
				donation_stats["ZIP_CODE"] = d["ZIP_CODE"]
				donation_stats["TRANSACTION_DT"] = d["TRANSACTION_DT"]
				donation_stats["PERCENTILE"] = str(sorted(self.get_transac_list(relevant_donors))[percentile_ind])
				donation_stats["TOTAL_AMT"] = str(transaction_sum)
				donation_stats["REPEATS"] = str(num_repeats)

				self.result_dict.append(donation_stats)

		return self.result_dict


