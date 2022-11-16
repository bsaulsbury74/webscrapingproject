import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapter = random.randint(1,21)


webpage = 'https://biblehub.com/niv/john/'+ str(chapter) +".htm"

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

page_verses = soup.findAll("div", attrs={"class":"chap"})

for verse in page_verses:
    verse_list=verse.text.split(".")



my_verse = random.choice(verse_list[:len(verse_list)-5])



message = "Chapter:" + str(chapter) + " Verse: " + my_verse
print(message)

import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber = '+14143481198'

myCellPhone = '9257847406'

textmessage = client.messages.create(to=myCellPhone, from_=TwilioNumber, body=message)

print(textmessage.status)