
import pandas as pd
import datetime as dt
import json

# Read the data, ensuring python file and the .csv file are in the same directory

data = pd.read_csv("dataset.csv")

data.head()

date_sample = dt.datetime.strptime("2020-03-23","%Y-%m-%d").date()

def obsolete_flaging(expiring_date):

	""" obsolete_flaging function returns TRUE or FLASE To differentiate between 
	expired and non-expired items using the date column. All items with a date before 2021-01-01 are expired
	"""

	# Coverting expiration date of an item to date_sample

	date_of_item = dt.datetime.strptime(expiring_date,"%Y-%m-%d").date()

	# Calculating different between date_sample and date_of_item

	different_in_dates = date_of_item - date_sample
	different_in_days = different_in_dates.days


	# Returns 'TRUE' of 'FALSE' depending on the value of different_in_days

	if different_in_days > 0:
		return 'FALSE'
	else:
		return 'TRUE'

# Adds a new column named [obsolete]. The column should flag TRUE, indicating an item is 
# expired and FALSE, otherwise

data['obsolete'] = data['date'].map(obsolete_flaging)

# Transform the output data to a JSON format

data_with_obsolete_column = data.to_json()

# Store the data in your local directory

with open('data_with_obsolete_column.json', 'w') as json_file:
	json.dump(data, json_file)