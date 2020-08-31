import numberGuesser
import simplePhonebook as simpPBK 

while (True):
    print("Welcome to Dennis' misc Python codes");
    print('Press [0] for the number guesser');
    print('Press [1] for the simple phonebook');
    print('[Q]uit/[q]uit');
    choice = input();
    if (choice == '0'):
        print("You selected Number Guesser!");
        numberGuesser.numberGuesser();
    elif (choice == '1'):
        print("You selected Simple Phonebook");
        simpPBK.runBook();
    elif ((choice == 'Q') or (choice == 'q')):
        break;
    


