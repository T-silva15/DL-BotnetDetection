import os
import pandas as pd

# Define the path to the folder containing the CSV files
folder_path = 'proj/datasets/sized_data/1000_lines'

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # Extract the label from the filename (assuming the label is the part before the first underscore)
        label = filename.split('_')[0]
        
        # Construct the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Add the label column
        df['label'] = label
        
        # Save the updated DataFrame back to the CSV file
        df.to_csv(file_path, index=False)


print("Labels added to all files in the sized_data folder.")