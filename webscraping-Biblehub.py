import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request



url = 'https://biblehub.com/asv/john/1.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

url = urlopen(req).read()

soup = BeautifulSoup(url, 'html.parser')

print(soup.title.text)
# after running this code, you should get the title of the page as your output

verses_list = soup.findAll('p', class_='reg')

#for verse in verses_list:
    #print(verse.text)
    #input()

verse_list = [v.text.split('.') for v in verses_list]

#print(verse_list)

print(random.choice(random.choice(verse_list)))
# the output of the first random.choice command is another list.
# that is why we need two- the get an individual verse within the list/block