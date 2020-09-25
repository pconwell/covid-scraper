import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import re

today = datetime.today()

today_url = f"https://www.asafenashville.org/updates/mphd-daily-covid-19-update-for-{today.strftime('%B').lower()}-{today.strftime('%d')}/"
yesterday_url = f"https://www.asafenashville.org/updates/mphd-daily-covid-19-update-for-{(today - timedelta(1)).strftime('%B').lower()}-{(today - timedelta(1)).strftime('%d')}/"

today_page = requests.get(today_url)
yesterday_page =requests.get(yesterday_url)

data = []
for page in [today_page, yesterday_page]:
   soup = BeautifulSoup(page.content, 'html.parser')
   table = soup.table
   table_rows = table.find_all('tr')

   for tr in table_rows:
      td = tr.find_all('td')
      row = [i.text for i in td]
      if row[0] in ["Total", "Inactive/Recovered", "Deaths", "Total active cases"]:
         # print(row)
         data.append(int(row[1].replace(',', '')))
   # print("\n")

total_delta = (data[0] - data[4])
inactive_delta = (data[1] - data[5])
deaths_delta = (data[2] - data[6])
active_delta = (data[3] - data[7])

print(f"Cases: {data[0]:,} ({total_delta:+d})\nDeaths: {data[1]:,} ({deaths_delta:+d})\nRecovered/Inactive: {data[2]:,} ({inactive_delta:+d})\nActive: {data[3]:,} ({active_delta:+d})")

##############################################################################################
##############################################################################################
##############################################################################################

key_metric_url = "https://www.asafenashville.org/reopening-key-metrics"
metric_page = requests.get(key_metric_url)
soup = BeautifulSoup(metric_page.content, 'html.parser')

test = soup(text=re.compile('Current: '))

metrics = []
for i in test:
   metrics.append(i.split(":")[1].split(" ")[1])

print(f"Transmission Rate: {metrics[0]}\nHospital Floor Bed Capacity: {metrics[4]} (Goal: 20%)\nHospital ICU Bed Capacity: {metrics[5]} (Goal: 20%)\nNew Cases per 100K Residents: {metrics[6]} (Goal: <10)\n7-Day Positive Test Rate: {metrics[7]} (Goal: <10)")