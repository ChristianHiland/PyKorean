from files import homeh

def korean():
    
    # Importing tkinter
    import tkinter as tk
    
    # Windows & Settings
    english= tk.Tk()
    english.geometry("400x600")
    english.title("English")
    
    # Actions
    def inputword():
        word = E.get()
        def koreanw():
            if word == 'hello':
                tk.Label(english, text="hello").pack()
                tk.Label(english, text="안녕하세요").pack()
            elif word == 'yes':
                tk.Label(english, text="yes").pack()
                tk.Label(english, text="네").pack()
            elif word == 'home':
                tk.Label(english, text="home").pack()
                tk.Label(english, text="음악").pack()
            elif word == 'opposite':
                tk.Label(english, text="opposite").pack()
                tk.Label(english, text="반").pack()
            elif word == 'side':
                tk.Label(english, text="side").pack()
                tk.Label(english, text="면").pack()
            elif word == 'Mr':
                tk.Label(english, text="씨").pack()
                tk.Label(english, text="It also means Mr, Ms, and Mrs").pack()
            elif word == 'I':
                tk.Label(english, text="I").pack()
                tk.Label(english, text="나").pack()
            elif word == 'she':
                tk.Label(english, text="she").pack()
                tk.Label(english, text="여자").pack()
            elif word == 'he':
                tk.Label(english, text="he").pack()
                tk.Label(english, text="그").pack()
            elif word == 'they':
                tk.Label(english, text="they").pack()
                tk.Label(english, text="그들").pack()
            elif word == 'we':
                tk.Label(english, text="we").pack()
                tk.Label(english, text="나").pack()
            elif word == 'go':
                tk.Label(english, text="go").pack()
                tk.Label(english, text="가요").pack()
            elif word == 'come':
                tk.Label(english, text="come").pack()
                tk.Label(english, text="오요").pack()
            elif word == 'be':
                tk.Label(english, text="be").pack()
                tk.Label(english, text="이요").pack()
            elif word == 'eat':
                tk.Label(english, text="eat").pack()
                tk.Label(english, text="먹요").pack()
            elif word == 'drink':
                tk.Label(english, text="drink").pack()
                tk.Label(english, text="마시요").pack()
            elif word == 'give':
                tk.Label(english, text="give").pack()
                tk.Label(english, text="주요").pack()
            elif word == 'see':
                tk.Label(english, text="see").pack()
                tk.Label(english, text="보요").pack()
            elif word == 'sleep':
                tk.Label(english, text="sleep").pack()
                tk.Label(english, text="자요").pack()
            elif word == 'wake up':
                tk.Label(english, text="wake up").pack()
                tk.Label(english, text="일어나요").pack()
            elif word == 'buy':
                tk.Label(english, text="buy").pack()
                tk.Label(english, text="사요").pack()
            elif word == 'write':
                tk.Label(english, text="write").pack()
                tk.Label(english, text="쓰요").pack()
            elif word == 'laugh':
                tk.Label(english, text="laugh").pack()
                tk.Label(english, text="우요").pack()
            elif word == 'cry':
                tk.Label(english, text="cry").pack()
                tk.Label(english, text="울요").pack()
            elif word == 'wear':
                tk.Label(english, text="wear").pack()
                tk.Label(english, text="입요").pack()
            elif word == 'walk':
                tk.Label(english, text="walk").pack()
                tk.Label(english, text="걸요").pack()
            elif word == 'read':
                tk.Label(english, text="read").pack()
                tk.Label(english, text="읠요").pack()
            elif word == 'learn':
                tk.Label(english, text="learn").pack()
                tk.Label(english, text="배우요").pack()
            elif word == 'study':
                tk.Label(english, text="study").pack()
                tk.Label(english, text="공부하요").pack()
            elif word == 'meet':
                tk.Label(english, text="meet").pack()
                tk.Label(english, text="만나요").pack()
            elif word == 'good':
                tk.Label(english, text="good").pack()
                tk.Label(english, text="즣아요").pack()
            elif word == 'bad':
                tk.Label(english, text="bad").pack()
                tk.Label(english, text="나빠요").pack()
            elif word == 'flu':
                tk.Label(english, text="flu").pack()
                tk.Label(english, text="독감").pack()
            elif word == 'death':
                tk.Label(english, text="death").pack()
                tk.Label(english, text="자망").pack()
            elif word == 'no':
                tk.Label(english, text="no").pack()
                tk.Label(english, text="아니요").pack()
            elif word == 'tear':
                tk.Label(english, text="tear").pack()
                tk.Label(english, text="눈물").pack()
            elif word == 'news':
                tk.Label(english, text="news").pack()
                tk.Label(english, text="뉴스").pack()
            elif word == 'all':
                tk.Label(english, text="all").pack()
                tk.Label(english, text="다").pack()
            elif word == 'attend':
                tk.Label(english, text="attend").pack()
                tk.Label(english, text="다니요").pack()
            elif word == 'leg':
                tk.Label(english, text="leg").pack()
                tk.Label(english, text="다리").pack()
            elif word == 'word':
                tk.Label(english, text="word").pack()
                tk.Label(english, text="단어").pack()
            elif word == 'close':
                tk.Label(english, text="close").pack()
                tk.Label(english, text="닫요").pack()
            elif word == 'calendar':
                tk.Label(english, text="calendar").pack()
                tk.Label(english, text="달력").pack()
            elif word == 'how are you?':
                tk.Label(english, text="How are you?").pack()
                tk.Label(english, text="안녕하십니까?").pack()
            elif word == 'how':
                tk.Label(english, text="how").pack()
                tk.Label(english, text="어떻게").pack()
            elif word == 'academic':
                tk.Label(english, text="academic").pack()
                tk.Label(english, text="교수").pack()
            elif word == 'boundary':
                tk.Label(english, text="boundary").pack()
                tk.Label(english, text="교수").pack()
            elif word == 'borrow':
                tk.Label(english, text="borrow").pack()
                tk.Label(english, text="빌리다").pack()
            elif word == 'character':
                tk.Label(english, text="character").pack()
                tk.Label(english, text="성격").pack()
            elif word == 'typical':
                tk.Label(english, text="typical").pack()
                tk.Label(english, text="전형적인").pack()
            elif word == 'take':
                tk.Label(english, text="take").pack()
                tk.Label(english, text="테이크").pack()
            elif word == 'absence':
                tk.Label(english, text="absence").pack()
                tk.Label(english, text="결근").pack()
            elif word == 'lack':
                tk.Label(english, text="lack").pack()
                tk.Label(english, text="이 없다").pack()
            elif word == 'embrace':
                tk.Label(english, text="embrace").pack()
                tk.Label(english, text="포옹하다").pack()
            elif word == 'accept':
                tk.Label(english, text="").pack()
                tk.Label(english, text="동의하기").pack()
            elif word == 'foreign':
                tk.Label(english, text="foreign").pack()
                tk.Label(english, text="외국의").pack()
            elif word == 'highlight':
                tk.Label(english, text="highlight").pack()
                tk.Label(english, text="가장 밝은 부분").pack()
            elif word == 'language':
                tk.Label(english, text="language").pack()
                tk.Label(english, text="언어").pack()
            elif word == 'knowledge':
                tk.Label(english, text="knowledge").pack()
                tk.Label(english, text="지식").pack()
            elif word == 'ask':
                tk.Label(english, text="ask").pack()
                tk.Label(english, text="물어보기").pack()
            elif word == 'away':
                tk.Label(english, text="away").pack()
                tk.Label(english, text="떨어져 있는").pack()
            elif word == 'air':
                tk.Label(english, text="air").pack()
                tk.Label(english, text="공기").pack()
            elif word == 'at':
                tk.Label(english, text="at").pack()
                tk.Label(english, text="~에").pack()
            elif word == 'alone':
                tk.Label(english, text="alone").pack()
                tk.Label(english, text="홀로").pack()
            elif word == 'back':
                tk.Label(english, text="back").pack()
                tk.Label(english, text="뒤").pack()
            elif word == 'child':
                tk.Label(english, text="child").pack()
                tk.Label(english, text="어린이").pack()
            elif word == 'country':
                tk.Label(english, text="country").pack()
                tk.Label(english, text="국가").pack()
            elif word == 'cold':
                tk.Label(english, text="cold").pack()
                tk.Label(english, text="추운").pack()
            elif word == 'day':
                tk.Label(english, text="day").pack()
                tk.Label(english, text="낮").pack()
            elif word == 'gas':
                tk.Label(english, text="gas").pack()
                tk.Label(english, text="가스").pack()
            elif word == 'one':
                tk.Label(english, text="one").pack()
                tk.Label(english, text="하나").pack()
            elif word == 'two':
                tk.Label(english, text="two").pack()
                tk.Label(english, text="둘").pack()
            elif word == 'three':
                tk.Label(english, text="three").pack()
                tk.Label(english, text="셋").pack()
            elif word == 'four':
                tk.Label(english, text="four").pack()
                tk.Label(english, text="넷").pack()
            elif word == 'five':
                tk.Label(english, text="five").pack()
                tk.Label(english, text="다섯").pack()
            elif word == 'six':
                tk.Label(english, text="six").pack()
                tk.Label(english, text="여섯").pack()
            elif word == 'seven':
                tk.Label(english, text="seven").pack()
                tk.Label(english, text="일곱").pack()
            elif word == 'eight':
                tk.Label(english, text="eight").pack()
                tk.Label(english, text="여덟").pack()
            elif word == 'nine':
                tk.Label(english, text="nine").pack()
                tk.Label(english, text="아홉").pack()
            elif word == 'ten':
                tk.Label(english, text="ten").pack()
                tk.Label(english, text="십").pack()
            elif word == 'how':
                tk.Label(english, text="how").pack()
                tk.Label(english, text="어떻게").pack()
            
            # Place
            elif word == 'store':
                tk.Label(english, text="store").pack()
                tk.Label(english, text="가게").pack()

            # Animals
            elif word == 'cat':
                tk.Label(english, text="cat").pack()
                tk.Label(english, text="고양이").pack()
            elif word == 'dog':
                tk.Label(english, text="dog").pack()
                tk.Label(english, text="개").pack()
            elif word == 'fish':
                tk.Label(english, text="fish").pack()
                tk.Label(english, text="생선").pack()
            
            # Type of people
            elif word == 'german':
                tk.Label(english, text="German").pack()
                tk.Label(english, text="독일 사람").pack()
            elif word == 'person':
                tk.Label(english, text="person").pack()
                tk.Label(english, text="사람").pack()
            
            # Others
            elif word == 'many':
                tk.Label(english, text="many").pack()
                tk.Label(english, text="많은").pack()

            # Nouns
            elif word == 'time':
                tk.Label(english, text="time").pack()
                tk.Label(english, text="시각").pack()
            elif word == 'times':
                tk.Label(english, text="times").pack()
                tk.Label(english, text="타임스").pack()
            elif word == 'fun':
                tk.Label(english, text="fun").pack()
                tk.Label(english, text="재미있는").pack()
            elif word == 'function':
                tk.Label(english, text="function").pack()
                tk.Label(english, text="기능").pack()
            elif word == 'channel':
                tk.Label(english, text="channel").pack()
                tk.Label(english, text="채널").pack()

            
            
            # Verbs
            elif word == 'have':
                tk.Label(english, text="have").pack()
                tk.Label(english, text="가지다").pack()
            elif word == 'tell':
                tk.Label(english, text="tell").pack()
                tk.Label(english, text="말하다").pack()
            elif word == 'go to':
                tk.Label(english, text="go to").pack()
                tk.Label(english, text="이동").pack()
            elif word == 'tired':
                tk.Label(english, text="tired").pack()
                tk.Label(english, text="피곤한").pack()
            elif word == 'sleepy':
                tk.Label(english, text="sleepy").pack()
                tk.Label(english, text="졸린").pack()
            elif word == 'feel':
                tk.Label(english, text="feel").pack()
                tk.Label(english, text="느끼다").pack()
            elif word == 'stop':
                tk.Label(english, text="stop").pack()
                tk.Label(english, text="멈추다").pack()

            # Preposition
            elif word == 'to':
                tk.Label(english, text="to").pack()
                tk.Label(english, text="에게").pack()
            
            # Pronoun
            elif word == 'you':
                tk.Label(english, text="you").pack()
                tk.Label(english, text="너").pack()
            
            else:
                tk.Label(english, text="Opps we don't have that one, check again.").pack()
        koreanw()
    def back():
        english.destroy()
        homeh.home()
    # Labels
    ET = tk.Label(english, text = "Words:")
    
    # Entry Widget
    E = tk.Entry(english)
    
    # Buttons
    EN = tk.Button(english, text="Enter", command= inputword)
    B = tk.Button(english, text="Back", command=back)
    Q = tk.Button(english, text="Quit", command=english.quit)
    
    # Showing the elements
    ET.pack()
    E.pack()
    EN.place(x=300, y=15)
    B.place(x=200, y=500)
    Q.place(x=140, y=500)
    english.mainloop()
