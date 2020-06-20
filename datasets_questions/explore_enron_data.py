#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r+"))

total =  len(enron_data)

poi_total = sum( x["poi"] == True for x in enron_data.values() )

#print enron_data["PRENTICE JAMES"]["total_stock_value"]

#print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

#print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

NaN_total_payments = sum( p["total_payments"] == 'NaN' for p in enron_data.values())

print total, NaN_total_payments, 1.00 * NaN_total_payments/total

POI_NaN_total_payments = sum( p["poi"] == True and p["total_payments"] == 'NaN' for p in enron_data.values())

print poi_total, POI_NaN_total_payments, 1.00 * POI_NaN_total_payments/poi_total