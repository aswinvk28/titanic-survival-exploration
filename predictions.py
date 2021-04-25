import os
import sys
import csv
    

def import_csv(file_path):
    file = open(file_path, 'r')
    csvreader = csv.reader(file, delimiter=',')
    prediction_data = PredictionData()
    for line in csvreader:
        prediction_data.append(line)
    
    return prediction_data

def predictions_0(data):
    """ Model with no features. Always predicts a passenger did not survive. """

    predictions = []
    for _, passenger in data.iterrows():
        
        # Predict the survival of 'passenger'
        predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
data = import_csv('titanic_data.csv')
predictions = predictions_0(data)

def predictions_1(data):
    """ Model with one feature: 
            - Predict a passenger survived if they are female. """
    
    predictions = []
    for _, passenger in data.iterrows():
        
        # Remove the 'pass' statement below 
        # and write your prediction conditions here
        pass
    
    # Return our predictions
    return pd.Series(predictions)

# Make the predictions
predictions = predictions_1(data)