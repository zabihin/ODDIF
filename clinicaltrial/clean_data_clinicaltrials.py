import pandas as pd
import ast


df = pd.read_csv('clinical_data.csv', sep=';')
print(len(df))
## filter data to enrollment>3 and status:completed, terminated 
filtered_df = df[(df['Enrollment'] > 3) & (df['Status'].isin(['COMPLETED', 'TERMINATED']))]
print(len(filtered_df))


conditions_column = filtered_df['Conditions'].apply(ast.literal_eval)  
exploded_series = conditions_column.explode()
all_diseas = exploded_series.tolist()
print(len(all_diseas))
unique_conditions = set(all_diseas)
print(len(unique_conditions))