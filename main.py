import requests
from bs4 import BeautifulSoup

city = input("enter city name: ")

url= "https://www.google.com/search?q="+"weather"+city
content = requests.get(url).content

soup = BeautifulSoup(content, "html.parser")
print(f"{city} Weather's Information:")
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
loc = soup.find("span",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text

data = str.split("\n")
time= data[0]
sky= data[1]

print("Temperature is", temp)
print("Time: ", time)
print(f"Location :", loc)
print("Sky Description: ", sky)
