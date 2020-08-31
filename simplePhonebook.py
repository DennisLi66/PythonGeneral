import shelve;
import re;

def printEntry(name,entry):
    print(name);
    print(entry[0]);
    print(entry[1]);
    print('\n')

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
            print("Printing all entries...\n")
            for v in data:
                printEntry(v,data[v]);
            print("Printing done.")
        #QUITTING
        elif ((choice == "Q") or (choice == "q")):
            print("Quitting");
            break;
        #DELETING
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
        #SEARCHING
        elif ((choice == "S") or (choice == "s")):
            print("Who's information would you like to retrieve?");
            info = input();
            tInfo = data.get(info,0);
            if (tInfo == 0):
                print("Entry Not Found.");
            else:
                printEntry(info,tInfo);
        #ADDING
        elif ((choice == "A") or (choice == "a")):
            print("What is the name of the person you want to add?");
            #Some places let you name your kid with any character on a keyboard - go with that
            name = input();
            print("What is their phone number?");
            print("Formatting: (123)456-7890 ");
            #match against a regex
            #^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$
            pRegex = re.compile("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$")
            pNum = "";
            while (True):
                pNum = input();
                if (pRegex.match(pNum)):
                    break;
                else:
                    print("Sorry, that didn't work. Please retype the number.");
                    print("Formatting: (123)456-7890 ");
            print("Any notes you would like to write about this person?");
            Notes = input();
            data[name] = (pNum,Notes);
            print("Here is your entry.")
            printEntry(name,data[name]);
    data.close();





runBook();
