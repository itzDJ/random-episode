"""Module contained functions to scrape the episodes of the shows"""

from bs4 import BeautifulSoup
from pathlib import Path
import requests

file_dir = Path(__file__).parent.absolute()

# functions explained in The Big Bang Theory function


def get_friends() -> None:
    """Function to scrape the episodes of Friends to a text file"""
    url = "https://epguides.com/Friends/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/friends.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[29:29 + 236]):
            f.write(f"{info.text} | {title.text}\n")


def get_himym() -> None:
    """Function to scrape the episodes of How I Met Your Mother to a text file"""  # noqa
    url = "https://epguides.com/HowIMetYourMother/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/himym.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[29:29 + 208]):
            f.write(f"{info.text} | {title.text}\n")


def get_rick_and_morty() -> None:
    """Function to scrape the episodes of Rick and Morty to a text file"""
    url = "https://epguides.com/RickAndMorty/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/rick_and_morty.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[26:26 + 51]):
            f.write(f"{info.text} | {title.text}\n")


def get_seinfeld() -> None:
    """Function to scrape the episodes of Seinfeld to a text file"""
    url = "https://epguides.com/Seinfeld/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/seinfeld.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[47:47 + 180]):
            f.write(f"{info.text} | {title.text}\n")


def get_silicon_valley() -> None:
    """Function to scrape the episodes of Silicon Valley to a text file"""
    url = "https://epguides.com/SiliconValley/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/silicon_valley.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[33:33 + 53]):
            f.write(f"{info.text} | {title.text}\n")


def get_south_park():
    """Function to scrape the episodes of South Park to a text file"""
    url = "https://epguides.com/southpark/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/south_park.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[32:32 + 313]):
            f.write(f"{info.text} | {title.text}\n")


def get_tbbt() -> None:
    """Function to scrape the episodes of The Big Bang Theory to a text file"""

    # epguides is a good website to scrape the episodes of the shows
    url = "https://epguides.com/bigbangtheory/"

    # "page" stores the html of the page using "requests.get"
    # without ".text", the response number is returned (200 for success)
    page = requests.get(url).text

    # "BeautifulSoup" is used to parse the html
    # "page" is the html of the page
    # "html.parser" is the parser used
    soup = BeautifulSoup(page, "html.parser")

    # the episode info (season and episode number) is stored in the <td> tag
    epinfo = soup.find_all("td", class_="epinfo left pad")

    # the episode titles are stored in the <a> html tags
    eptitle = soup.find_all("a")

    # the episode info and titles are stored in a text file
    with open(f"{file_dir}/shows/tbbt.txt", "w") as f:
        # zip function used to traverse the two lists at the same time

        # the "eptitles" list has more elements than just the episode titles
        # the "36"th element of that list is the first episode of season 1
        # there are 279 episodes in the series so
        # the element of the last episode is 36 + 279
        for info, title in zip(epinfo, eptitle[36:36 + 279]):
            f.write(f"{info.text} | {title.text}\n")


def get_young_sheldon() -> None:
    """Function to scrape the episodes of Young Sheldon to a text file"""
    url = "https://epguides.com/youngsheldon/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")

    epinfo = soup.find_all("td", class_="epinfo left pad")
    eptitle = soup.find_all("a")

    with open(f"{file_dir}/shows/young_sheldon.txt", "w") as f:
        for info, title in zip(epinfo, eptitle[29:29 + 105]):
            f.write(f"{info.text} | {title.text}\n")
