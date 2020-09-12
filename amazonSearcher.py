#interact with amazon shopping experience
#pull reviews
#pull related products to a search
#amazon search options
#save searches
#save date searched, related searches
#review past searches 

def ezSearchURL(product):
    url = "https://www.amazon.com/";
    combo = "s?k=" + '+'.join(words.split());
    return url + combo;

def ezSearchBookURL(info):
    url = "https://www.amazon.com/";
    combo = "s?k=" + '+'.join(info.split()) + "&i=stripbooks"
    return url + combo;

def interface():
    print("Welcome to the Amazon Interaction Interface.")
    while (True):
        print("[S]earch/[s]earch for something new.")
        print("[A]dvanced/[a]dvanced search")
        print("[R]eview/[r]eview past saved searches.")
        print("[H]istory/[h]istory")
        print("[Q]uit/[q[uit")
        choice = input();
        if ((choice == "q") or (choice == "Q")):
            break;
        elif ((choice == "S") or (choice == "s")):
            print("What product would you like to search for?")
            prod = input().strip();
            if ((prod.lower() == "book") or (prod.lower() == "books")):
                print("Maybe you should be a little more specific. What is your book about or related to? (Press ENTER without typing anything to cancel.)")
                info = input().strip()
                if (len(info) == 0):
                    print("Canceling...")
                else:
                    print("Searching for books related to " + info);
            else:
                print("Searching for " + prod);
                url = ezSearchURL(prod);
            

interface();
