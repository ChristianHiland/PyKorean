import module
type = input("What langage are you from? ")

if type == 'English':
    module.english.korean()
    print("Here you go.")
elif type == 'Korean':
    module.korean.english()
    print("Here you go.")
else:
    print("Sorry we don't have that language. :(")
