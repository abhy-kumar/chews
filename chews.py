import feedparser
import appdirs
import os
import sys
import webbrowser
import errno

appauthor = "Abhishek Kumar"  # If the data directory doesn't exist, create it
datadir = appdirs.user_data_dir(appname, appauthor)
if (not os.path.isdir(datadir)):
    os.makedirs(datadir)

path = os.path.join(datadir, "sites.txt")

d = feedparser.parse("*link here, tba*")
for i in range (0:):
    d.entries[i].title

