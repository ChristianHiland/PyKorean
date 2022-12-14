# All the words in a dir
words = {
    # Greetings
    "hello": "hello: 안녕하세요: annyeonghaseyo",
    
    # Answering words
    "yes": "yes: 네: ne",
    "no": "no: 아니요: aniyo",
    
    # Time
    "time": "time: 시각: sigak",
    "times": "times: 타임스: taimseu",
    "day": "day: 낮: nach",
    
    # Things
    "gas": "gas: 가스: gaseu",
    "air": "air: 공기: gongki",
    "language": "language: 언어: eoneo",
    "word": "word: 단어: daneo",
    "news": "news: 뉴스: nyuseu",

    # Places
    "country": "country: 국가: gukga",
    "store": "store: 가게: gake",
    "at": "at: ~에: ~e",
    
    # Movement
    "back": "back: 뒤: dwi",
    "go": "go: 가요: ga",
    "away": "away: 떨어져 있는: ddeoleojyeo ssneun",
    
    # Actions
    "take": "take: 테이크: teipeu",
    
    # Pronouns & People
    "you": "you: 너: ne",
    "mr": "Mr, Ms, Mrs: 씨: ssi",
    "i": "I: 나: na",
    "she": "she: 여자: yeocha",
    "he": "he: 그: geu",
    "they": "they: 그들: geudeul",
    "we": "we: 나: na",
    "all": "all: 다: da",
    "german": "german: 독일 사람: donil saram",
    "person": "person: 사람: saram",
    "foreign": "foreign: 외국의: winunui",
    
    # Asking words
    "how": "how: 어떻게: eoddeohge",
    
    # Other
    "to": "to: 에게: ege",
    
    # Feel
    "cold": "cold: 추운: chun",
    "alone": "alone: 홀로: hodlo",
    
    # Animals
    "cat": "cat: 고양이: goyeongi",
    "dog": "dog: 개: gae",
    "fish": "fish: 생선: saengseon",
}

# The greetings
greetings = {
    "how are you": "How are you?: 안녕하십니까?: annyeonghasibnigga?"
}

numbers = {
    "one": "One: 하나: hana"
}
numberss = {
    "one": "One: 일: il",
    "1": "One: 일: il"
}

# Gets the user input for the choise
print("////////////////////////////////////////////////")
print("/////               Options                /////")
print("/////  1. find the words 2. List all words /////")
print("/////  3. Greetings      4. Numbers        /////")
print("////////////////////////////////////////////////")
print("       ")
option = input("Option: ")

if option == str(1):
    word = input("Word: ")
    # Gets the user input and then goes to the words dir to get the word.
    print(" ")
    theword = words[str(word)]
    print(theword.replace(":", ","))
elif option == str(2):
    print(words)
elif option == str(3):
    greeting = input("Greeting: ")
    print(" ")
    thewords = greetings[str(greeting)]
    print(thewords.replace(":", ","))
elif option == str(4):
    number = input("#: ")
    print(" ")
    print("Native Korean")
    print(numbers[str(number)])
    print(" ")
    print("Sino Korean")
    print(numberss[str(number)])
else:
    print("Sorry that's that an option.")
    
