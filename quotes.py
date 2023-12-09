from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

authordict = {}
tagdict = {}
quote_list = []
longest_quote = ""
shortest_quote = "This is a short dummy quote, I hope this works haha"
totalwordcount = 0

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

        if len(quote) > len(longest_quote):
            longest_quote = quote
            longquoteauth = author

        if len(quote) < len(shortest_quote):
            shortest_quote = quote 
            shortquoteauth = author

        quotewords = quote.split()
        for word in quotewords:
            totalwordcount += 1


totalquotes = len(quote_list)
avgquotes = totalwordcount/totalquotes


authordict_sorted1 = sorted(authordict.items(), key = lambda x:x[1], reverse = True)
sorted_authordict = dict(authordict_sorted1)

author_keys_list = list(sorted_authordict.keys())
author_values_list = list(sorted_authordict.values())

top_10_authors = author_keys_list[:10]
top_10_authors_quotes = author_values_list[:10]



tagdict_sorted1 = sorted(tagdict.items(), key = lambda x:x[1], reverse = True)
sorted_tagdict = dict(tagdict_sorted1)

tag_keys_list = list(sorted_tagdict.keys())
tag_values_list = list(sorted_tagdict.values())

top_10_tags = tag_keys_list[:10]
top_10_tags_num = tag_values_list[:10]


from plotly.graph_objs import Bar
from plotly import offline

# top 10 most quoted authors
data = [
    {
        "type":"bar",
        "x": top_10_authors,
        "y": top_10_authors_quotes,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width": 1.5, "color":"rgb(25,25,25)"}
        },
        "opacity": 0.6, 
    }
]

my_layout = {
    "title": "Top 10 Most Quoted Authors",
    "xaxis": {"title": "Author"},
    "yaxis": {"title": "Number of Quotes"}
}

fig = {"data": data, "layout": my_layout }

offline.plot(fig, filename = "author_analysis.html")

# top 10 most popular tags 
data2 = [
    {
        "type":"bar",
        "x": top_10_tags,
        "y": top_10_tags_num,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width": 1.5, "color":"rgb(25,25,25)"}
        },
        "opacity": 0.6, 
    }
]

my_layout = {
    "title": "Top 10 Most Popular Tags",
    "xaxis": {"title": "Tag"},
    "yaxis": {"title": "Number of Times Mentioned"}
}

fig = {"data": data2, "layout": my_layout }

offline.plot(fig, filename = "tag_analysis.html")


print(f"\nQuotes per author: {authordict}")
print(f"\nThe author with the most quotes was {max(authordict, key=authordict.get)}")
print(f"\nThe author with the least quotes was {min(authordict, key=authordict.get)}")
print(f"\nThe average length per quote was {avgquotes} words")
print(f"\nThe longest quote, at {len(longest_quote.split())} words, was: {longest_quote} - {longquoteauth}")
print(f"\nThe shortest quote, at {len(shortest_quote.split())} words, was: {shortest_quote} - {shortquoteauth}")
print(f"\nTag distribution: {tagdict}")
print(f"\nThe most popular tag was {max(tagdict, key=tagdict.get)}, mentioned {max(tagdict.values())} times")
print(f"\nA total of {len(tagdict)} tags were used")
