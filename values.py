'''
Values configuration (number of tries, words etc...)
'''

#words.txt contains the words of this game. 
with open("words.txt", "r") as words:
    words=words.read().split("\n")

#number of retries
retries=8

#savefile's name
savefile='save'
#TODO: option menu
  
