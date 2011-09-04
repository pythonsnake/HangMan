"""
HangManGame
"""

print "        HangManGame, by PythonSnake"
print "                Pre-Alpha Version"

#import modules
import values
import random
import functions
username=raw_input("Hi. What's your name ? ")
print "Guess the word ! You have 8 tries only though."

answer=True
score=0
while answer:
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
  print "The definition of", word_to_guess, ' is:\n',functions.getDefinition(word_to_guess)
  functions.continue_quit(answer)
if answer=='save':
  score_save={username:score}
  functions.save(savefile, score_save)
#continue/quit

