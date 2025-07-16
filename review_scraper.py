import requests
from bs4 import BeautifulSoup

def scrape():

    url = 'https://steamcommunity.com/app/3527290/positivereviews/?browsefilter=toprated&snr=1_5_100010_'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find_all("div", {"class":"apphub_CardContentMain"})
    for review in reviews:
        for string in review.stripped_strings:
            print(string)
        print("\n\n")

if __name__ == '__main__':
    scrape()
