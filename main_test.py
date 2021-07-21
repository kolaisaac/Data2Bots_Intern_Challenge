from challenge import check_expiration


def test_obsolete_flaging_expired():

	""" Ensuring that obsolete_flaging function returns TRUE for All items with a date before 2021-01-01 are expired
	"""
	expired = obsolete_flaging('2020-12-22')
	assert expired == 'TRUE', "Should be TRUE"

def test_obsolete_flaging_not_expired():

	""" Ensuring that obsolete_flaging function returns FALSE for All items with a date after 2021-01-01 are not expired
	"""
	expired = obsolete_flaging('2021-06-12')
	assert expired == 'FALSE', "Should be FALSE"