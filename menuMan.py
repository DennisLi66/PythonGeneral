#idea for this site
# user types in a food type
# user types in a location
# pull yelp or google to find relevant places
# try to pull menu
# try to pull reviews
# pull travel distance if specific
# produce info about a particular food - WIkipedia?


def interface():
    print("Welcome to the Food Finder.");
    while (True):
        print("What sort of food are you interested in? (Press Enter without typing anything to quit.)")
        food = input().strip();
        if (len(food) == 0):
            print("Quitting...")
            break;
        elif (!food.isalpha()):
            print("Please type a genre of food, such as seafood, or a food name, like hamburger.")
        else:
            


interface()
