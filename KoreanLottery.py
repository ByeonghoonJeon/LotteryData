import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


# Load the dataset from the CSV file
df = pd.read_csv('lottoRes.csv')

# Remove any leading or trailing whitespace from the column names
df.columns = df.columns.str.strip()

# Select the last 20 rows of the DataFrame
last_20_rows = df.tail(50)

# Define the columns that contain the lottery numbers
number_columns = ['no1', 'no2', 'no3', 'no4', 'no5', 'no6', 'bonus']

# Create a dictionary to store the counts for each number from 1 to 45
number_counts = {i: 0 for i in range(1, 46)}


#[When trying to get numbers from the recent 20 rows
for number in range(1, 46):
    number_counts[number] = (last_20_rows[number_columns] == number).sum().sum()

# # [When trying to get all numbers from history] Loop through each number to count its occurrences in the specified columns
# for number in range(1, 46):
#     number_counts[number] = (df[number_columns] == number).sum().sum()

# Convert the dictionary of counts into a pandas DataFrame for easier handling
counts_df = pd.DataFrame(list(number_counts.items()), columns=['Number', 'Count'])
counts_df.to_csv('number_counts.csv', index=False)

# # Sort the DataFrame by 'Count' in descending order
# counts_df = counts_df.sort_values(by='Count', ascending=False)

# Print the resulting DataFrame to the console
print("Counts of each number from 1 to 45:")
print(counts_df)

# def get_lotto_numbers(draw_no):
#     api_url = f"https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={draw_no}"

#     try:
#         response = requests.get(api_url)
#         response.raise_for_status()

#         data = response.json()
#         print(f"{draw_no}회 결과추출")

#         return {
#             'drwNo' : data['drwNo'],
#             'date': data['drwNoDate'], 
#             'lottoNumb': [str(data[f"drwtNo{i}"]) for i in range(1, 7)], 
#             'bonusNumb': data['bnusNo']
#         }
        
        
#     except requests.exceptions.RequestException as e:
#         print(f"오류가 발생했습니다: {e}")
        
# def maxRound():
#     url = "https://www.dhlottery.co.kr/common.do?method=main"
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html.parser')
#     max_numb = soup.find(name="strong", attrs={"id": "lottoDrwNo"}).text
#     return int(max_numb)

       
# # 최신 회차 가져오기
# maxCount = maxRound()

# draw_no  = 1

# # CSV 파일 쓰기
# with open('lottoRes.csv', 'w', newline='') as csvfile:
#     # CSV 파일 쓰기
#     writer = csv.writer(csvfile, delimiter=',')
    
#     # 1화부터 최신화까지 크롤링
#     for draw_no in range(1, maxCount+1):
#         res = get_lotto_numbers(draw_no)
#         # 순서 : 회차, 날짜, 로또번호1, 로또번호2, 로또번호3, 로또번호4, 로또번호5, 로또번호6, 보너스번호
#         writer.writerow([res.get('drwNo'), res.get('date')] + res.get('lottoNumb') + [res.get('bonusNumb')])