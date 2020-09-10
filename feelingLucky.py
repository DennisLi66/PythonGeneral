import requests, webbrowser, urllib.parse
import bs4
import os

def prettyPrint(superList):
    for x in range(len(superList)):
        print("[" + str(x) + "]:" + superList[x][0] + " (" + superList[x][1] + ")");
        #print("[" + str(x) + "]:" + superList[x][1]);

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
    

def produceGoogleLink(words,offset = 0):
    link = "https://www.google.com/search?q=";
    combo = '+'.join(words.split());
    return link + combo + "&start=" + str(offset);

def interface():
    print("Welcome to the Google Search Site Spawner.")
    offset = 0;
    while (True):
        print("[P]roduce/[p]roduce the first page of results from Google Search.")
        print("[Q]uit/[q]uit")
        choice = input();
        if ((choice == "Q") or (choice == "q")):
            break;
        elif ((choice == "P") or (choice == "p")):
            print("What would you like to search?")
            words = input();
            url = produceGoogleLink(words);
            try:
                mList = obtainHTMLfromURL(url);
            except:
                print("Something went wrong. Returning to hub.")
            if (len(mList) == 0):
                print("Unfortunately, no results for " + words + " exists.")
            else:
                cleanMessyURL(mList);
                while (True):
                    print("\nType a given number to open the associated website.")
                    print("[O]pen/[o]pen all sites shown.");
                    prettyPrint(mList);
                    if (offset > 0):
                        print("[P]revious/[p]revious page")
                    print("[N]ext/[n]ext page")
                    print("[C]ancel/[c]ancel");
                    iChoice = input();
                    if ((iChoice == "C") or (iChoice == "c")):
                        print('\n')
                        break;
                    elif (iChoice.isnumeric()):
                        num = int(iChoice);
                        if ((num < 0) or (num >= len(mList))):
                            print("Sorry, that isn't an applicable number.")
                        else:
                            print("Opening: " + mList[num][1]);
                            webbrowser.open(mList[num][1])
                    elif ((iChoice == "O") or (iChoice == "o")):
                        for tupl in mList:
                            print("Opening: " + tupl[1]);
                            webbrowser.open(tupl[1]);
                    elif ((iChoice == "N") or (iChoice == "n")):
                        offset += 10;
                        url = produceGoogleLink(words,offset);
                        try:
                            nList = obtainHTMLfromURL(url);
                        except:
                            print("Something went wrong. Returning to hub.")
                        if (len(nList) == 0):
                            print("Unfortunately, no more results for " + words + " exist.")
                            offset -= 10;
                        else:
                            mList = nList;
                            cleanMessyURL(mList);
                    elif (((iChoice == "P") or (iChoice == "p")) and offset > 0):
                        offset -= 10;
                        url = produceGoogleLink(words,offset);
                        try:
                            mList = obtainHTMLfromURL(url);
                            cleanMessyURL(mList);
                        except:
                            print("Something went wrong. Returning to hub.")
        else:
            print("Sorry, didn't catch that. You're going to have to try again.")
            
