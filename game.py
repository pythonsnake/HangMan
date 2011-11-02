"""
HangManGame
"""

print "        HangManGame, by PythonSnake"
print "             0.1 Beta Version     "

#import modules
import values
import random
import functions

username=raw_input("Hi. What's your name ? ")
score=0

if functions.load(values.savefile)!=False and username in functions.load(values.savefile).keys():
    s=functions.load(values.savefile)
    score+=s[username]
    print "I remember ya ! You had {0} points !".format(s[username])

functions.menu()

print "Guess the word ! You have 8 tries only though."

answer='y'

while answer.lower()[0]=='y':
#declaring variables
    count=0
    i=random.randrange(113810)
    word_to_guess=values.words[i]

#hide the word
    print functions.hide_it(word_to_guess, "-")
    print "Left:",values.retries-count, "retries."


#GAME1
    letter=raw_input("Type a letter: ")
    word = functions.goodletter(word_to_guess, letter)
    if word=="-"*len(word_to_guess) and letter and len(letter)==1:
        count+=1
    if not letter or len(letter)>1:
        print "Invalid!"
    else:
        print word
    print "Left:",values.retries-count, "retries."


#GAME2
#TODO: Merge  GAME1 and GAME2
    while count<values.retries:
        letter=raw_input("Type a letter: ")
        word1 = functions.goodletter(word_to_guess, letter)
        word = functions.merge(word, word1, "-")
        if word1=="-"*len(word_to_guess) and letter and len(letter)==1:
            count+=1
        if not letter or len(letter)>1:
            print "Invalid!"
        else:
            print word
        print "Left:",values.retries-count, "retries."

#win/lose
        if word==word_to_guess:
            print "You win."
            score+=count
            break
    if word!=word_to_guess:
        print "You lose.\nThe word was", word_to_guess
    print "The definition of", word_to_guess, 'is:\n',functions.getDefinition(word_to_guess)

#continue/quit/save
    answer=raw_input("Do you want to continue ? yes/no: ")
    if answer[0].lower()=='n':
        saveOrNot=raw_input("Do you want to save ? yes/no: ")
        if saveOrNot[0].lower()=='y':
            score_save={username:score}
            functions.save(values.savefile, score_save)
