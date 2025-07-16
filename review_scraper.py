import requests
from bs4 import BeautifulSoup
from selenium import webdriver

TYPE = ["positivereviews", "negativereviews"]
FILTER = ["mostrecent", "toprated"]

FUNNY = "funny"

# I'm going to discard every review under 5 words because this type of reviews usually are obscure reference to the game and not a proper review

# Scrap relevant game ids from here https://store.steampowered.com/search/?term=


def scrape_games():
    url = f'https://store.steampowered.com/search/?term='

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    game_ids = []
    games = soup.find_all("a")
    for game in games:
        if game.has_attr("data-ds-appid"):
            game_ids.append(game.get("data-ds-appid"))
    return game_ids


def scrape_game(game_id):
    url = f'https://store.steampowered.com/app/{game_id}/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    name = soup.find("div", {"class": "apphub_AppName"})
    genre = soup.find("span", {"data-panel": '{"flow-children":"row"}'})

    print(name.text)
    print(genre.text)
    # I should also scrap the price
    print("\n")


def scrape_reviews(game_id, type, filter):

    url = f'https://steamcommunity.com/app/{game_id}/{type}/?browsefilter={filter}&snr=1_5_100010_&p=1&filterLanguage=english'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    reviews = soup.find_all("div", {"class": "apphub_CardContentMain"})

    funny = "No one has rated this review as funny yet"
    badges = "0"
    review_count = len(reviews)
    for review in reviews:
        i = 0
        for string in review.stripped_strings:
            match i:
                case 0:
                    helpfull = string
                case 1:
                    if FUNNY in string:
                        funny = string
                        i -= 1
                    else:
                        badges = string
                case 2:
                    recommended = string
                case 3:
                    hours = string
                case 5:
                    review_text = string
            i += 1
        print(f"HELPFULL: {helpfull}")
        print(f"FUNNY: {funny}")
        print(f"BADGES: {badges}")
        print(f"RECOMMENDED: {recommended}")
        print(f"HOURS: {hours}")
        print(f"REVIEW: {review_text}")
        print("\n")
    return review_count


if __name__ == '__main__':
    game_ids = scrape_games()
    review_count = 0
    for game_id in game_ids:
        scrape_game(game_id)
        for filter in FILTER:
            for type in TYPE:
                review_count += scrape_reviews(game_id, type, filter)
    print(f"{review_count} REVIEWS ENCOUNTERED\n")
