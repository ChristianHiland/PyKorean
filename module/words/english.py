# This contans the words in Korean

# Importing tkinter
import tkinter as tk

def koreantk():
    
    # Windows & Settings
    english= Tk
    english.geometry("600X400")
    english.title("English")
    
    # Actions
    def inputword():
        words = Tkinter_variable(english, value = E.get())
        korean()
    def back():
        english.destroy
        
    # Labels
    ET = Label(master, text = "Words:")
    
    # Grids
    ET.grid(row = 0, column = 0, sticky = W, pady = 2)
    B.grid(row = 2, column = 2, sticky = E)
    
    # Entry Widget
    E = tk.Entry(english)
    E.grid(row = 0, column = 1, pady = 2)
    
    # Buttons
    EN = tk.Button(english, text="Enter", command= inputword)
    B = tk.Button(english, text="Back", command= back)
    
    # Showing the elements
    ET.pack()
    E.pack()
    EN.pack()
    B.pack()
    english.mainloop()
    
def korean():
    
    if word == 'hello':
        Label(english, text"hello").pack
        Label(english, text"안녕하세요").pack
    elif word == 'yes':
        Label(english, text"yes").pack
        Label(english, text"네").pack
    elif word == 'home':
        Label(english, text"home").pack
        Label(english, text"음악").pack
    elif word == 'opposite':
        Label(english, text"opposite").pack
        Label(english, text"반").pack
    elif word == 'side':
        Label(english, text"side").pack
        Label(english, text"면").pack
    elif word == 'dog':
        Label(english, text"dog").pack
        Label(english, text"개").pack
    elif word == 'Mr':
        Label(english, text"씨").pack
        Label(english, text"It also means Mr, Ms, and Mrs").pack
    elif word == 'I':
        Label(english, text"I").pack
        Label(english, text"나").pack
    elif word == 'she':
        Label(english, text"she").pack
        Label(english, text"여자").pack
    elif word == 'he':
        Label(english, text"he").pack
        Label(english, text"그").pack
    elif word == 'they':
        Label(english, text"they").pack
        Label(english, text"그들").pack
    elif word == 'we':
        Label(english, text"we").pack
        Label(english, text"나").pack
    elif word == 'go':
        Label(english, text"go").pack
        Label(english, text"가요").pack
    elif word == 'come':
        Label(english, text"come").pack
        Label(english, text"오요").pack
    elif word == 'have':
        Label(english, text"have").pack
        Label(english, text"있요").pack
    elif word == 'be':
        Label(english, text"be").pack
        Label(english, text"이요").pack
    elif word == 'eat':
        Label(english, text"eat").pack
        Label(english, text"먹요").pack
    elif word == 'drink':
        Label(english, text"drink").pack
        Label(english, text"마시요").pack
    elif word == 'give':
        Label(english, text"give").pack
        Label(english, text"주요").pack
    elif word == 'see':
        Label(english, text"see").pack
        Label(english, text"보요").pack
    elif word == 'sleep':
        Label(english, text"sleep").pack
        Label(english, text"자요").pack
    elif word == 'wake up':
        Label(english, text"wake up").pack
        Label(english, text"일어나요").pack
    elif word == 'buy':
        Label(english, text"buy").pack
        Label(english, text"사요").pack
    elif word == 'write':
        Label(english, text"write").pack
        Label(english, text"쓰요").pack
    elif word == 'laugh':
        Label(english, text"laugh").pack
        Label(english, text"우요").pack
    elif word == 'cry':
        Label(english, text"cry").pack
        Label(english, text"울요").pack
    elif word == 'wear':
        Label(english, text"wear").pack
        Label(english, text"입요").pack
    elif word == 'walk':
        Label(english, text"walk").pack
        Label(english, text"걸요").pack
    elif word == 'read':
        Label(english, text"read").pack
        Label(english, text"읠요").pack
    elif word == 'learn':
        Label(english, text"learn").pack
        Label(english, text"배우요").pack
    elif word == 'study':
        Label(english, text"study").pack
        Label(english, text"공부하요").pack
    elif word == 'meet':
        Label(english, text"meet").pack
        Label(english, text"만나요").pack
    elif word == 'good':
        Label(english, text"good").pack
        Label(english, text"즣아요").pack
    elif word == 'bad':
        Label(english, text"bad").pack
        Label(english, text"나빠요").pack
    elif word == 'flu':
        Label(english, text"flu").pack
        Label(english, text"독감").pack
    elif word == 'death':
        Label(english, text"death").pack
        Label(english, text"자망").pack
    elif word == 'no':
        Label(english, text"no").pack
        Label(english, text"아니요").pack
    elif word == 'tear':
        Label(english, text"tear").pack
        Label(english, text"눈물").pack
    elif word == 'news':
        Label(english, text"news").pack
        Label(english, text"뉴스").pack
    elif word == 'all':
        Label(english, text"all").pack
        Label(english, text"다").pack
    elif word == 'attend':
        Label(english, text"attend").pack
        Label(english, text"다니요").pack
    elif word == 'leg':
        Label(english, text"leg").pack
        Label(english, text"다리").pack
    elif word == 'word':
        Label(english, text"word").pack
        Label(english, text"단어").pack
    elif word == 'close':
        Label(english, text"close").pack
        Label(english, text"닫요").pack
    elif word == 'calendar':
        Label(english, text"calendar").pack
        Label(english, text"달력").pack
    else:
        Label(english, text"Opps we don't have that one, check again.").pack
