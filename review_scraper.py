import requests
from bs4 import BeautifulSoup

GAME_ID = "632470"
TYPE = "positivereviews"
FILTER = "mostrecent"
PAGE = "1"


FUNNY = "funny"

# I'm going to discard every review under 5 words because this type of reviews usually are obscure reference to the game and not a proper review

def scrape_reviews():

    url = f'https://steamcommunity.com/app/{GAME_ID}/{TYPE}/?browsefilter={FILTER}&snr=1_5_100010_&p={PAGE}'
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find_all("div", {"class":"apphub_CardContentMain"})

    print(f"{len(reviews)} REVIEWS ENCOUNTERED\n")
    n = 0
    funny = "No one has rated this review as funny yet"
    badges = "0"
    for review in reviews:
        i = 0
        for string in review.stripped_strings:
            if i == 0:
                helpfull = string
            elif i == 1:
                if FUNNY in string:
                    funny = string
                    i-=1
                else:
                    badges = string
            elif i == 2:
                recommended = string
            elif i == 3:
                hours = string
            elif i == 5:
                review_text = string
            i += 1
        print(f"HELLPFUL: {helpfull}")
        print(f"FUNNY: {funny}")
        print(f"BADGES: {badges}")
        print(f"RECOMMENDED: {recommended}")
        print(f"HOURS: {hours}")
        print(f"REVIEW: {review_text}")
        print("\n")
            
    
    
if __name__ == '__main__':
    scrape_reviews()
