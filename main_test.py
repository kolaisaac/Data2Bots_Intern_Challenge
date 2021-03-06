
import unittest
from challenge import check_expiration
from challenge import data_to_json

class DataJson(object):
	"""docstring for DataJson"""
	def data_with_obsolete_cloumn_json(self):

		#Confirm that the ptogram only takes csv files
		file = 'data_updated.json'
		expired = check_expiration(file)
		self.assertFalse(expired == True)

	def data_with_obsolete_cloumn_csv(self):

		file = 'dataset.csv'
		expired = check_expiration(file)
		self.assertTrue(expired == True)

if __name__ == '__main__':
	unittest.main()