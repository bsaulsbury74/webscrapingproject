from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2
from twilio.rest import Client

url = 'https://crypto.com/price'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

Title = soup.title


tablecells=soup.findAll('tr')


for row in tablecells[1:7]:
    tabledesc= row.findAll('td')
    if tabledesc:
        Name = tabledesc[2].text
        cp= tabledesc[3].text
        cpint=cp.split('$')
        cpint1= cpint[1]
        Rise=tabledesc[3].text

        if '-' in Rise:
            Rise= Rise.split('-')
            Rise= ('-'+ Rise[1])
        else:
            Rise=Rise.split('+')
            Rise=('+'+ Rise[1])
        cpint2=cpint1.lstrip('$')
        cpint2=cpint2.replace(',','')
        cpint2=float(cpint2)


        if'-' in Rise:
            originalprice=Rise.rstrip('%')
            originalprice=originalprice.lstrip('-')
            originalprice=float(originalprice)/100
            originalprice=1+originalprice
            originalprice=originalprice* int(cpint2)

        if '+' in Rise:
            originalprice=Rise.rstrip('%')
            originalprice=originalprice.lstrip('+')
            originalprice=float(originalprice)/100
            originalprice=1-originalprice
            originalprice=originalprice* float(cpint2)

            print(f'Name: {Name}')
            print(f'Current Price:{cpint1}')
            print(f'24 Hour Change:{Rise}')
            print(f'Original Price: {"${:,.2f}".format(originalprice)}')
            print()
            print()
    input()
            
client= Client(keys2.accountSID,keys2.authToken)
TwilioNumber = '+14143481198'

myCellPhone = '9257847406'

textmessage=client.messages.create(to=myCellPhone,from_=TwilioNumber,body="BTC has fallen bellow $40,000")
textmessage1=client.messages.create(to=myCellPhone,from_=TwilioNumber,body="ETH has fallen bellow $3,000")

if Name=="BitcoinBTC" and cpint2<40000:
    print(textmessage)
if Name== "EtherumETH" and cpint2<3000:
    print(textmessage1)
        

        
       

    
    