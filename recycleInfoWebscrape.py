from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

# Recycling website
html = urlopen('https://www.recyclingtown.com/recycled-materials/')

# create the BeautifulSoup object
soup = BeautifulSoup(html.read(), "lxml")

data = soup.find('article',{"id":"post-21"})
print(data)
recycleList = []

#scrapes data by going to right indicators in html
for ul in data.findChildren('ul'):
    for li in ul.find_all('li'):
        recycleList.append(li.text)

#writes scraped data to a csv file
with open('recycle.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(recycleList)

# # save it to a file that we can edit
# fout = open('RECYCLEABLE.txt', 'wt', encoding='utf-8')
# fout.write(str(soup))
# fout.close()
