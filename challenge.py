
import pandas as pd
import json
import numpy as np

# Read the data, ensuring python file and the .csv file are in the same directory

data = pd.read_csv("dataset.csv")


def check_expiration(data):

	# declaration of variables
	item_date = data['date']

	# Adds a new column named [obsolete]. The column should flag TRUE, indicating an item is 
	# expired and FALSE, otherwise

	obsolete = np.where(data['date']<'2021-01-01', True, False)

	data['obsolete'] = obsolete

	data_with_obsolete_column = data

	return data_with_obsolete_column



# Transform the output data to a JSON format

def data_to_json(data):
    
    try:
        data_to_json = data.to_json()

        # Store the data in your local directory
        
        with open('data_updated.json', 'w') as json_file:
            json.dump(data_to_json, json_file)
            
        print("JSON file created successfully")
        
    except Exception:
        print("JSON file not created")

data_to_json(data)