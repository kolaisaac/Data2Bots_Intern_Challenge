
import pandas as pd
import json
import numpy as np

# Read the data, ensuring python file and the .csv file are in the same directory

data = pd.read_csv("dataset.csv")

# declaration of variables

item_date = data['date']

obsolete = np.where(data['date']<'2021-01-01', True, False)


# Adds a new column named [obsolete]. The column should flag TRUE, indicating an item is 
# expired and FALSE, otherwise

data['obsolete'] = obsolete

data_with_obsolete_column = data

# Transform the output data to a JSON format

data_with_obsolete_updated = data_with_obsolete_column.to_json()

# Store the data in your local directory

with open('data_with_obsolete_updated.json', 'w') as json_file:
	json.dump(data_with_obsolete_updated, json_file)