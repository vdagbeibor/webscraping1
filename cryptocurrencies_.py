from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.webull.com/quote/crypto'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

#print(soup.title.text)

crypto_data = soup.findAll("div", attrs = {'class':'table-cell'})

#symbol = ("div", attrs = {'class':'csr118})

counter = 1
for x in range(5):
    name = crypto_data[counter].text
    last_price =float(crypto_data[counter + 1].text.replace(',',''))
    change_string = crypto_data[counter + 2].text
    change_sign = change_string[0]
    
    if change_sign == '+':
        change = float(crypto_data[counter + 2].text.strip('+').strip('%'))/100
        prev_price = last_price / (1 + change)
    else:
        change = float(crypto_data[counter + 2].text.strip('-').strip('%'))/100
        prev_price = last_price / (1 - change)

    print(name)
    print(last_price)
    print(change)
    print(prev_price)
    input()

    counter += 10
    
    

    if name == "EEthereumETHUSD" and last_price > 2000:
        import keys 
        from twilio.rest import Client 

        client = Client(keys.accountSID, keys.authToken)

        TwilioNumber = "+18449471862"

        myCellPhone = "+17577074649"

        message = "Hi there Professor Bhojwani! The cryptocurrency value for Etherium is above $2000! Let's get selling!"

        textmessage = client.messages.create(to = myCellPhone, from_ = TwilioNumber, body = message)
        
        print(textmessage.status)
        
