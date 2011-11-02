"""
Functions of HangManGame
"""

#importing
import pickle
import urllib
import lxml
import lxml.html
import values
import sys

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

def load(savefile):
    """
    Load a savefile
    """
    try:
        with open(savefile, 'rb') as loader:
            myUnpickle=pickle.Unpickler(loader).load()
    except:
        return False
    else:
        with open(savefile, 'rb') as loader:
            myUnpickle=pickle.Unpickler(loader)
            loaded=myUnpickle.load()
        return loaded

def save(savefile, score):
    """
    Save the score in savefile (binary)
    """
#TODO: -All scores in one dict
#      -Add score to existing usernames
#      -Create savefile       
    data=load(savefile)
    if data!=False and score.items()[0] in data:
        data[score.keys()[0]]+=score.items()[0]
    with open(savefile, "w+b") as save:
        mypickle=pickle.Pickler(save)
        mypickle.dump(score)

def getDefinition(word):
    """
    Get the definition of a file.
    Internet access required.
    Argument: word
    Source: www.anagrammer.com
    """
    source = urllib.urlopen('http://www.anagrammer.com/scrabble/{0}'.format(word)).read()
    tree = lxml.html.document_fromstring(source)
    try:
        results = tree.xpath("//span[@class='definition']")[0].text_content().capitalize()
    except IndexError:
        print "No results ?! There's a bug !"
    else:
        results = tree.xpath("//span[@class='definition']")[0].text_content().capitalize()
        return results

def menu():
    print "P - Play"
    print "O - Options"
    print "Q - Quit"
    menuChoose=raw_input("Choose: ")
    while menuChoose.lower()[0]!='p' and menuChoose.lower()[0]!='o' and menuChoose.lower()[0]!='q':  
        print 'Invalid.'
    if menuChoose.lower()[0]=='p':  
        return
    elif menuChoose.lower()[0]=='o':
        print "R - Number of retries"
        print "S - Savefile's name"
        options=raw_input('What do you want to change ? ')
        while options.lower()[0]!='r' and options.lower()[0]!='s':
            print 'Invalid.' 
        if options.lower()[0]=='r':
            new=raw_input('Enter new value: ')
            values.retries=int(new)
        elif options.lower()[0]=='s':
            new=raw_input('Enter new value: ')
            values.savefile=int(new)
    elif menuChoose.lower()[0]=='q':
        sys.exit()
        
