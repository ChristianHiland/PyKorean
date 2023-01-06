from dictWord import words
from dictWord import greetings
from dictWord import numbers
from dictWord import numberss
from dictWord import sets

def option1():
    word = input("Word: ")
    # Gets the user input and then goes to the words dir to get the word.
    print(" ")
    theword = words[str(word)]
    print(theword.replace(":", ","))
    continued  = input("Continue? [Y/N]: ")
    if continued == "Y":
        option1()
    else:
        whilestate()
def option3():
    greeting = input("Greeting: ")
    print(" ")
    thewords = greetings[str(greeting)]
    print(thewords.replace(":", ","))
    continued  = input("Continue? [Y/N]: ")
    if continued == "Y":
        option2()
    else:
        whilestate()
def option4():
    number = input("#: ")
    print(" ")
    print("////// Native Korean //////")
    print(numbers[str(number)])
    print(" ")
            
    print("//////  Sino Korean  //////")
    print(numberss[str(number)])
    continued  = input("Continue? [Y/N]: ")
    if continued == "Y":
        option2()
    else:
        whilestate()
# The 
def option5():
    
    # Telling the user what sets there are.
    print("/////////////////////////////////////////////////////////////////////////////")
    print("//// Set 1: This set includes the pronunciation of 'ㄴ ㅇ ㄷ ㅅ ㄱ'        ////")
    print("//// Set 1a: This set includes the pronunciation rules of 'ㄴ ㅇ ㄷ ㅅ ㄱ' ////")
    print("//// Set 2 This set includes the pronunciation of 'ㅁ ㅏ ㅣ ㅗ ㅔ'         ////")
    print("//// Set 2a: This set includes the pronunciation rules of 'ㅁ ㅏ ㅣ ㅗ ㅔ' ////")
    print("/////////////////////////////////////////////////////////////////////////////")
    print("")
    print("Each set has different lessons on how to pronounce each letter.")
    set = input("Set #: ")
    theset = sets[str(set)]
    print(theset)
    continued  = input("Continue? [Y/N]: ")
    if continued == "Y":
        option1()
    else:
        whilestate()

def whilestate():
    option = input("Option: ")
    le = 0
    while le < 1:
        if option == str(1):
            option1()
        elif option == str(2):
            print(words)
            le += 1
        elif option == str(3):
            option3()
        elif option == str(4):
            option4()
        elif option == str(5):
            option5()
        else:
            print("Sorry that's that an option.")
            le += 1
            whilestate()

# Gets the user input for the choise
print("////////////////////////////////////////////////")
print("/////               Options                /////")
print("/////  1. find the words 2. List all words /////")
print("/////  3. Greetings      4. Numbers        /////")
print("////////////////////////////////////////////////")
print("       ")
whilestate()
