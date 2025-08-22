import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# Load the dataset from the CSV file
df = pd.read_csv('powerballHistory.csv')

# Remove any leading or trailing whitespace from the column names
df.columns = df.columns.str.strip()

# Select the last 20 rows of the DataFrame
last_20_rows = df.tail(100)

# Define the columns that contain the lottery numbers
number_columns = ['bonus']

# Create a dictionary to store the counts for each number from 1 to 45
number_counts = {i: 0 for i in range(1, 26)}


# #[When trying to get numbers from the recent 20 rows
# for number in range(1, 27):
#     number_counts[number] = (last_20_rows[number_columns] == number).sum().sum()

# [When trying to get all numbers from history] Loop through each number to count its occurrences in the specified columns
for number in range(1, 27):
    number_counts[number] = (df[number_columns] == number).sum().sum()

# # Convert the dictionary of counts into a pandas DataFrame for easier handling
counts_df = pd.DataFrame(list(number_counts.items()), columns=['Number', 'Count'])
counts_df.to_csv('[PB_bonus]number_count.csv', index=False)

# # Sort the DataFrame by 'Count' in descending order
counts_df = counts_df.sort_values(by='Count', ascending=False)

# Print the resulting DataFrame to the console
print(counts_df)





# # URL of the JSON data
# url = "https://data.ny.gov/api/views/d6yy-54nr/rows.json?accessType=DOWNLOAD"

# try:
#     # Send a GET request to the URL
#     response = requests.get(url)
#     response.raise_for_status()  # Raise an exception for bad status codes

#     # Parse the JSON response
#     data = response.json()

#     # The 'Winning Numbers' are at index 9 in each data row.
#     # We can find this index programmatically by looking at the metadata
#     winning_numbers_index = -1
#     for i, col in enumerate(data['meta']['view']['columns']):
#         if col.get('id') == 538589854 or col.get('fieldName') == 'winning_numbers':
#             # The actual data starts after the system columns (sid, id, etc.)
#             # Let's find the correct index in the 'data' array by looking for a column with the right name
#             if col['name'] == 'Winning Numbers':
#                  # Based on the API data structure, this column is the 10th element (index 9) in each row's list
#                 winning_numbers_index = 9 
#                 break

#     if winning_numbers_index != -1:
#         # Extract only the winning numbers
#         winning_numbers = [row[winning_numbers_index] for row in data['data']]

#         # Write the data to a CSV file
#         output_csv_file = 'powerballHistory.csv'
#         with open(output_csv_file, 'w', newline='') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(['Winning Numbers'])  # Write the header
#             for numbers in winning_numbers:
#                 writer.writerow([numbers])

#         print(f"Winning numbers have been successfully written to {output_csv_file}")
#     else:
#         print("Could not find the 'Winning Numbers' column.")

# except requests.exceptions.RequestException as e:
#     print(f"An error occurred during the request: {e}")
# except (KeyError, IndexError) as e:
#     print(f"An error occurred while parsing the data: {e}. The data structure might have changed.")