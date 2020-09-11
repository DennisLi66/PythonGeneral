#install requests,beautifulsoup4
import requests
import bs4
import os

# Convert to non-Wikipedia - use similar to feeling lucky

def constructURLfromWord(words):
    print("Generating Wikipedia URL...");
    combo = '_'.join(words.split());
    url = "https://en.wikipedia.org/wiki/" + combo;
    print(url);
    return url;

def extractPage(webpage,words):
    path = "";
    res = requests.get(webpage);
    if (res.status_code != requests.codes.ok):
        raise Exception("Error Code: " + res.status_code);
    path = os.path.join(os.getcwd(),'data','WebPages','Raw',words + '.txt');
    file = open(path,'wb');
    for chunk in res.iter_content(100000):
        file.write(chunk)
    file.close()
    return path;

def convertToPlainText(path):
    return;

def interface():
    print("Welcome to the Website downloader.");
    print(os.path.join(os.getcwd(),'data','WebPages'))
    mostRecentPath = "";
    while (True):
        print("What would you like to do?");
        print("[D]ownload/[d]ownload a webpage.")
        print("[E]xamine/[e]xamine a webpage")
        print("[R]emove/[r]emove a webpage")
        print("[Q]uit/[q]uit");
        choice = input();
        if ((choice == 'D') or (choice == 'd')):
            print("What would you like to search for?");
            pageToDL = input();
            url = constructURLfromWord(pageToDL);
            mostRecentPath = extractPage(url,pageToDL);
        elif ((choice == 'R') or (choice == 'r')):
            print("Which Wikipedia article would you like to remove from your downloads?");
            kill = input();
            kill = '_'.join(words.split());
            path = os.path.join(os.getcwd(),'data','WebPages','Raw',kill + '.txt');
            if (os.path.exists(path)):
                os.unlink(path)
                print(path + " was removed.")
            else:
                print(path + " did not exist.");
        elif ((choice == "Q") or (choice == 'q')):
            break;
        elif ((choice == "E") or (choice == 'e')):
            print("What further command would you like to do?")
            print("[C]onvert/[c]onvert your HTML to text.")
            print("[S]earch/[s]earch for something in your downloaded page.")
            print("[O]pen/[o]pen downloaded document into browser.")
            print("[R]eturn/[r]eturn")
            deepChoice = input();
interface();
