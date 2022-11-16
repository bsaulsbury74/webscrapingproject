
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

tablecells=soup.findAll("tr")



for row in tablecells[1:6]:
    tabledesc=row.findAll("td")
    Rank= tabledesc[0].text
    movname=tabledesc[1].text
    gross=int(tabledesc[7].text.replace('$','').replace(',',''))
    Dist=tabledesc[9].text
    theaters=int(tabledesc[6].text.replace(',',''))
    avgpertheatre= round(gross/theaters,2)
    print("Rank:",(Rank))
    print("Movie Name:",(movname))
    print("Total Gross:", (gross))
    print("Distibutor:", (Dist))
    print("Average Per Theatre:", (avgpertheatre))
    print()
    print()
