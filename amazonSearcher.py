#interact with amazon shopping experience
#pull reviews
#pull related products to a search
#amazon search options
#save searches
#save date searched, related searches
#review past searches 

def ezURL(product):
    url = "";
    return url;

def interface():
    print("Welcome to the Amazon Interaction Interface.")
    while (True):
        print("[S]earch/[s]earch for something new.")
        print("[A]dvanced/[a]dvanced search")
        print("[R]eview/[r]eview past saved searches.")
        print("[H]istory/[h]istory")
        print("[Q]uit/[q[uit")
        choice = input();
        if ((choice == "q") and (choice == "C")):
            break;
        elif ((choice == "S") and (choice == "s")):
            print("What product would you like to search for?")
            prod = input();
            

interface();
