#install requests
import requests
import os


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

def interface():
    print("Welcome to the Web Retrieval and Action area.");
    print(os.path.join(os.getcwd(),'data','WebPages'))
    mostRecentPath = "";
    while (True):
        print("What would you like to do?");
        print("[D]ownload/[d]ownload a webpage")
        choice = input();
        if ((choice == 'D') or (choice == 'd')):
            print("Which page would you like to extract?");
            pageToDL = input();
            url = constructURLfromWord(pageToDL);
            mostRecentPath = extractPage(url,pageToDL);
    
interface();