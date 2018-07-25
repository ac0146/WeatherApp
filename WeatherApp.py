import requests
from bs4 import BeautifulSoup
import pandas as pd

#request information from the website (returns 200, which is good)
r = requests.get('https://whnt.com/weather/').text
#get actual content from website using our url (r) and html parser (lxml)
soup = BeautifulSoup(r, 'lxml')

days = [] #list for days
forecast = [] #list for weather
highlow = [] #list for high/low temperatures
chanceofrain = [] #list for chance of rain
i = 0 #variable to increment to print out each days forecast

#pulls each day from webpage into our list
for day in soup.find_all("div", class_="date"):
    days.append(day.text)

#pulls each day's forecast into out list
for weather in soup.find_all("strong", class_="day-description"):
    forecast.append(weather.text)

#pulls each day's high/low temps into our list (strips extra \t and \n)
for highnlow in soup.find_all("div", class_="day-hi-low"):
    highlow.append(highnlow.text.strip('\t\n'))

#pulls each day's chance of rain into our list (strips extra \n and \t and also
#just reads where the precipitation chance is as opposed to wind as well
for precip in soup.find_all("div", class_="day-details"):
    chanceofrain.append(precip.text[8:11].strip('\n\t'))

#LONG line, ***NEEDS FIXING WITH A LOOP OR SOMETHING***
data = {'Weather:':[forecast[0], forecast[1], forecast[2], forecast[3], forecast[4], forecast[5], forecast[6]], 'LO/HI:':[highlow[0], highlow[1], highlow[2], highlow[3], highlow[4], highlow[5], highlow[6]], 'Chance of Rain:':[chanceofrain[0], chanceofrain[1], chanceofrain[2], chanceofrain[3], chanceofrain[4], chanceofrain[5], chanceofrain[6]]}

df = pd.DataFrame(data, columns = ['Weather:', 'LO/HI:', 'Chance of Rain:'], index = days)
print(df)

exit = input()
