# Hangman Game
# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()



# -------------------------------------
# Hangman Part 1: Three helper functions

def is_word_guessed(secret_word, letter_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    sw=list(secret_word)
    if set(sw)==set(letter_guessed):
        return True
    else:
        return False
    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word=""
    for x in secret_word:
        guessed_word=guessed_word+" _"
        
    for x in letters_guessed:
        index_num=[i for i, ltr in enumerate(secret_word) if ltr == x]
        nl=list(guessed_word)
        for j in index_num:
            ind=j*2
            ix=ind+1
            nl[ix]=x
        guessed_word=''.join(nl)
        
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    ava_letters=string.ascii_lowercase
    if len(letters_guessed)!=0:
        for x in letters_guessed:
            ava_letters=ava_letters.replace(x,"_")
    else:
        ava_letters=string.ascii_lowercase
        
    return ava_letters


   
    
# end of part 1
    
    
    
    
# -------------------------------------
# Hangman Part 2: The Game

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    '''


    print("Welcome to the game Hangman!")
    wordlen=len(secret_word)
    print("I am thinking of a word that is "+str(wordlen)+" letters long.")
    warnings=3
    print("You have "+str(warnings)+" warnings left.")
    guesses=6
    vowels = 'aeiou'
    letters_guessed=[]
    letter_guessed=[]
    same=[]
    
    while guesses<=6:
        print("--------------")
        print("You have "+str(guesses)+" guesses left.")
        av_let=get_available_letters(letters_guessed)
        print("Available Letters: "+av_let)
        print("Please guess a letter: ")
        x=input()
        if x.isalpha():
            user_guess=x.lower()
            
            if user_guess not in letters_guessed:
            
                 letters_guessed.append(user_guess)
                 if user_guess in secret_word:
                    letter_guessed.append(user_guess)
                    print("Good guess:"+get_guessed_word(secret_word, letters_guessed))
                    answer=is_word_guessed(secret_word,letter_guessed)
                    if answer==True:
                        score=guesses*len(letter_guessed)
                        print("--------------")
                        print("Congratulations, you won!") 
                        print("Your total score for this game is:"+str(score))
                        break

                    
                 elif user_guess in same:
                     if warnings>0:
                        warnings=warnings-1
                        print("Oops! You've already guessed that letter.")
                        print("You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))
                     else:
                        if guesses>1: 
                            print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                            guesses=guesses-1
                        else:
                            print("--------------")
                            print("Sorry, you ran out of guesses. The word was "+(secret_word))
                            break
                    
               
                 elif user_guess in vowels:
                     if guesses>2:
                       print("Oops! That letter is not in my word:")
                       guesses=guesses-2
                     else:
                        print("--------------")
                        print("Sorry, you ran out of guesses. The word was "+(secret_word))
                       
               
                        
                    
                 else:
                    if guesses>1:
                        print("Oops! That letter is not in my word:"+get_guessed_word(secret_word, letters_guessed))
                        same.append(user_guess)
                        guesses=guesses-1
                    else:
                        print("--------------")
                        print("Sorry, you ran out of guesses. The word was "+(secret_word))
                        break

                 if warnings==0:
                    if guesses>1:
                        print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                        guesses=guesses-1
                    else:
                        print("--------------")
                        print("Sorry, you ran out of guesses. The word was "+(secret_word))
                        break
                    

            elif guesses==0:
                    print("--------------")
                    print("Sorry, you ran out of guesses. The word was "+(secret_word))
                    break
                
            else:
                    if warnings>0:
                        warnings=warnings-1
                        print("Oops! You've already guessed that letter.")
                        print("You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))
                    else:
                        if guesses>1: 
                            print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                            guesses=guesses-1
                        else:
                            print("--------------")
                            print("Sorry, you ran out of guesses. The word was "+(secret_word))
                            break       


        else:
            if warnings>0:
                warnings=warnings-1
                print("Oops! That is not a valid letter.")
                print("You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))

                
            else:
                if guesses>1:   
                    print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                    guesses=guesses-1

                else:
                    print("--------------")
                    print("Sorry, you ran out of guesses. The word was"+(secret_word))
                    break
                


        
            
# -----------------------------------
# end of part 2
    
    
    
# -------------------------------------
# Hangman Part 3: The Game with Hints


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the letters_guessed length;
        False otherwise: 
    '''

    my_word = my_word.replace(' ','')
    other_word = other_word.replace(' ','')
    if (len(my_word)==len(other_word)):
        for i in range (len(my_word)):
            if my_word[i]!='_':
                if my_word[i]==other_word[i]:
                    flag=1;
                else:
                    flag=0;
                    break;
    
    else :
        flag=0;
    if (flag==1):
        return True;
    elif(flag==0):
        return False;



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''

    matchlist=[]

    for i in wordlist:
        if(match_with_gaps(my_word,i)):
            matchlist.append(i)
            
    if(len(matchlist)!=0) :
        print("Possible word matches are: ");
        print(*matchlist, sep = ", ")  
    else:
        print("No matches found");




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    '''

    
    print("Welcome to the game Hangman!")
    wordlen=len(secret_word)
    print("I am thinking of a word that is "+str(wordlen)+" letters long.")
    warnings=3
    print("You have "+str(warnings)+" warnings left.")
    guesses=6
    vowels = 'aeiou'
    letters_guessed=[]
    letter_guessed=[]
    same=[]
    
    while guesses<=6:
        print("--------------")
        print("You have "+str(guesses)+" guesses left.")
        av_let=get_available_letters(letters_guessed)
        print("Available Letters: "+av_let)
        print("Please guess a letter: ")
        x=input()
        if x.isalpha():
            user_guess=x.lower()
            
            if user_guess not in letters_guessed:
            
                 letters_guessed.append(user_guess)
                 if user_guess in secret_word:
                    letter_guessed.append(user_guess)
                    print("Good guess:"+get_guessed_word(secret_word, letters_guessed))
                    answer=is_word_guessed(secret_word,letter_guessed)
                    if answer==True:
                        score=guesses*len(letter_guessed)
                        print("--------------")
                        print("Congratulations, you won!") 
                        print("Your total score for this game is:"+str(score))
                        break

                    
                 elif user_guess in same:
                     if warnings>0:
                        warnings=warnings-1
                        print("Oops! You've already guessed that letter.")
                        print("You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))
                     else:
                        if guesses>1: 
                            print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                            guesses=guesses-1
                        else:
                            print("--------------")
                            print("Sorry, you ran out of guesses. The word was "+(secret_word))
                            break
                    
               
                 elif user_guess in vowels:
                     if guesses>2:
                       print("Oops! That letter is not in my word:")
                       guesses=guesses-2
                     else:
                        print("--------------")
                        print("Sorry, you ran out of guesses. The word was "+(secret_word))
                       
               
                        
                    
                 else:
                    if guesses>1:
                        print("Oops! That letter is not in my word:"+get_guessed_word(secret_word, letters_guessed))
                        same.append(user_guess)
                        guesses=guesses-1
                    else:
                        print("--------------")
                        print("Sorry, you ran out of guesses. The word was "+(secret_word))
                        break

                 if warnings==0:
                    if guesses>1:
                        print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                        guesses=guesses-1
                    else:
                        print("--------------")
                        print("Sorry, you ran out of guesses. The word was "+(secret_word))
                        break
                    

            elif guesses==0:
                    print("--------------")
                    print("Sorry, you ran out of guesses. The word was "+(secret_word))
                    break
                
            else:
                    if warnings>0:
                        warnings=warnings-1
                        print("Oops! You've already guessed that letter.")
                        print("You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))
                    else:
                        if guesses>1: 
                            print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                            guesses=guesses-1
                        else:
                            print("--------------")
                            print("Sorry, you ran out of guesses. The word was "+(secret_word))
                            break       

        elif (x=="*"):
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))  
        else:
            if warnings>0:
                warnings=warnings-1
                print("Oops! That is not a valid letter.")
                print("You have "+str(warnings)+" warnings left:"+get_guessed_word(secret_word, letters_guessed))

                
            else:
                if guesses>1:   
                    print("You have no warnings left so you lose one guess:"+get_guessed_word(secret_word, letters_guessed))
                    guesses=guesses-1

                else:
                    print("--------------")
                    print("Sorry, you ran out of guesses. The word was"+(secret_word))
                    break
                
    
# -----------------------------------
# end of part 3

# Main code 

# To test part 2
# uncomment the following two lines.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)


    
# To test part 3 re-comment out the above lines and 
# uncomment the following two lines. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)