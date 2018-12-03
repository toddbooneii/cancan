import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

############### GENERAL RECYCLING INFO ###############
html = urlopen('https://www.recyclingtown.com/recycled-materials/')

# create the BeautifulSoup object
soup = BeautifulSoup(html.read(), 'lxml')
data = soup.find('article',{'id':'post-21'})

#scrapes data by finding right tags in html
#contains recyling types & general descriptions
recycleList = []
for ul in data.findChildren('ul'):
    for li in ul.find_all('li'):
        recycleList.append(li.text)

generalrecyclyList = []
headerList = []

#creates a header list & their associated general info values as a list
for x in recycleList:
    headerList.append(x.split('\n')[0])
    generalrecyclyList.append(x.split('\n')[1])

############### ALUMINUM INFO ###############
htmlAluminum = urlopen('https://www.recyclingtown.com/aluminum-recycling/')
soupAluminum = BeautifulSoup(htmlAluminum.read(), 'lxml')
dataAluminum = soupAluminum.find('article',{'id':'post-7'})

aluminumList = []
for p in dataAluminum.findChildren('p'):
    aluminumList.append(p.text)
aluminumInfo = " ".join(aluminumList)

############### BATTERY INFO ###############
htmlBattery = urlopen('https://www.recyclingtown.com/battery-recycling/')
soupBattery = BeautifulSoup(htmlBattery.read(), 'lxml')
dataBattery = soupBattery.find('article',{'id':'post-8'})

batteryList = []
for p in dataBattery.findChildren('p'):
    batteryList.append(p.text)
batteryInfo = " ".join(batteryList)

############### COMPUTER INFO ###############
htmlComputer = urlopen('https://www.recyclingtown.com/computer-recycling/')
soupComputer = BeautifulSoup(htmlComputer.read(), 'lxml')
dataComputer = soupComputer.find('article',{'id':'post-10'})

computerList = []
for p in dataComputer.findChildren('p'):
    computerList.append(p.text)
computerInfo = " ".join(computerList)

############### E-CYCLING INFO ###############
htmlEcycle = urlopen('https://www.recyclingtown.com/e-cycling/')
soupEcycle = BeautifulSoup(htmlEcycle.read(), 'lxml')
dataEcycle = soupEcycle.find('article',{'id':'post-13'})

ecycleList = []
for p in dataEcycle.findChildren('p'):
    ecycleList.append(p.text)
ecycleInfo = " ".join(ecycleList)

############### GLASS INFO ###############
htmlGlass = urlopen('https://www.recyclingtown.com/glass-recycling/')
soupGlass = BeautifulSoup(htmlGlass.read(), 'lxml')
dataGlass = soupGlass.find('article',{'id':'post-14'})

glassList = []
for p in dataGlass.findChildren('p'):
    glassList.append(p.text)
glassInfo = " ".join(glassList)

############### MOBILE PHONE INFO ###############
htmlPhone = urlopen('https://www.recyclingtown.com/mobile-phone-recycling/')
soupPhone = BeautifulSoup(htmlPhone.read(), 'lxml')
dataPhone = soupPhone.find('article',{'id':'post-16'})

phoneList = []
for p in dataPhone.findChildren('p'):
    phoneList.append(p.text)
phoneInfo = " ".join(phoneList)

############### PAPER PHONE INFO ###############
htmlPaper = urlopen('https://www.recyclingtown.com/paper-recycling/')
soupPaper = BeautifulSoup(htmlPaper.read(), 'lxml')
dataPaper = soupPaper.find('article',{'id':'post-17'})

paperList = []
for p in dataPaper.findChildren('p'):
    paperList.append(p.text)
paperInfo = " ".join(paperList)

############### PLASTIC PHONE INFO ###############
htmlPlastic = urlopen('https://www.recyclingtown.com/plastic-recycling/')
soupPlastic = BeautifulSoup(htmlPlastic.read(), 'lxml')
dataPlastic = soupPlastic.find('article',{'id':'post-18'})

plasticList = []
for p in dataPlastic.findChildren('p'):
    plasticList.append(p.text)
plasticInfo = " ".join(plasticList)

############### TIRE PHONE INFO ###############
htmlTire = urlopen('https://www.recyclingtown.com/tire-recycling/')
soupTire = BeautifulSoup(htmlTire.read(), 'lxml')
dataTire = soupTire.find('article',{'id':'post-29'})

tireList = []
for p in dataTire.findChildren('p'):
    tireList.append(p.text)
tireInfo = " ".join(tireList)

############### WASTE PHONE INFO ###############
htmlWaste = urlopen('https://www.recyclingtown.com/waste-recycling/')
soupWaste = BeautifulSoup(htmlWaste.read(), 'lxml')
dataWaste = soupWaste.find('article',{'id':'post-30'})

wasteList = []
for p in dataWaste.findChildren('p'):
    wasteList.append(p.text)
wasteInfo = " ".join(wasteList)

############### WATER PHONE INFO ###############
htmlWater = urlopen('https://www.recyclingtown.com/water-recycling/')
soupWater = BeautifulSoup(htmlWater.read(), 'lxml')
dataWater = soupWater.find('article',{'id':'post-31'})

waterList = []
for p in dataWater.findChildren('p'):
    waterList.append(p.text)
waterInfo = " ".join(waterList)

#####################################################################

#dumps all of the recycling additional information into 1 list
allList = []
allList.append(aluminumInfo)
allList.append(batteryInfo)
allList.append(computerInfo)
allList.append(ecycleInfo)
allList.append(glassInfo)
allList.append(phoneInfo)
allList.append(paperInfo)
allList.append(plasticInfo)
allList.append(tireInfo)
allList.append(wasteInfo)
allList.append(waterInfo)



def getRecycleInfoDF():
    #creates a dataframe of recycling name, general info, additional info
    dictionary = {'General Info':generalrecyclyList,'Recycling':headerList, 'Additional Info':allList}
    d1 = pd.DataFrame(dictionary)
    d1 = d1[['Recycling','General Info','Additional Info']]
    return d1
    # d1.to_csv('recycleInfo.csv')

getRecycleInfoDF()
