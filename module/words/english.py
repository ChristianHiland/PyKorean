# This contans the words in Korean

from tkinter import W

def korean():
    # Importing tkinter
    import tkinter as tk
    # Windows & Settings
    english= tk.Tk()
    english.geometry("600x400")
    english.title("English")
    # Actions
    def inputword():
        word = E.get()
        korean
    def back():
        english.destroy
    # Labels
    ET = tk.Label(english, text = "Words:")
    # Entry Widget
    E = tk.Entry(english)
    # Buttons
    EN = tk.Button(english, text="Enter", command= inputword)
    B = tk.Button(english, text="Back", command= back)
    # Showing the elements
    ET.pack()
    E.pack()
    EN.pack()
    B.pack()
    english.mainloop()

    if word == 'hello':
        tk.Label(english, text="hello").pack
        tk.Label(english, text="안녕하세요").pack
    elif word == 'yes':
        tk.Label(english, text="yes").pack
        tk.Label(english, text="네").pack
    elif word == 'home':
        tk.Label(english, text="home").pack
        tk.Label(english, text="음악").pack
    elif word == 'opposite':
        tk.Label(english, text="opposite").pack
        tk.Label(english, text="반").pack
    elif word == 'side':
        tk.Label(english, text="side").pack
        tk.Label(english, text="면").pack
    elif word == 'dog':
        tk.Label(english, text="dog").pack
        tk.Label(english, text="개").pack
    elif word == 'Mr':
        tk.Label(english, text="씨").pack
        tk.Label(english, text="It also means Mr, Ms, and Mrs").pack
    elif word == 'I':
        tk.Label(english, text="I").pack
        tk.Label(english, text="나").pack
    elif word == 'she':
        tk.Label(english, text="she").pack
        tk.Label(english, text="여자").pack
    elif word == 'he':
        tk.Label(english, text="he").pack
        tk.Label(english, text="그").pack
    elif word == 'they':
        tk.Label(english, text="they").pack
        tk.Label(english, text="그들").pack
    elif word == 'we':
        tk.Label(english, text="we").pack
        tk.Label(english, text="나").pack
    elif word == 'go':
        tk.Label(english, text="go").pack
        tk.Label(english, text="가요").pack
    elif word == 'come':
        tk.Label(english, text="come").pack
        tk.Label(english, text="오요").pack
    elif word == 'have':
        tk.Label(english, text="have").pack
        tk.Label(english, text="있요").pack
    elif word == 'be':
        tk.Label(english, text="be").pack
        tk.Label(english, text="이요").pack
    elif word == 'eat':
        tk.Label(english, text="eat").pack
        tk.Label(english, text="먹요").pack
    elif word == 'drink':
        tk.Label(english, text="drink").pack
        tk.Label(english, text="마시요").pack
    elif word == 'give':
        tk.Label(english, text="give").pack
        tk.Label(english, text="주요").pack
    elif word == 'see':
        tk.Label(english, text="see").pack
        tk.Label(english, text="보요").pack
    elif word == 'sleep':
        tk.Label(english, text="sleep").pack
        tk.Label(english, text="자요").pack
    elif word == 'wake up':
        tk.Label(english, text="wake up").pack
        tk.Label(english, text="일어나요").pack
    elif word == 'buy':
        tk.Label(english, text="buy").pack
        tk.Label(english, text="사요").pack
    elif word == 'write':
        tk.Label(english, text="write").pack
        tk.Label(english, text="쓰요").pack
    elif word == 'laugh':
        tk.Label(english, text="laugh").pack
        tk.Label(english, text="우요").pack
    elif word == 'cry':
        tk.Label(english, text="cry").pack
        tk.Label(english, text="울요").pack
    elif word == 'wear':
        tk.Label(english, text="wear").pack
        tk.Label(english, text="입요").pack
    elif word == 'walk':
        tk.Label(english, text="walk").pack
        tk.Label(english, text="걸요").pack
    elif word == 'read':
        tk.Label(english, text="read").pack
        tk.Label(english, text="읠요").pack
    elif word == 'learn':
        tk.Label(english, text="learn").pack
        tk.Label(english, text="배우요").pack
    elif word == 'study':
        tk.Label(english, text="study").pack
        tk.Label(english, text="공부하요").pack
    elif word == 'meet':
        tk.Label(english, text="meet").pack
        tk.Label(english, text="만나요").pack
    elif word == 'good':
        tk.Label(english, text="good").pack
        tk.Label(english, text="즣아요").pack
    elif word == 'bad':
        tk.Label(english, text="bad").pack
        tk.Label(english, text="나빠요").pack
    elif word == 'flu':
        tk.Label(english, text="flu").pack
        tk.Label(english, text="독감").pack
    elif word == 'death':
        tk.Label(english, text="death").pack
        tk.Label(english, text="자망").pack
    elif word == 'no':
        tk.Label(english, text="no").pack
        tk.Label(english, text="아니요").pack
    elif word == 'tear':
        tk.Label(english, text="tear").pack
        tk.Label(english, text="눈물").pack
    elif word == 'news':
        tk.Label(english, text="news").pack
        tk.Label(english, text="뉴스").pack
    elif word == 'all':
        tk.Label(english, text="all").pack
        tk.Label(english, text="다").pack
    elif word == 'attend':
        tk.Label(english, text="attend").pack
        tk.Label(english, text="다니요").pack
    elif word == 'leg':
        tk.Label(english, text="leg").pack
        tk.Label(english, text="다리").pack
    elif word == 'word':
        tk.Label(english, text="word").pack
        tk.Label(english, text="단어").pack
    elif word == 'close':
        tk.Label(english, text="close").pack
        tk.Label(english, text="닫요").pack
    elif word == 'calendar':
        tk.Label(english, text="calendar").pack
        tk.Label(english, text="달력").pack
    else:
        tk.Label(english, text="Opps we don't have that one, check again.").pack
