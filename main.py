import module
type = input("What langage are you from? ")

if type == 'English':
    module.english.korean()
elif type == 'Korean':
    module.korean.english()
else:
    print("Sorry we don't have that one. :(")
