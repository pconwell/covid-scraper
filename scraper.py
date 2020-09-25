import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

today = datetime.today()

today_url = f"https://www.asafenashville.org/updates/mphd-daily-covid-19-update-for-{today.strftime('%B').lower()}-{today.strftime('%d')}/"
yesterday_url = f"https://www.asafenashville.org/updates/mphd-daily-covid-19-update-for-{(today - timedelta(1)).strftime('%B').lower()}-{(today - timedelta(1)).strftime('%d')}/"

today_page = requests.get(today_url)
yesterday_page =requests.get(yesterday_url)

for page in [today_page, yesterday_page]:
   soup = BeautifulSoup(page.content, 'html.parser')
   table = soup.table
   table_rows = table.find_all('tr')

   for tr in table_rows:
      td = tr.find_all('td')
      row = [i.text for i in td]
      if row[0] in ["Total", "Inactive/Recovered", "Deaths", "Total active cases"]:
         print(row)