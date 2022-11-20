"""
Get a random episode from a selected TV show
    - Friends
    - How I Met Your Mother
    - Rick and Morty
    - Seinfeld
    - Silicon Valley
    - The Big Bang Theory
    - Young Sheldon
"""

import random
from scrape_episodes import file_dir
import scrape_episodes as se
import sys
import time


def scrape_all_sites() -> None:
    """
    Scrape the TV show websites
    """
    se.get_friends()
    se.get_himym()
    se.get_rick_and_morty()
    se.get_seinfeld()
    se.get_silicon_valley()
    se.get_south_park()
    se.get_tbbt()
    se.get_young_sheldon()


if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv

    if argc == 2:
        if argv[1] == "-y":
            yn = "y"
        elif argv[1] == "-n":
            yn = "n"
        else:
            print("Invalid argument.")
            sys.exit()
    else:
        yn = input("Scrape TV shows (yn): ").lower()

    if yn == "y" or yn == "yes":
        print("Scraping...\r", end="")

        time_start = time.perf_counter()
        scrape_all_sites()
        time_end = time.perf_counter()
        time_diff = time_end - time_start
        print(f"Scraping finished in {time_diff:.1f} seconds.\n")

    print("Show listings:\n")

    print("1) Friends")
    print("2) How I Met Your Mother")
    print("3) Rick and Morty")
    print("4) Seinfeld")
    print("5) Silicon Valley")
    print("6) South Park")
    print("7) The Big Bang Theory")
    print("8) Young Sheldon")

    select_show = input("\nSelect TV show: ").lower()
    match select_show:
        # cases explained in The Big Bang Theory case
        case "1" | "one" | "friends":
            with open(f"{file_dir}/shows/friends.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case "2" | "two" | "himym" | "how i met your mother":
            with open(f"{file_dir}/shows/himym.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case "3" | "three" | "rick" | "morty" | "rick and morty":
            with open(f"{file_dir}/shows/rick_and_morty.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case "4" | "four" | "seinfeld":
            with open(f"{file_dir}/shows/seinfeld.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case "5" | "five" | "silicon" | "valley" | "silicon valley":
            with open(f"{file_dir}/shows/silicon_valley.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case "6" | "six" | "south park":
            with open(f"{file_dir}/shows/south_park.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case "7" | "seven" | "tbbt" | "big bang" | "the big bang theory":
            with open(f"{file_dir}/shows/tbbt.txt") as f:
                # "lines" is a list of all the lines in the file
                lines = f.readlines()
                # randomly select an element from the list excluding
                # the last character (the last character is the newline)
                print(random.choice(lines)[:-1])
        case "8" | "eight" | "young sheldon" | "sheldon":
            with open(f"{file_dir}/shows/young_sheldon.txt") as f:
                lines = f.readlines()
                print(random.choice(lines)[:-1])
        case _:
            print("Not an option.")
