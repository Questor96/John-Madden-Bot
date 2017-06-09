import requests
from bs4 import BeautifulSoup

for n in range(1,4):
    url = 'http://www.wikiquotesx.com/authors/john-madden-quotes/' + str(n)
    page_soup = BeautifulSoup(requests.get(url).text, 'html5lib')
    page_quotes = [i.find('a').text for i in page_soup.find_all('blockquote')]
    for i in page_quotes:
        print(i)
