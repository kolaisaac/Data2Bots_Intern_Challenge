from challenge import check_expiration
import pandas as pd

def test_obsolete_flaging_expired():

	""" Ensuring that obsolete_flaging function returns TRUE for All items with a date before 2021-01-01 are expired
	"""
	item_date = pd.to_datetime('2020-12-22')
	expired = check_expiration(item_date)
	assert expired == 'TRUE', "Should be TRUE"

def test_obsolete_flaging_not_expired():

	""" Ensuring that obsolete_flaging function returns FALSE for All items with a date after 2021-01-01 are not expired
	"""
	item_date = pd.to_datetime('2021-01-01')
	expired = check_expiration(item_date)
	assert expired == 'FALSE', "Should be FALSE"