#interact with amazon shopping experience
#pull reviews
#pull related products to a search
#amazon search options
#save searches
#save date searched, related searches
#review past searches 

#DEAD CODE - NEED AMAZON API, CANNOT BE WEB SCRAPED


import requests, webbrowser, urllib.parse, datetime
import bs4
import os

def ezSearchURL(product):
    url = "https://www.amazon.com/";
    combo = "s?k=" + '+'.join(product.split());
    return url + combo;

def ezSearchBookURL(info):
    url = "https://www.amazon.com/";
    combo = "s?k=" + '+'.join(info.split()) + "&i=stripbooks"
    return url + combo;

def obtainPage(url):
    print("URL: " + url);
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }
    res = requests.get(url,headers=headers);
    if (res.status_code != requests.codes.ok):
        print("Error Code: " + str(res.status_code))
        raise Exception("Error Code: " + str(res.status_code));
    bS = bs4.BeautifulSoup(res.text,"html.parser");
    path = os.path.join(os.getcwd(),'data','amazonSearcher','history.txt');
    file = open(path,'a');
    file.write(res.text)
    file.close()

def writeToHistory(searchedproduct,pageName="",URL = ""):
    path = os.path.join(os.getcwd(),'data','amazonSearcher','history.txt');
    file = open(path,'a');
    time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S");
    #file.write(str(time)+'\n')
    file.close()
    

def interface():
    print("Welcome to the Amazon Interaction Interface.")
    while (True):
        print("[S]earch/[s]earch for something new.")
        print("[A]dvanced/[a]dvanced search")
        print("[R]eview/[r]eview past saved searches.")
        print("[H]istory/[h]istory")
        print("[Q]uit/[q]uit")
        choice = input();
        if ((choice == "q") or (choice == "Q")):
            break;
        elif ((choice == "S") or (choice == "s")):
            print("What product would you like to search for?")
            prod = input().strip();
            url = "";
            if ((prod.lower() == "book") or (prod.lower() == "books")):
                print("Maybe you should be a little more specific. What is your book about or related to? (Press ENTER without typing anything to cancel.)")
                info = input().strip()
                if (len(info) == 0):
                    print("Canceling...")
                else:
                    print("Searching for books related to " + info);
                    url = ezSearchURL(info);
                    prod = info + "books";
            else:
                print("Searching for " + prod);
                url = ezSearchURL(prod);
                obtainPage(url)
            
            

interface();
