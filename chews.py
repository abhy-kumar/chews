#!/usr/bin/env python

import click
import feedparser

@click.command()
def main():
    val = 15
    print("Hi. Welcome to Chews. The following feed uses Reuters RSS source\n")
    print("Here are the top news for today:")
    d = feedparser.parse("http://feeds.reuters.com/reuters/INtopNews")
    num = min(val, len(d['entries']))
    for entry in d['entries'][:num]:
                title = entry['title']
                print("> " + title)
                callback = lambda link=entry['link']: openSite(link)

if __name__ == "__main__":
    main()
