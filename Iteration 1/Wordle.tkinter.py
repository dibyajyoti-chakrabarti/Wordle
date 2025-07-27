#Note: Please take care of all the path values for the txt files before executing.
#Please check if all the Buttons are working.

#HEX Colour codes used
#Green - #58B11A
#Yellow - #FFDE00
#Grey - #4B4B4B
#Red - #FF502A

from tkinter import *
import tkinter.font
from PIL import Image, ImageTk

#Home Page Graphics
home=Tk()
home.geometry("1000x670")
home.title("Home Screen")
home['bg']='black'

pyLogo = ImageTk.PhotoImage(Image.open("C:\Debbo 12A\Wordle\logo.png"))
pyLabel = Label(home, image = pyLogo)
pyLabel.image = pyLogo
pyLabel.place(x=90,y=30)

#Font
wordleFont= ("Bernard MT Condensed", 35, 'bold')
titleFont= ("Bauhaus 93", 45)
ruleFont= ("Times New Roman",17, 'bold')
enterFont= ("Times New Roman",25,'bold')
btnFont = ("Elephant",18,'bold')
backFont= ("Old English Text MT", 22, 'bold')

#Bunch of home page Labels
Label(home,text="WELCOME TO ", font= titleFont, fg="white", bg="black", anchor='n', padx=10, pady=10).place(x=540,y=50)
Label(home,text="W", fg="white", font= wordleFont, bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=570, y=150)
Label(home,text="O", fg="white", font= wordleFont, bg="#FFDE00",  anchor='n',padx=15,pady=5).place(x=635,y=150)
Label(home,text="R", fg="white", font= wordleFont, bg="#4B4B4B",  anchor='n',padx=10,pady=5).place(x=690,y=150)
Label(home,text="D", fg="white", font= wordleFont, bg="#58B11A",  anchor='n', padx=10,pady=5).place(x=740, y=150)
Label(home,text="L", fg="white", font= wordleFont, bg="#FFDE00", anchor='n',padx=15,pady=5).place(x=790,y=150)
Label(home,text="E", fg="white", font= wordleFont, bg="#4B4B4B", anchor='n',padx=10,pady=5).place(x=840,y=150)


def errorName():

    #Basic Dimensions
    error = Tk()
    error.geometry('500x400')
    error.title('Error!')
    error['bg']='black'
    
    errorMsg = '''
    It seems like you have
    not entered a name yet!

    Please enter a name before
    starting the game!'''
    Label(error,text="Alert!", fg="white", font= wordleFont, bg="#FF502A",  anchor='n',padx=15,pady=5).place(x=180, y=50)
    Label(error, text=errorMsg, bg="black", fg="white", font= ruleFont).place(x=90,y=120)
    backError=Button(error, text= "Okay", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= error.destroy, borderwidth= 10).place(x=200, y=300)


def nameList():
    name = enterName.get()

    file = open("C:\Debbo 12A\Wordle\storeName.txt",'w')
    file.write(name)
    file.close()
    
    x = open("C:\Debbo 12A\Wordle\storeName.txt",'r')
    content = x.read()
    x.close()

    if(content==''):

        errorName()
        
    else:
        nameMsg ='''Name Registered!
        Click to start game.'''

        Label(home,text=nameMsg, fg="white", font= ("Forte",30), bg="#58B11A",justify = 'left',padx=20,pady=43).place(x=490, y=300)
        #print(leaderBoard) #check progress of Leaderboard
    


#Entering and storing player name
Label(text="Enter Your Name",fg="#58B11A", bg="black",font=("Times New Roman", 30)).place(x=590,y=300)
enterName=Entry(home,fg="black", bg="white",  font=enterFont)
enterName.pack()
enterName.place(x=570,y=350)
nameBtn=Button(home, text="Enter", bg="#58B11A", fg="white", font=btnFont, command=nameList, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=670,y=400)

#Rules for the game
def rulesWordle():
    rules=Tk()
    rules['bg']='#4B4B4B'
    
    rulesContent = '''Rules:

    - You have unlimited amount of time to guess a:
    - 5 letter word in 5 guesses with the help of hints.
    - Once you get the word correct, you go to a new randomly generated word.
    - If you fail to guess a word in the 5 tries provided, you lose.


    Hints provided:

    1) If the letter is green, it means the letter is in the word and in the correct position.
    2) If the letter is yellow, it means the letter is in the word but not in the correct position.
    3) If the letter is grey, it means the the letter is not in the word.

    Best of Luck!
    '''

    rules.geometry("1100x550")
    rules.title("About Wordle")
    Label(rules,text="RULES",fg="#58B11A",bg="#4B4B4B",font=titleFont).place(x=500,y=50)
    Label(rules, text =rulesContent,fg="#FFDE00",bg="#4B4B4B",font=ruleFont, justify ='left').place(x=130,y=120)
    
    

    backRule=Button(rules, text= "Back", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, command= rules.destroy, cursor= 'hand2', borderwidth= 10).place(x=950, y=55)


#Creators 
def creatorWordle():
    creator=Tk()
    creator['bg']='#4B4B4B'

    creatorContent = '''
    This piece of software has been made by a team of 4 members. 
    Also, I can assure you that no GitHub code was used in the creation of this software.
    Source: Trust me bro.

    [Our team] : -

    1) Akshat (Coded and designed GUI; basic algorithm conversion to GUI)

    2) Aditya (Coded and designed GUI; basic algorithm conversion to GUI)

    3) Aarav (Logic Ideas and Marketing)

    4) Dibyajyoti (Coded Fundamental algorithm and finalized the project)

    '''
    creator.geometry("1100x500")
    creator.title("About Wordle")
    Label(creator,text="THE CREATORS",fg="#58B11A",bg="#4B4B4B",font=titleFont).place(x=375,y=50)
    Label(creator, text =creatorContent,fg="#FFDE00",bg="#4B4B4B",font=ruleFont,justify = 'left').place(x=150,y=120)
    backCreator=Button(creator, text= "Back", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= creator.destroy, borderwidth= 10).place(x=950, y=55)

#All about wordle and related button
def aboutWordle():
    about=Tk()
    about['bg']='#4B4B4B'
    
    aboutContent = '''
    Wordle was initially created by Welsh software engineer Josh Wardle.
    He had initially intended for only him and his partner to play the game.
    However, he made the game public in October 2021, and it went viral in December 2021. 
    His simple once-a-day game, played on a web browser, now has around 2 million daily users.
    The New York Times ended up buying the rights to the game from Wardle, 
    for an undisclosed fee greater than a million dollars!

    '''
    about.geometry("1100x350")
    about.title("About Wordle")
    Label(about,text="ABOUT WORDLE",fg="#58B11A",bg="#4B4B4B",font=titleFont).place(x=375,y=50)
    Label(about, text =aboutContent,fg="#FFDE00",bg="#4B4B4B",font=ruleFont).place(x=75,y=120)
    backAbout=Button(about, text= "Back", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= about.destroy, borderwidth= 10).place(x=950, y=55)


#All time leaderboards
def leadWordle():
    lead=Tk()
    lead['bg']='#4B4B4B'

    lead.geometry("800x600")
    lead.title("About Wordle")
    Label(lead,text="LEADERBOARD",fg="#58B11A",bg="#4B4B4B",font=titleFont).place(x=200,y=50)
    
    

    file1 = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'r')
    info1 = file1.read()
    file1.close()

    file2 = open("C:\Debbo 12A\Wordle\streakLead.txt",'r')
    info2 = file2.read()
    file2.close()

    key = info1.split('\n')
    value = info2.split('\n')

    key.pop()
    value.pop()
    #print(key)
    #print(value)

    d={}
    for i in range (len(key)):
        d[key[i]] = value[i]
    #print(d)


    sorted_values = sorted(d.values()) # Sort the values
    sorted_dict = {}

    sorted_keys = sorted(d, key=d.get)
    for w in sorted_keys:
        sorted_dict[w] = d[w]

    #print(sorted_dict)
    res = dict(reversed(list(sorted_dict.items())))

    #print(res)

    L1 = list(res.keys())
    L2 = list(res.values())

    finalKey = ''
    finalValue = ''
    for i in L1:
        finalKey = finalKey + i + '\n' +'\n'
    for i in L2:
        finalValue = finalValue + i + '\n' + '\n'

    
    x = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'w')
    x.write('')
    x.close()

    y = open("C:\Debbo 12A\Wordle\streakLead.txt",'w')
    y.write('')
    y.close()
    
    a = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'a')
    a.write(finalKey)
    a.close()

    b = open("C:\Debbo 12A\Wordle\streakLead.txt",'a')
    b.write(finalValue)
    b.close() 
    
    file1 = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'r')
    playerName = file1.read()
    file1.close()
    
    file2 = open("C:\Debbo 12A\Wordle\streakLead.txt",'r')
    streakInfo = file2.read()
    file2.close()
    
    Label(lead, text =playerName,fg="#FFDE00",bg="#4B4B4B",font=ruleFont).place(x=200,y=150)
    Label(lead, text =streakInfo,fg="#FFDE00",bg="#4B4B4B",font=ruleFont).place(x=500,y=150)
    Label(lead, text ='#1',fg="#A47616",bg="#FFCD00",font=("Brush Script MT",15,'bold'),padx=13,pady=5).place(x=145,y=195)
    Label(lead, text ='#2',fg="#767675",bg="#D8D6D0",font=("Brush Script MT",15,'bold'),padx=10,pady=5).place(x=145,y=245)
    Label(lead, text ='#3',fg="#8D2200",bg="#E17444",font=("Brush Script MT",15,'bold'),padx=10,pady=5).place(x=145,y=295)
    backLead=Button(lead, text= "Back", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= lead.destroy, borderwidth= 10).place(x=680, y=55)
    def leadReset():
        defaultName = '''[PLAYER NAME]
        '''
        defaultStreak = '''[STREAK]
        '''

        a = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'w')
        a.write(defaultName)
        a.close()

        b = open("C:\Debbo 12A\Wordle\streakLead.txt",'w')
        b.write(defaultStreak)
        b.close()

        lead.destroy()
        leadWordle()
    delLead=Button(lead, text= "Reset Leaderboard", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= leadReset, borderwidth= 10).place(x=30, y=520)

    
ruleBtn= Button(home, text ="Rules",fg="black",bg="#FFDE00",command = rulesWordle, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=100,y=310)
creatortBtn= Button(home, text ="The Creators",fg="black",bg="#FFDE00",command = creatorWordle, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=100,y=390)
aboutBtn= Button(home, text ="About the Game",fg="black",bg="#FFDE00",command = aboutWordle, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=100,y=470)
leadBtn = Button(home, text ="All Time Leaderboard",fg="black",bg="#FFDE00",command = leadWordle, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=100,y=550)

def resetWindow():
    #Basic Dimensions
    reset = Tk()
    reset.geometry('500x500')
    reset.title('Reset TXT files')
    reset['bg']='black'

    def doneScreen():
        #Basic Dimensions
        done = Tk()
        done.geometry('375x350')
        done.title('File updated')
        done['bg']='black'
        doneMsg = '''
        The file has been updated

        to default settings!'''
        Label(done,text="Task done!", fg="white", font= wordleFont, bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=80, y=50)
        Label(done, text=doneMsg, bg="black", fg="white", font= ruleFont).place(x=15,y=120)
        backDone=Button(done, text= "Okay", bg= '#58B11A', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= done.destroy, borderwidth= 10).place(x=135, y=250)
        

    def res1():

        a = open("C:\Debbo 12A\Wordle\storeName.txt",'w')
        a.write('')
        a.close()

        doneScreen()

    def res3():

        defaultName = '''[PLAYER NAME]
        '''
        
        a = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'w')
        a.write(defaultName)
        a.close()

        doneScreen()

    def res4():

        defaultStreak = '''[STREAK]
        '''

        a = open("C:\Debbo 12A\Wordle\streakLead.txt",'w')
        a.write(defaultStreak)
        a.close()

        doneScreen()

    def res2():

        a = open("C:\Debbo 12A\Wordle\winStreak.txt",'w')
        a.write('0')
        a.close()

        doneScreen()
    
    Label(reset, text="Reset your TXT files here", bg="black", fg="white", font= ("Times New Roman",30, 'bold')).place(x=40,y=20)

    resetBtn1= Button(reset, text ="RESET storeName.txt",fg="white",bg="#58B11A",command = res1, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=105,y=100)
    resetBtn2= Button(reset, text ="RESET winStreak.txt",fg="white",bg="#58B11A",command = res2, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=105,y=180)
    
    resetBtn3= Button(reset, text ="RESET storeNameLead.txt",fg="black",bg="#FFDE00",command = res3, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=75,y=260)
    resetBtn4= Button(reset, text ="RESET streakLead.txt",fg="black",bg="#FFDE00",command = res4, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=100,y=340)
    
    backStreak=Button(reset, text= "Done", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= reset.destroy, borderwidth= 10).place(x=210, y=420)


resetFile = Button(home, text ="!",fg="black",bg="#FFDE00",command = resetWindow, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=930,y=20)

def create():
    #To check if the user has entered his/her name
    file = open("C:\Debbo 12A\Wordle\storeName.txt",'r')
    name = file.read()
    file.close()

    if(name==''):

        errorName()
       
    else:
       
        import random
        index= random.randint(1,2303)
        file=open("C:\Debbo 12A\Wordle\wordBank.txt",'r')
        content=file.read()
        file.close()

        string=''
        for i in content:
            if i == ' ':
                i='\n'
            string+=i
        wordBank=string.split('\n')
        word_ = wordBank[index]

        import random
        index=random.randint(1,12974)

        file=open("C:\Debbo 12A\Wordle\guessBank.txt",'r')
        content=file.read()
        file.close()

        str1=''
        for i in content:
            str1+=i
        inter=str1.split('\n')
        guessBank=inter+wordBank

       
        #Basic Dimensions
        game = Tk()
        game.geometry('930x730')
        game.title('Game Window')
        game['bg']='black'

        def streakWordle():
            #Basic Dimensions
            streak = Tk()
            streak.geometry('500x350')
            streak.title('Streak')
            streak['bg']='black'

            a = open("C:\Debbo 12A\Wordle\winStreak.txt",'r')
            content = a.read()
            a.close()

            streakMsg = '''
            Currently on Streak Number
            
            '''+content
            Label(streak,text="Streak Number", fg="white", font= wordleFont, bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=100, y=50)
            Label(streak, text=streakMsg, bg="black", fg="white", font= ruleFont).place(x=20,y=120)

            backStreak=Button(streak, text= "Okay", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= streak.destroy, borderwidth= 10).place(x=200, y=250)
        
        streakBtn= Button(game, text ="Check Streak Number",fg="black",bg="#FFDE00",command = streakWordle, font= btnFont, cursor= 'hand2', borderwidth= 10).place(x=600,y=60)

       
        #Title
        Label(game,text="W", fg="white", font= wordleFont, bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=260, y=50)
        Label(game,text="O", fg="white", font= wordleFont, bg="#FFDE00",  anchor='n',padx=15,pady=5).place(x=325,y=50)
        Label(game,text="R", fg="white", font= wordleFont, bg="#4B4B4B",  anchor='n',padx=10,pady=5).place(x=380,y=50)
        Label(game,text="D", fg="white", font= wordleFont, bg="#58B11A",  anchor='n', padx=10,pady=5).place(x=430, y=50)
        Label(game,text="L", fg="white", font= wordleFont, bg="#FFDE00", anchor='n',padx=15,pady=5).place(x=480,y=50)
        Label(game,text="E", fg="white", font= wordleFont, bg="#4B4B4B", anchor='n',padx=10,pady=5).place(x=530,y=50)
        Label(game,text= "Enter 5 letter words",font= titleFont,bg='#4B4B4B',fg="white").place(x=130,y=150)


        #The word
        word=word_
        print(word)
        #Error Screen
        def errorScreen():
            #Basic Dimensions
            error = Tk()
            error.geometry('500x400')
            error.title('Error!')
            error['bg']='black'

            errorMsg = '''
            The guess should be  
            a valid 5 letter word!

            Please check the number of letters
            and try again!'''
            Label(error,text="Alert!", fg="white", font= wordleFont, bg="#FF502A",  anchor='n',padx=15,pady=5).place(x=180, y=50)
            Label(error, text=errorMsg, bg="black", fg="white", font= ruleFont).place(x=15,y=120)

            backError=Button(error, text= "Okay", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= error.destroy, borderwidth= 10).place(x=200, y=300)
        
        def gameOver():
            #Basic Dimensions
            over = Tk()
            over.geometry('500x450')
            over.title('Game Over!')
            over['bg']='black'

            nameInfo = open("C:\Debbo 12A\Wordle\storeName.txt",'r')
            info1 = nameInfo.read()
            nameInfo.close()
            s1 = info1 + '\n'
            file1 = open("C:\Debbo 12A\Wordle\storeNameLead.txt",'a')
            file1.write(s1)
            file1.close()
            streakInfo = open("C:\Debbo 12A\Wordle\winStreak.txt",'r')
            info2 = streakInfo.read()
            streakInfo.close()
            s2 = info2 + '\n'
            
            file2 = open("C:\Debbo 12A\Wordle\streakLead.txt",'a')
            file2.write(s2)
            file2.close()
            a = open("C:\Debbo 12A\Wordle\winStreak.txt",'w')
            a.write('0')
            a.close()

            overMsg = '''
            Must be a really 
            hard word!

            It was a good run.

            Btw the word was

            '''
            s = '['+word+']'
            Label(over,text="Game Over!", fg="white", font= wordleFont, bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=140, y=50)
           
            Label(over, text=overMsg, bg="black", fg="white", font= ruleFont).place(x=90,y=120)
            Label(over, text=s, bg="#FFDE00", fg="black", font= ruleFont).place(x=220,y=320)
            def closingGame():
                game.destroy()
                over.destroy()
            overGame=Button(over, text= "End game", bg= '#FF1B10', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= closingGame, borderwidth= 10).place(x=180, y=370)

        
        #Colour deciding code
        #def colour_set(guess,yIndex,guessNo):
        def generateColour(guess):
            

            letters_guess=[]
            for i in guess:
                letters_guess.append(i)

            letters_word=[]
            for i in word:
                letters_word.append(i)

            #Colour Selection
            green_colour_pos=[' ',' ',' ',' ',' ']
            yellowGrey_colour_pos=[' ',' ',' ',' ',' ']

            for i in range (0,5):
                if letters_guess[i]==letters_word[i]:
                    letters_word[i]='-'
                    green_colour_pos[i]='#58B11A'
    
            for i in range (0,5):
                if (letters_guess[i] in letters_word)==True:
                    letters_word[letters_word.index(letters_guess[i])]='-'
                    yellowGrey_colour_pos[i]='#FFDE00'
                else:
                    yellowGrey_colour_pos[i]='#4B4B4B'

            for i in range (0,5):
                if green_colour_pos[i]==' ':
                    green_colour_pos[i]=yellowGrey_colour_pos[i]
                
            return green_colour_pos

        def printHint(guess,yIndex):
            colour = generateColour(guess)

            #HEX Colour codes used
            #Green - #58B11A
            #Yellow - #FFDE00
            #Grey - #4B4B4B

            
            #Printing
            Label(game,text=guess[0], fg="white", font= wordleFont, bg=colour[0],  anchor='n',padx=15,pady=5).place(x=230, y=yIndex)
            Label(game,text=guess[1], fg="white", font= wordleFont, bg=colour[1],  anchor='n',padx=15,pady=5).place(x=300,y=yIndex)
            Label(game,text=guess[2], fg="white", font= wordleFont, bg=colour[2],  anchor='n',padx=10,pady=5).place(x=370,y=yIndex)
            Label(game,text=guess[3], fg="white", font= wordleFont, bg=colour[3],  anchor='n', padx=10,pady=5).place(x=440, y=yIndex)
            Label(game,text=guess[4], fg="white", font= wordleFont, bg=colour[4], anchor='n',padx=15,pady=5).place(x=510,y=yIndex)
        def nextWord():
            #Basic Dimensions
            newWord = Tk()
            newWord.geometry('450x400')
            newWord.title('You got it!')
            newWord['bg']='black'

            newMsg = '''
            You guessed the word!

            Let's try another word.

            You might get this one 
            as well!
            '''
            Label(newWord,text="You guessed it!", fg="white", font= wordleFont, bg="#58B11A",  anchor='n',padx=15,pady=5).place(x=65, y=50)
            Label(newWord, text=newMsg, bg="black", fg="white", font= ruleFont).place(x=40,y=120)
            def startNewGame():
                newWord.destroy()
                game.after(500,create)
            newGame=Button(newWord, text= "Next Word!", bg= '#58B11A', fg= '#FDEDEC', font= backFont, cursor= 'hand2', command= startNewGame, borderwidth= 10).place(x=140, y=320)

        def winCheck(guess,guessNo):
            colour = generateColour(guess)
            #Checking for win
            if ('#FFDE00' in colour)==False and ('#4B4B4B' in colour)==False:
                a = open("C:\Debbo 12A\Wordle\winStreak.txt",'r')
                content = a.read()
                a.close()

                updateContent = int(content)+1
                updateContent = str(updateContent)
                b = open("C:\Debbo 12A\Wordle\winStreak.txt",'w')
                b.write(updateContent)
                b.close()

                game.destroy()
                nextWord()
            else:
                if guessNo == 5:
                    

                    gameOver()
        
        

        def guess1():
            #Guess 1
            def returnGuess1():
                guess1 = enterGuess1.get()
                guess1 = guess1.lower()
                if len(guess1)==5 and guess1 in guessBank:
                    Label(game,text="                             ", fg="white", font= wordleFont, bg="black",  anchor='n',padx=15,pady=5).place(x=230, y=250)
                    #The word generated is ---> word
                    #The guess entered is ---> guess
                    printHint(guess1,250)
                    winCheck(guess1,1)
                else:
                    errorScreen()
            enterGuess1=Entry(game,fg="black", bg="white",  font=enterFont)
            enterGuess1.pack()
            enterGuess1.place(x=230,y=250)
            guessBtn=Button(game, text="Check 1", bg="#58B11A", fg="white", font=btnFont, command=returnGuess1, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=680,y=240)
            

        
        def guess2():
            #Guess 2
            def returnGuess2():
                guess2 = enterGuess2.get()
                guess2 = guess2.lower()
                if len(guess2)==5 and guess2 in guessBank:
                    Label(game,text="                             ", fg="white", font= wordleFont, bg="black",  anchor='n',padx=15,pady=5).place(x=230, y=350)
                    #The word generated is ---> word
                    #The guess entered is ---> guess
                    printHint(guess2,350)
                    winCheck(guess2,2)
                else:
                    errorScreen()
            enterGuess2=Entry(game,fg="black", bg="white",  font=enterFont)
            enterGuess2.pack()
            enterGuess2.place(x=230,y=350)
            guessBtn=Button(game, text="Check 2", bg="#58B11A", fg="white", font=btnFont, command=returnGuess2, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=680,y=340)

        def guess3():
            #Guess 3
            def returnGuess3():
                guess3 = enterGuess3.get()
                guess3 = guess3.lower()
                if len(guess3)==5 and guess3 in guessBank:
                    Label(game,text="                             ", fg="white", font= wordleFont, bg="black",  anchor='n',padx=15,pady=5).place(x=230, y=450)
                    #The word generated is ---> word
                    #The guess entered is ---> guess
                    printHint(guess3,450)
                    winCheck(guess3,3)
                else:
                    errorScreen()
            enterGuess3=Entry(game,fg="black", bg="white",  font=enterFont)
            enterGuess3.pack()
            enterGuess3.place(x=230,y=450)
            guessBtn=Button(game, text="Check 3", bg="#58B11A", fg="white", font=btnFont, command=returnGuess3, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=680,y=440)

        def guess4():
            #Guess 4
            def returnGuess4():
                guess4 = enterGuess4.get()
                guess4 = guess4.lower()
                if len(guess4)==5 and guess4 in guessBank:
                    Label(game,text="                             ", fg="white", font= wordleFont, bg="black",  anchor='n',padx=15,pady=5).place(x=230, y=550)
                    #The word generated is ---> word
                    #The guess entered is ---> guess
                    printHint(guess4,550)
                    winCheck(guess4,4)
                else:
                    errorScreen()
            enterGuess4=Entry(game,fg="black", bg="white",  font=enterFont)
            enterGuess4.pack()
            enterGuess4.place(x=230,y=550)
            guessBtn=Button(game, text="Check 4", bg="#58B11A", fg="white", font=btnFont, command=returnGuess4, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=680,y=540)

        def guess5():
            #Guess 5
            def returnGuess5():
                guess5 = enterGuess5.get()
                guess5 = guess5.lower()
                if len(guess5)==5 and guess5 in guessBank:
                    Label(game,text="                             ", fg="white", font= wordleFont, bg="black",  anchor='n',padx=15,pady=5).place(x=230, y=650)
                    #The word generated is ---> word
                    #The guess entered is ---> guess
                    printHint(guess5,650)
                    winCheck(guess5,5)
                else:
                    errorScreen()
            enterGuess5=Entry(game,fg="black", bg="white",  font=enterFont)
            enterGuess5.pack()
            enterGuess5.place(x=230,y=650)
            guessBtn=Button(game, text="Check 5", bg="#58B11A", fg="white", font=btnFont, command=returnGuess5, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=680,y=640)
        
        guessBtn=Button(game, text="GIVE UP", bg="#FF502A", fg="white", font=btnFont, command=gameOver, padx=20,pady=5,borderwidth= 10, cursor= 'hand2').place(x=20,y=60)

        guess1()
        guess2()
        guess3()
        guess4()
        guess5()
playBtn= Button(text="CLICK TO PLAY!",fg="white",bg="#58B11A",font=btnFont, borderwidth= 10, command= create,padx=50,pady=20, cursor= 'hand2').place(x=550,y=500)

mainloop()
