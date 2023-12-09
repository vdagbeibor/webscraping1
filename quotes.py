from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

authordict = {}
tagdict = {}
quote_list = []

for page_number in range(11): 

    url = 'http://quotes.toscrape.com/page/' + str(page_number) + '/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

    req = Request(url, headers = headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    #print(soup.title.text)
    quotes_data = soup.findAll("div", class_='quote')
    # each element in this list contains a quote and its accessory info (author, tags)
    
    
    for q in quotes_data: 
        quote = q.find("span", class_='text').text
        quote_list.append(quote)
        author = q.find("small", class_='author').text
        tags_data = q.findAll("a", class_='tag')
        for t in tags_data:
            tag = t.text
            if tag in tagdict: 
                tagdict[tag] += 1
            else:
                tagdict[tag] = 1

        if author in authordict:
            authordict[author] += 1
        else:
            authordict[author] = 1

print(authordict)
print(tagdict)
print(quote_list)





totalquotes = len(quote_list)
print(f"\nQuotes by author: authordict")
print(f"\nAuthor with the most quotes: {max(authordict, key=authordict.get)}")
print(f"\nAuthor with the least quotes: {min(authordict, key=authordict.get)}")
print(f"\nAverage length per quote: {avg_quotes} words per quote")
print(f"\nLongest Quote ({len(longest_quote.split())} words): {longest_quote} - {lquoteauth}")
print(f"\nShortest Quote ({len(shortest_quote.split())} words): {shortest_quote} - {squoteauth}")
print(f"\nMost Popular Tag: {max(tag_dict, key=tag_dict.get)} ({max(tag_dict.values())} times)")
print(f"\nTotal tags: {len(tagdict)}")
      

    


















