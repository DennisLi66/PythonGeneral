import requests, webbrowser, urllib.parse
import bs4
import os

def prettyPrint(superList):
    for x in range(len(superList)):
        print("[" + str(x) + "]:" + superList[x][0]);
        print("[" + str(x) + "]:" + superList[x][1]);

def cleanMessyURL(superList):
    for i in range(len(superList)):
        c = superList[i][1][7:];
        #print(superList[i][1][7:])
        rex = c.rfind("&sa=U&ved=")
        c = c[0:rex]
        c = urllib.parse.unquote(c)
        superList[i] = (superList[i][0],c);
        


def obtainHTMLfromURL(url):
    print("URL: " + url);
    res = requests.get(url)
    if (res.status_code != requests.codes.ok):
        raise Exception("Error Code: " + res.status_code);
    bS = bs4.BeautifulSoup(res.text,"html.parser");
    #bS = bS.prettify();
    #links = bS.find_all('div div div', attrs={'class':'r'});
    superList = [];

    listsC = bS.findAll("div", {"class": "ZINbbc xpd O9g5cc uUPGi"})
    listsD = [];
    listsA = [];
    listsB = []
    for i in range(len(listsC)):
        plac = listsC[i].findAll("div", {"class": "kCrYT"})
       # print(len(plac) > 0);
        if (len(plac) > 0):
            listsD.append(plac[0])
    for u in range(len(listsD)):
        if (len(listsD[u].findAll("div", {"class": "BNeawe vvjwJb AP7Wnd"})) > 0):
            listsA.append(listsD[u].findAll("div", {"class": "BNeawe vvjwJb AP7Wnd"})[0])
        if (len(listsD[u].select('a')) > 0):
            listsB.append(listsD[u].select('a')[0])
    

    for l in range(len(listsA)):
        superList.append((listsA[l].getText(),listsB[l].get('href')))
        #print(listsA[l])
        #print(listsB[l])
    return superList;
    
    
def produceGoogleLink(words):
    link = "https://www.google.com/search?q=";
    combo = '+'.join(words.split());
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
            print("What would you like to search?")
            words = input();
            url = produceGoogleLink(words);
            mList = obtainHTMLfromURL(url);
            cleanMessyURL(mList);
            prettyPrint(mList);
        else:
            print("Sorry, didn't catch that. You're going to have to try again.")


interface();
