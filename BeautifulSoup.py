from bs4 import BeautifulSoup
import requests
import re



URL = "https://news.yahoo.co.jp/"
res = requests.get(URL)


soup = BeautifulSoup(res.text, "html.parser")
  
topic = soup.find(class_="sc-jGFFOr Pplqh")

data_list = topic.find_all(href=re.compile("news.yahoo.co.jp/pickup"))

headline_link_list = [data.attrs["href"] for data in data_list]


for headline_link in headline_link_list:

  summary = requests.get(headline_link)

  summary_soup = BeautifulSoup(summary.text, "html.parser")

  summary_find = summary_soup.find('p', class_='sc-dTSiUb fCZKLk')
  print(summary_find.text)
  print("")

  summary_found = summary_soup.find('p', class_='sc-eQvJSV cMIDqS highLightSearchTarget')
  print(summary_found.text)
  print("") 

  print(headline_link)