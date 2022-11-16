import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#https://ebible.org/asv/JHN08



random_chapter= random.randint(1,21)

if random_chapter<10:
    random_chapter='0' +str(random_chapter)
else:
    random_chapter=str(random_chapter)

webpage = 'https://ebible.org/asv/JHN'+ random_chapter+'.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

req=Request(webpage, headers=headers)

webpage=urlopen(req).read()
soup=BeautifulSoup(webpage, 'html.parser')

verse=soup.findAll("div",class_="main")
#print(verse)

for v in verse:
    verse_list=v.text.split('.')

#print(verse_list)

myverse= random.choice(verse_list[:len(verse_list)-5])
#print(f"Chapter: {random_chapter}, Verse: {myverse}")

message= "Chapter: "+random_chapter+" Verse:" + myverse
print(message)

import keys2
from twilio.rest import Client

client= Client(keys2.accountSID,keys2.authToken)

TwilioNumber='+14143481198'

mycellnumber='9257847406'

textmessage=client.messages.create(to=mycellnumber, from_=TwilioNumber, body= message)

print(textmessage.status)


