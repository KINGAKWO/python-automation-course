# Step 3.1: Fetch HTML Content
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import os

html_content = requests.get("http://127.0.0.1:5500/Activity_webscraping%20and%20dataprocessing/Files/home/coder/project/learn/baseball_stats.html").text
soup = BeautifulSoup(html_content, 'html.parser')

print(soup.prettify().encode('utf-8').decode('utf-8'))

# Step 3.2: Extract the Required Data
# Extract all rows from the table
table = soup.find('table')
head = soup.find('th')
rows = table.find_all('tr')
data = []
for row in rows:
    cols = row.find_all(['th', 'td'])
    data.append([col.get_text(strip=True) for col in cols])

# Write data to CSV file
with open('sports_statistics.csv ', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    

# Step 4.1: Convert to a DataFrame
# Convert the game data into a pandas DataFrame
df = pd.read_csv('sports_statistics.csv ')

# Inspect the DataFrame
### YOUR CODE HERE ###
print(df.head())

# Save and print the shaped data
### YOUR CODE HERE ###
print(df.shape)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###
df.to_csv('sports_statistics.csv', index=False)
