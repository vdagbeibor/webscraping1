import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

random_chapter = random.choice(list(range(1,22)))

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)

else: 
    random_chapter = str(random_chapter)



url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'
# remember, you can create urls dynamically
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

url = urlopen(req).read()

soup = BeautifulSoup(url, 'html.parser')

print(soup.title.text)

'''verses_list = soup.findAll('div', class_='p')

verse_list = [v.text.split('.') for v in verses_list]

print(random.choice(random.choice(verse_list)))'''

# OR

page_verses = soup.findAll('div', class_='main')

for verses in page_verses:
    verse_list = verses.text.split(".")


mychoice = random.choice(verse_list[:-5])
# ^ omits last 5 elements
# how come we didn't have to do random.choice twice this time? 
verse = f'Chapter: {random_chapter} Verse: {mychoice}'

print(verse)

import keys
from twilio.rest import Client 

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+18449471862"

myCellPhone = "+17577074649"

textmessage = client.messages.create(to = myCellPhone, from_ = TwilioNumber, body = verse)


