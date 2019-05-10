#!/usr/bin/env python3

from feedparser import parse

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
    site = "http://feeds.reuters.com/reuters/INtopNews"
    from datetime import date

    top = 15
    print()
    print(color.PURPLE + color.BOLD + "Hi. Welcome to Chews. The following feed uses Reuters RSS source" + color.END + color.END, '\n')
    print("Here are the top news for today,", date.today(), '\n')
    newsfeed = parse(site)
    num = min(top, len(newsfeed['entries']))
    for entry in newsfeed['entries'][:num]:
                title = entry['title']
                print(">", title)
    print()
if __name__ == "__main__":
    main()
