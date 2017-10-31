from checkEachInputStructure import *

class Donation:

	comparison_mode = 1

	def __init__(self, cmte_id, zip_code, transaction_dt, transaction_amt, other_id):
		self.cmte_id = cmte_id
		self.zip_code = zip_code
		self.transaction_dt = transaction_dt
		self.transaction_amt = int(transaction_amt)
		self.other_id = other_id

		self.number_of_zip_donations = 1
		self.number_of_date_donations = 1
		self.zip_median = self.transaction_amt
		self.date_median = self.transaction_amt
		self.zip_amount = self.transaction_amt
		self.date_amount = self.transaction_amt

	def increase_number(self):
		if Donation.comparison_mode == 1:
			self.number_of_zip_donations += 1
		elif Donation.comparison_mode == 2:
			self.number_of_date_donations += 1

	def update_median(self):
		if Donation.comparison_mode == 1:
			self.zip_median = DesideRounding(self.zip_amount / self.number_of_zip_donations)
		elif Donation.comparison_mode == 2:
			self.date_median = DesideRounding(self.date_amount / self.number_of_date_donations)

	def has_other_id(self):
		return checkDataLimitationForOtherID(self.other_id)

	def has_valid_date(self):
		return checkTransactionDateStructure(self.transaction_dt)

	def has_valid_zip(self):
		return checkZipcodeStructure(self.zip_code)

	def is_valid_to_check(self):
		return checkCMTEID_and_TransactionAmount_structure(self.cmte_id, self.transaction_amt)

	def _split_date(self):
		day = int(self.transaction_dt[:2])
		month = int(self.transaction_dt[2:4])
		year = int(self.transaction_dt[4:])

		return (year, month, day)


	def __eq__(self, other):
		if Donation.comparison_mode == 1:
			return self.cmte_id == other.cmte_id and self.zip_code == other.zip_code
		elif Donation.comparison_mode == 2:
			return self.cmte_id == other.cmte_id and self.transaction_dt == other.transaction_dt

	def __lt__(self, other):
		if self.cmte_id != other.cmte_id:
			return self.cmte_id < other.cmte_id
		else:
			return self._split_date() < other._split_date()

	
	def __repr__(self):
		return str(self)