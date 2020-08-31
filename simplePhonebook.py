import os;
import shelve;

def printEntry(name,entry):
    print(name);
    print(entry[0]);
    print(entry[1]);

def runBook():
    print("Welcome to Dennis' simple phonebook")
    data = shelve.open("data/simplePhonebook");
    while (True):
        print(
"""
[A]dd/[a]dd an entry to the phonebook.
[D]elete/[d]elete an entry from the phonebook.
[E]dit/[e]dit an entry
[S]earch/[s]earch for a specific entry
[P]rint/[p]rint all entries.
[Q]uit/[q]uit """)
        choice = input();
        #PRINTING
        if ((choice == "P") or (choice == "p")):
            print("Printing all entries...")
            for v in data:
                print(v);
            print("Printing done.")
        #QUITTING
        elif ((choice == "Q") or (choice == "q")):
            print("Quitting");
            break;
        elif ((choice == "D") or (choice == "d")):
            print("Who's information would you like to delete?");
            name = input();
            toDel = data.get(name,0);
            if (toDel == 0):
                print("Entry Not Found.")
            else:
                print("Are you sure you want to delete this entry?");
                printEntry(name,toDel);
                print("[Y]es/[y]es");
                print("[N]o/[n]o");
                tELLME = input();
                if ((tELLME == "Y") or (tELLME == "y")):
                    data.pop(name,None);
                elif ((tELLME == "N") or (tELLME == "n")):
                    print("Stopping Deletion.");
                else:
                    print("Not a valid choice; stopping deletion.");
        elif ((choice == "S") or (choice == "s")):
            print("Who's information would you like to retrieve?");
            info = input();
            tInfo = data.get(info,0);
            if (tInfo == 0):
                print("Entry Not Found.");
            else:
                printEntry(info,tInfo);
        elif ((choice == "A") or (choice == "a")):
            print("What is the name of the person you want to add?");
            name = input();
            print("What is their phone number?");
            #match against a regex
            #^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$
    data.close();





runBook();
