word=" "
guess=" "

def get_word():
    #pip install random-word
    from random_word import RandomWords
    print("Please wait while the code makes a random 5 letter word for you!")
    print("\n")
    ct=1
    while True:
        random_words = RandomWords()
        word_=random_words.get_random_word()
        if word_ == None:
            continue
        print("Calculating... ",(ct))
        word_=word_.lower()
        ct=ct+1
        if (len(word_))==5:
            if word_[4]!='s':
                break
    word=word_
    return word
   

def guess_word():
    print("Guess a 5 letter word: ")
    while True:
        guess_=input()
        if len(guess_)==5:
            break
        print("It has to be 5 letters long! Try again:       ")
    guess_=guess_.lower()
    guess=guess_
    return guess


def colour_set():
    word=get_word()

    print('\n')
    print('\n')

    win_check=-1
    for i in range (0,5):
        print("Guess  #",(i+1))
        
        guess=guess_word()
    
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
                green_colour_pos[i]='Green'
   
        for i in range (0,5):
            if (letters_guess[i] in letters_word)==True:
                letters_word[letters_word.index(letters_guess[i])]='-'
                yellowGrey_colour_pos[i]='Yellow'
            else:
                yellowGrey_colour_pos[i]='Grey'

        for i in range (0,5):
            if green_colour_pos[i]==' ':
                green_colour_pos[i]=yellowGrey_colour_pos[i]

    
        print(green_colour_pos)
        print('\n')
        print('---------------')

        if ('Yellow' in green_colour_pos)==False and ('Grey' in green_colour_pos)==False:
            win_check=1
            break
        else:
            win_check=0

    if win_check==0:
        print("The word was --->  ",word)
    if win_check==1:
        print("Congratulations! You guessed the correct word!")
    
colour_set()
