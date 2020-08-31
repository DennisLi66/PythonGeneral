import numberGuesser
import simplePhonebook as simpPBK 

while (True):
    print("Welcome to Dennis' misc Python codes");
    print('Press [0] for the number guesser');
    print('Press [1] for the simple phonebook');
    choice = input();
    if (choice == '0'):
        print("You selected Number Guesser!");
        numberGuesser.numberGuesser();
    if (choice == '1'):
        print("You selected Simple Phonebook");
        simpPBK.populate();
        simpPBK.runBook();




