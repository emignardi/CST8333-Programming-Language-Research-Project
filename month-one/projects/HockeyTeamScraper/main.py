from bs4 import BeautifulSoup
import requests
import pandas as pd

# BeautifulSoup Setup
url = "https://www.scrapethissite.com/pages/forms/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# DataFrame Columns
table_header_titles = soup.find_all("th")
columns = [column.text.strip() for column in table_header_titles]

# DataFrame Setup
df = pd.DataFrame(columns=columns)

# DataFrame Data
table_row_data = soup.find_all("tr", class_="team")
for row in table_row_data:
    row_data = row.find_all("td")
    data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = data

# print(columns)
# print(data)

# Export DataFrame (CSV & XLSX)
df.to_csv("C:\\Users\\migna\\OneDrive\\Desktop\\LearnPython\\month-one\\projects\\HockeyTeamScraper\\hockey-teams.csv", index=False)
df.to_excel("C:\\Users\\migna\\OneDrive\\Desktop\\LearnPython\\month-one\\projects\\HockeyTeamScraper\\hockey-teams.xlsx", index=False)