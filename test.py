import pandas as pd

# Assume df is your DataFrame
df = pd.read_csv('user_data.csv')

# Accessing the 'Username' column of the first row
username = df.iloc[0]['Password']
print(username)
