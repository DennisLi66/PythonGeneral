import requests
import bs4
import os

def openPage():
    return;

def obtainHTMLfromURL(url):
    print("URL: " + url);
    res = requests.get(url)
    if (res.status_code != requests.codes.ok):
        raise Exception("Error Code: " + res.status_code);
    bSObj = bs4.BeautifulSoup(res.text);
    links = bSObj.select('r');
    print(links);

def createListofLinks(text):
    

def produceGoogleLink(words):
    link = "https://www.google.com/search?q=";
    combo = '_'.join(words.split());
    return link + combo;

def interface():
    print("Welcome to the I'm Feeling Lucky Spawner.")
    while (True):
        print("[P]roduce/[p]roduce ten pages from Google's I'm feeling lucky.")
        print("[Q]uit/[q]uit")
        choice = input();
        if ((choice == "Q") or (choice == "q")):
            break;
        elif ((choice == "P") or (choice == "p")):

        else:
            print("Sorry, didn't catch that. You're going to have to try again.")


interface();
