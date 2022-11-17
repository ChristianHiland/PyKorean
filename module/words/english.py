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
        Label(english, text"안녕하세요").pack
        print("네")
    elif word == 'home':
        Label(english, text"안녕하세요").pack
        print("음악")
    elif word == 'opposite':
        Label(english, text"안녕하세요").pack
        print("반")
    elif word == 'side':
        Label(english, text"안녕하세요").pack
        print("면")
    elif word == 'dog':
        Label(english, text"안녕하세요").pack
        print("개")
    elif word == 'Mr':
        Label(english, text"안녕하세요").pack
        print("씨")
    elif word == 'I':
        Label(english, text"안녕하세요").pack
        print("나")
    elif word == 'she':
        Label(english, text"안녕하세요").pack
        print("여자")
    elif word == 'he':
        Label(english, text"안녕하세요").pack
        print("그")
    elif word == 'they':
        Label(english, text"안녕하세요").pack
        print("그들")
    elif word == 'we':
        Label(english, text"안녕하세요").pack
        print("나")
    elif word == 'go':
        Label(english, text"안녕하세요").pack
        print("가요")
    elif word == 'come':
        Label(english, text"안녕하세요").pack
        print("오요")
    elif word == 'have':
        Label(english, text"안녕하세요").pack
        print("있요")
    elif word == 'be':
        Label(english, text"안녕하세요").pack
        print("이요")
    elif word == 'eat':
        Label(english, text"안녕하세요").pack
        print("먹요")
    elif word == 'drink':
        Label(english, text"안녕하세요").pack
        print("마시요")
    elif word == 'give':
        Label(english, text"안녕하세요").pack
        print("주요")
    elif word == 'see':
        Label(english, text"안녕하세요").pack
        print("보요")
    elif word == 'sleep':
        Label(english, text"안녕하세요").pack
        print("자요")
    elif word == 'wake up':
        Label(english, text"안녕하세요").pack
        print("일어나요")
    elif word == 'buy':
        Label(english, text"안녕하세요").pack
        print("사요")
    elif word == 'write':
        Label(english, text"안녕하세요").pack
        print("쓰요")
    elif word == 'laugh':
        Label(english, text"안녕하세요").pack
        print("우요")
    elif word == 'cry':
        Label(english, text"안녕하세요").pack
        print("울요")
    elif word == 'wear':
        Label(english, text"안녕하세요").pack
        print("입요")
    elif word == 'walk':
        Label(english, text"안녕하세요").pack
        print("걸요")
    elif word == 'read':
        Label(english, text"안녕하세요").pack
        print("읠요")
    elif word == 'learn':
        Label(english, text"안녕하세요").pack
        print("배우요")
    elif word == 'study':
        Label(english, text"안녕하세요").pack
        print("공부하요")
    elif word == 'meet':
        Label(english, text"안녕하세요").pack
        print("만나요")
    elif word == 'good':
        Label(english, text"안녕하세요").pack
        print("즣아요")
    elif word == 'bad':
        Label(english, text"안녕하세요").pack
        print("나빠요")
    elif word == 'flu':
        Label(english, text"안녕하세요").pack
        print("독감")
    elif word == 'death':
        Label(english, text"안녕하세요").pack
        print("자망")
    elif word == 'no':
        Label(english, text"안녕하세요").pack
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
