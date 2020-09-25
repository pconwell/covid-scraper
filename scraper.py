import requests
from bs4 import BeautifulSoup
import datetime

month = datetime.datetime.now().strftime("%B")
day = datetime.datetime.now().strftime("%d")

# this will need to be fixed to address rolling over a new month
today = f"https://www.asafenashville.org/updates/mphd-daily-covid-19-update-for-{month.lower()}-{day}/"
yesterday = f"https://www.asafenashville.org/updates/mphd-daily-covid-19-update-for-{month.lower()}-{int(day)-1}/"



page = requests.get(yesterday)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.table
table_rows = table.find_all('tr')

for tr in table_rows:
   td = tr.find_all('td')
   row = [i.text for i in td]
   if row[0] in ["Total", "Inactive/Recovered", "Deaths", "Total active cases"]:
      print(row)