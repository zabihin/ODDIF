import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://go.drugbank.com/drugs/DB00112'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.select_one('.datatable-remote')
    if table:
        df_list = pd.read_html(str(table))
        
        if df_list:
            df = df_list[0]
            
            df.to_csv('output.csv', index=False)
            print("DataFrame saved to 'output.csv'")
        else:
            print("No tables found in the HTML.")
    else:
        print("Table not found")
else:
    print("Failed to retrieve the webpage")