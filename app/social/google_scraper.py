import requests
from bs4 import BeautifulSoup

def GoogleAnalysis(term):
    url = 'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(
        term)
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html5lib')
    headline_results = soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd')
    websites = soup.find_all('div', class_='BNeawe UPmit AP7Wnd')

    body = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    main = soup.find_all('div', class_='kCrYT')

    headline = []
    links = []

    for i in range(0, len(main)):
        links.append(main[i].find("a")['href'])

    for i in range(0, len(headline_results), 1):
        link = links[i][7:]
        link = link.split('&sa')[0]
        b = {
            "title": headline_results[i].text,
            'website': websites[i].text,
            'body': body[i].text,
            'link': link
        }
        headline.append(b)
    return headline
   