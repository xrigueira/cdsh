import pandas as pd

# Load data
df = pd.read_csv("data/data_cdsh.csv")

# Define which columns belong to each category
gender_cols = ['Female', 'Male']
age_cols = ['17_and_Under', '18-64', '65_and_Over']
ethnicity_cols = ['Black', 'White', 'Hispanic', 'Asian', 'Native_American', 'Other_Missing']

# Melt gender
gender_df = df.melt(id_vars=['Year', 'Program', 'Level', 'County'], 
                    value_vars=gender_cols, 
                    var_name='Group', 
                    value_name='Value')
gender_df['Category'] = 'Gender'

# Melt age
age_df = df.melt(id_vars=['Year', 'Program', 'Level', 'County'], 
                    value_vars=age_cols, 
                    var_name='Group', 
                    value_name='Value')
age_df['Category'] = 'Age'

# Melt ethnicity
ethnicity_df = df.melt(id_vars=['Year', 'Program', 'Level', 'County'], 
                        value_vars=ethnicity_cols, 
                        var_name='Group', 
                        value_name='Value')
ethnicity_df['Category'] = 'Ethnicity'

# Combine all melted dataframes
reshaped_df = pd.concat([gender_df, age_df, ethnicity_df], ignore_index=True)

# Save the reshaped dataframe to a new CSV file
reshaped_df.to_csv("data/reshaped_data_cdsh.csv", index=False)