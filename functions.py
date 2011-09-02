"""
Functions of HangManGame
"""
import pickle
def goodletter(word, letter):
  """
  This function replaces the hidden letter with good ones.
  Arguments: word, letter
  Example: ---- becomes -e-- if the word is "bell" and the letter is "e"
  """
  new_word=''
  for i in word:
    if i==letter:
      new_word+=i
    else:
      new_word+="-"
  return new_word
   

def hide_it(word, hide_character):
  """
  It hides the word with a character.
  Arguments: word, character
  """
  return hide_character*len(word)
  

def merge(word1, word2, sep):
  """
  Merge two words of same lenght.
  Arguments: word1, word2, sep
  Example: merge("---e", "w---", "-") returns "w--e"
  """
  index=0
  word=''
  while index < len(word2):
    if word1[index]==sep:
      word+=word2[index]
    elif word1[index]!=sep:
      word+=word1[index]
    index+=1
  return word
    
def continue_quit(answer):
  """
  Ask to continue or not. Save feature added.
  If yes, returns True, else, return False
  """
  answer=raw_input("Do you want to continue ? yes or no : ")
  if answer[0].lower=='y':
    return True
  elif answer[0].lower=='n':
    answer=raw_input("Do you want to save ? yes or no : ")
    if answer[0].lower=='y':
      return "save"
    return False
    
def save(savefile, score):
  """
  Save the score in savefile (binary)
  """
  #TODO: -All scores in one dict
  #      -Add score to existing usernames
  #      -Create savefile
  with os.open(savefile, "wb") as savefile:
    mypickle=pickle.Pickler(savefile)
    mypickle.dump(score)