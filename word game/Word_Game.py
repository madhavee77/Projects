

HAND_SIZE = 10

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

SCRABBLE_LETTER_VALUES = { 'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4,
'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(word_list):
    
    return random.choice(word_list)

word_list = load_words()




def get_word_score(input_word, n):      #input_word is the word made by the user; n is letters in current hand
    
    input_word = input_word.lower()
    # calculate first component that is sum of 
    sum = 0
    for alpha in input_word:
        if alpha=='*':
            alpha_point=0
        else:
            alpha_point = SCRABBLE_LETTER_VALUES[alpha]
        sum = sum + alpha_point
        
    # calculate second component
    word_length=0
    for i in input_word:
        if i.isalpha:
            word_length= word_length+1
        else:
            word_length= word_length
                     

    p1_2c = (7 * word_length) - 3 * (n - word_length)  # part one of second component
    p2_2c = 1                                          # part two of second component

    if p1_2c > p2_2c:                           # compute score based on the part one and part two of second component
       score = p1_2c * sum
    else:
       score = p2_2c * sum

    return score



def get_frequency_dict(order):          # order is order of alphabets in an input_word
    
    freq = {}          
    
    for i in order:
        freq[i] = freq.get(i, 0) + 1       # example for "taan" o/p will be {'t':1, 'a':2, 'n':1}
   
    return freq


def display_hand(hand):           # hand as a dictionary 

    for alpha in hand.keys():
        for k in range(hand[alpha]):
             print (alpha, end = " ")              # outputs keys on same line
    print ()  

    
def deal_hand(n):

    hand = {};
    
    v_count = int((n / 3)-1)                         
    for i in range(v_count):
       a = VOWELS[random.randrange(0, len(VOWELS))]
       hand[a] = hand.get(a, 0) + 1
       
    c_count=int(2*n/3)+1
    for j in range(c_count):
        b = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[b] = hand.get(b, 0) + 1
    
    c='*'
    hand[c]=hand.get(c,0) + 1
    return hand    


def update_hand(hand, input_word):
    aa='*'
    hand_d = hand.copy()
    for alpha in input_word:
            hand_d[alpha] -= 1
    
    return hand_d    


def is_valid_word(input_word,hand,word_list):

    find_match=False    
    aa='*'
    if aa in input_word:
        for i in VOWELS:
            temp_word=input_word.replace('*',i)
            if temp_word in word_list:
                find_match=True
                break
            else:
                continue
        if find_match==True:
            return True
        else:
            return False
        
        
    else:           
        if input_word in word_list:
            return True
        else:
            return False
        
    

def wildcard(input_word, hand, word_list):
    av_hand=display_hand()
    total_score=get_word_score()
    valid_word=is_valid_word()
    print('Current Hand: '+ av_hand)

    while len(av_hand)>0:
        print('Current Hand: '+ av_hand)
        in_word=input()
        print('Enter word, or "!!" to indicate that you are finished:'+ in_word)
        if '!!' not in in_word:
             if is_valid_word(in_word,hand,word_list):
                 current_hand=update_hand(hand,in_word)
                 print('"'+in_word+'"'+' earned '+total_score+'points. Total '+total_score+'points') 
                 print('-----------------------')
                 print('Current Hand: '+ current_hand)
             else:
                 print('That is not a valid word. Please choose another word.')
                 print('-----------------------')
                 print('Current Hand: '+ current_hand)
        else:
            print('Total score: '+total_score+ ' points')
            break
        
        
        
        
def play_hand(hand):
    i=0
    display_hand(hand)
    current_hand=hand.copy()
    print('Enter word, or "!!" to indicate that you are finished:' )
    played_word= input()
    total_score=0
    while i>=0:
        if played_word != '!!':
    
            if is_valid_word(played_word,current_hand,word_list):
                word_score=get_word_score(played_word,len(current_hand))
                total_score+=word_score
                current_hand=update_hand(current_hand,played_word)
                print('"'+played_word+'"'+' earned '+str(word_score)+' points. Total: '+str(total_score)+' points') 
                print(" ")
                print('Current Hand: ',end=" ")
                display_hand(current_hand)
                i+=1
                print('Enter word, or "!!" to indicate that you are finished:',end=" " )
                played_word= input()            
            
            else:
                print('That is not a valid word. Please choose another word.')
                print(" ")
                current_hand=update_hand(current_hand,played_word)
                print('Current Hand: ',end=" ")
                display_hand(current_hand)
                print('Enter word, or "!!" to indicate that you are finished:',end=" " )
                played_word= input()
        else:
            print('Total score: '+str(total_score)+' points')
            break
    
def main():
    hand=deal_hand(HAND_SIZE)
    play_hand(hand);

main()
