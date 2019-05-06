#!/usr/bin/env python

import click
import feedparser

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

@click.command()
def main():

    import datetime
    today = datetime.date.today()
    mylist = []
    mylist.append(today)

    val = 15
    print("\n")
    print('\033[95m' + '\033[1m'+"Hi. Welcome to Chews. The following feed uses Reuters RSS source\n"+'\033[0m' + '\033[0m')
    print("Here are the top news for today, " + str(mylist[0]) + "\n")
    d = feedparser.parse("http://feeds.reuters.com/reuters/INtopNews")
    num = min(val, len(d['entries']))
    for entry in d['entries'][:num]:
                title = entry['title']
                print("> " + title)
                callback = lambda link=entry['link']: openSite(link)
    print("\n")
if __name__ == "__main__":
    main()
