# This contans the words in Korean
#Importing tkinter
import tkinter as tk

def koreantk():
    #Making the instance
    english= Tk
    #Setting the geometry of the window
    english.geometry("600X400")
    #Defining the vars
    word_var=tk.StringVar()
    def inputword():
            word=entry.get()
            korean()
    #Creating a Entry Widget        
    entry= tk.Entry(english, width=40)
    entry.pack()
    #Creating the button that gets input from the Entry Widget.
    enter= tk.Button(english, text="Enter", command= inputword)
    enter.pack()

def korean():
    if word == 'hello':
        Label(english, text"안녕하세요").pack
    elif word == 'yes':
        Label(english, text"네").pack
    elif word == 'home':
        Label(english, text"음악").pack
    elif word == 'opposite':
        Label(english, text"반").pack
    elif word == 'side':
        Label(english, text"면").pack
    elif word == 'dog':
        Label(english, text"개").pack
    elif word == 'Mr':
        Label(english, text"씨").pack
        Label(english, text"It also means Mr, Ms, and Mrs").pack
    elif word == 'I':
        Label(english, text"나").pack
    elif word == 'she':
        Label(english, text"여자").pack
    elif word == 'he':
        Label(english, text"그").pack
    elif word == 'they':
        Label(english, text"그들").pack
    elif word == 'we':
        Label(english, text"나").pack
    elif word == 'go':
        Label(english, text"가요").pack
    elif word == 'come':
        Label(english, text"오요").pack
    elif word == 'have':
        Label(english, text"있요").pack
    elif word == 'be':
        Label(english, text"이요").pack
    elif word == 'eat':
        Label(english, text"먹요").pack
    elif word == 'drink':
        Label(english, text"마시요").pack
    elif word == 'give':
        Label(english, text"주요").pack
    elif word == 'see':
        Label(english, text"보요").pack
    elif word == 'sleep':
        Label(english, text"자요").pack
    elif word == 'wake up':
        Label(english, text"일어나요").pack
    elif word == 'buy':
        Label(english, text"사요").pack
    elif word == 'write':
        Label(english, text"쓰요").pack
    elif word == 'laugh':
        Label(english, text"우요").pack
    elif word == 'cry':
        Label(english, text"울요").pack
    elif word == 'wear':
        Label(english, text"입요").pack
    elif word == 'walk':
        Label(english, text"걸요").pack
    elif word == 'read':
        Label(english, text"읠요").pack
    elif word == 'learn':
        Label(english, text"배우요").pack
    elif word == 'study':
        Label(english, text"공부하요").pack
    elif word == 'meet':
        Label(english, text"만나요").pack
    elif word == 'good':
        Label(english, text"즣아요").pack
    elif word == 'bad':
        Label(english, text"나빠요").pack
    elif word == 'flu':
        Label(english, text"독감").pack
    elif word == 'death':
        Label(english, text"자망").pack
    elif word == 'no':
        Label(english, text"아니요").pack
        print("아니요")
    elif word == 'tear':
        Label(english, text"눈물").pack
        print("눈물")
    elif word == 'news':
        Label(english, text"뉴스").pack
        print("뉴스")
    elif word == 'all':
        Label(english, text"다").pack
        print("다")
    elif word == 'attend':
        Label(english, text"다니요").pack
        print("다니요")
    elif word == 'leg':
        Label(english, text"다리").pack
        print("다리")
    elif word == 'word':
        Label(english, text"단어").pack
        print("단어")
    elif word == 'close':
        Label(english, text"닫요").pack
        print("닫요")
    elif word == 'calendar':
        Label(english, text"달력").pack
        print("달력")
    else:
        Label(english, text"Opps we don't have that one, check again.").pack
