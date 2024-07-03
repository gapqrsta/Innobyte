import pandas as pd
import numpy as np

# Load the dataset
file_path = 'path_to_your_file/Amazon Sale Report.csv'
data = pd.read_csv(file_path)

# Function to parse dates
def parse_dates(date):
    for fmt in ('%m-%d-%y', '%m-%d-%Y'):
        try:
            return pd.to_datetime(date, format=fmt)
        except ValueError:
            continue
    return np.nan

# Apply the function to the 'Date' column
data['Date'] = data['Date'].apply(parse_dates)

# Check for missing values after conversion
missing_values = data.isnull().sum()

# Display missing values
print(missing_values)
