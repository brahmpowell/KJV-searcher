# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:56:52 2015

@author: Tommy
"""


import collections
import numpy as np
import os
from timeit import default_timer as tc

old_dir = os.getcwd()
end_of_parent_dir = old_dir.index('Concordance')
parent_dir = old_dir[:end_of_parent_dir]
dir_to_book_arrays = parent_dir + 'Concordance_V1//Book_arrays'

os.chdir(dir_to_book_arrays)

# NOTE:  Bible books are in Bible like:
#    Bible = {'Book':[{'v#':[each_word_string]}]}
#    Bible = {'Genesis':Book, 'Exodus':Book2, ...}
#        Book = [{},{},{}]
# search them by going:
#    Bible['BookName'][chapter#-1][verse#]
Book_names = ['Genesis',
'Exodus',
'Leviticus',
'Numbers',
'Deuteronomy',
'Joshua',
'Judges',
'Ruth',
'I_Samuel',
'II_Samuel',
'I_Kings',
'II_Kings',
'I_Chronicles',
'II_Chronicles',
'Ezra',
'Nehemiah',
'Esther',
'Job',
'Psalms',
'Proverbs',
'Ecclesiastes',
'Song_of_Solomon',
'Isaiah',
'Jeremiah',
'Lamentations',
'Ezekiel',
'Daniel',
'Hosea',
'Joel',
'Amos',
'Obadiah',
'Jonah',
'Micah',
'Nahum',
'Habakkuk',
'Zephaniah',
'Haggai',
'Zechariah',
'Malachi',
'Matthew',
'Mark',
'Luke',
'John',
'Acts',
'Romans',
'I_Corinthians',
'II_Corinthians',
'Galatians',
'Ephesians',
'Philippians',
'Colossians',
'I_Thessalonians',
'II_Thessalonians',
'I_Timothy',
'II_Timothy',
'Titus',
'Philemon',
'Hebrews',
'James',
'I_Peter',
'II_Peter',
'I_John',
'II_John',
'III_John',
'Jude',
'Revelation']

Bible = {}
Bible['Genesis'] = np.load('Genesis_V1.npy')
Bible['Exodus'] = np.load('Exodus_V1.npy')
Bible['Leviticus'] = np.load('Leviticus_V1.npy')
Bible['Numbers'] = np.load('Numbers_V1.npy')
Bible['Deuteronomy'] = np.load('Deuteronomy_V1.npy')
Bible['Joshua'] = np.load('Joshua_V1.npy')
Bible['Judges'] = np.load('Judges_V1.npy')
Bible['Ruth'] = np.load('Ruth_V1.npy')
Bible['I_Samuel'] = np.load('I_Samuel_V1.npy')
Bible['II_Samuel'] = np.load('II_Samuel_V1.npy')
Bible['I_Kings'] = np.load('I_Kings_V1.npy')
Bible['II_Kings'] = np.load('II_Kings_V1.npy')
Bible['I_Chronicles'] = np.load('I_Chronicles_V1.npy')
Bible['II_Chronicles'] = np.load('II_Chronicles_V1.npy')
Bible['Ezra'] = np.load('Ezra_V1.npy')
Bible['Nehemiah'] = np.load('Nehemiah_V1.npy')
Bible['Esther'] = np.load('Esther_V1.npy')
Bible['Job'] = np.load('Job_V1.npy')
Bible['Psalms'] = np.load('Psalms_V1.npy')
Bible['Proverbs'] = np.load('Proverbs_V1.npy')
Bible['Ecclesiastes'] = np.load('Ecclesiastes_V1.npy')
Bible['Song_of_Solomon'] = np.load('Song_of_Solomon_V1.npy')
Bible['Isaiah'] = np.load('Isaiah_V1.npy')
Bible['Jeremiah'] = np.load('Jeremiah_V1.npy')
Bible['Lamentations'] = np.load('Lamentations_V1.npy')
Bible['Ezekiel'] = np.load('Ezekiel_V1.npy')
Bible['Daniel'] = np.load('Daniel_V1.npy')
Bible['Hosea'] = np.load('Hosea_V1.npy')
Bible['Joel'] = np.load('Joel_V1.npy')
Bible['Amos'] = np.load('Amos_V1.npy')
Bible['Obadiah'] = np.load('Obadiah_V1.npy')
Bible['Jonah'] = np.load('Jonah_V1.npy')
Bible['Micah'] = np.load('Micah_V1.npy')
Bible['Nahum'] = np.load('Nahum_V1.npy')
Bible['Habakkuk'] = np.load('Habakkuk_V1.npy')
Bible['Zephaniah'] = np.load('Zephaniah_V1.npy')
Bible['Haggai'] = np.load('Haggai_V1.npy')
Bible['Zechariah'] = np.load('Zechariah_V1.npy')
Bible['Malachi'] = np.load('Malachi_V1.npy')
Bible['Matthew'] = np.load('Matthew_V1.npy')
Bible['Mark'] = np.load('Mark_V1.npy')
Bible['Luke'] = np.load('Luke_V1.npy')
Bible['John'] = np.load('John_V1.npy')
Bible['Acts'] = np.load('Acts_V1.npy')
Bible['Romans'] = np.load('Romans_V1.npy')
Bible['I_Corinthians'] = np.load('I_Corinthians_V1.npy')
Bible['II_Corinthians'] = np.load('II_Corinthians_V1.npy')
Bible['Galatians'] = np.load('Galatians_V1.npy')
Bible['Ephesians'] = np.load('Ephesians_V1.npy')
Bible['Philippians'] = np.load('Philippians_V1.npy')
Bible['Colossians'] = np.load('Colossians_V1.npy')
Bible['I_Thessalonians'] = np.load('I_Thessalonians_V1.npy')
Bible['II_Thessalonians'] = np.load('II_Thessalonians_V1.npy')
Bible['I_Timothy'] = np.load('I_Timothy_V1.npy')
Bible['II_Timothy'] = np.load('II_Timothy_V1.npy')
Bible['Titus'] = np.load('Titus_V1.npy')
Bible['Philemon'] = np.load('Philemon_V1.npy')
Bible['Hebrews'] = np.load('Hebrews_V1.npy')
Bible['James'] = np.load('James_V1.npy')
Bible['I_Peter'] = np.load('I_Peter_V1.npy')
Bible['II_Peter'] = np.load('II_Peter_V1.npy')
Bible['I_John'] = np.load('I_John_V1.npy')
Bible['II_John'] = np.load('II_John_V1.npy')
Bible['III_John'] = np.load('III_John_V1.npy')
Bible['Jude'] = np.load('Jude_V1.npy')
Bible['Revelation'] = np.load('Revelation_V1.npy')



def findW(words,casesensitive=False,context=False):
    """
    Used to locate instances of words in the Bible.
    input words must be a single string, with words separated by spaces.
    """
    t0 = tc()
    
    # unpack string for individual words
    word_array = ['']
    for element in words:
        # separate words by where spaces are
        if element == ' ':
            word_array.append('')
        else:
            word_array[-1] += element
            
    
    # analyze words if upper/lowercase does not matter
    if casesensitive == False:
        # redefine 'words'
        words = []
        Words = []
        for word_index in range(len(word_array)):
            UppercaseLetter = word_array[word_index][0].upper()
            LowercaseLetter = word_array[word_index][0].lower()
            RestOfWord = word_array[word_index][1:]
            # create uppercase word
            Word = UppercaseLetter + RestOfWord
            Words.append(Word)
            # create lowercase word
            word = LowercaseLetter + RestOfWord
            words.append(word)
        #print(words)
        #print(Words)
    else:
        words = word_array
        #print(words)
            

    verses_containing_words = 0
    verses_containing_extra_words = 0
    occurrences = 0
    
    # go through books of the Bible
    for book_name in Book_names:
        Book = Bible[book_name]
        
        # go through each chapter
        for chapter_index in range(len(Book)):
            chapter_number = chapter_index + 1
            Chapter = Book[chapter_index]
            
            # go through each verse
            for verse_name,Verse in Chapter.items():

                # check to see if each word is in the verse
                word_index = 0
                contains = True
                contains_added = True
                while contains == True and word_index < len(words):
                    
                    # If upper/lowercase is unimportant...
                    if casesensitive == False:
                        word = words[word_index]
                        Word = Words[word_index]
                        # Is word in verse? (also check non-original tongues)
                        if word not in Verse and Word not in Verse and '[%s]'%word not in Verse and '[%s]'%Word not in Verse:
                            contains = False
                            
                    # If upper/lowercase is important...
                    elif casesensitive == True:
                        word = words[word_index]
                        # Is word in verse? (also check non-original tongues)
                        if word not in Verse and '[%s]'%word not in Verse:
                            contains = False
                            
                    word_index += 1
                
                if contains == True:
                    verses_containing_words += 1
                    total_verse = verse_writeout(Verse)
                    print(book_name,chapter_number,':',verse_name)
                    print('    ',total_verse)
    tf = tc()
    print(tf-t0)               
    print('number of verses containing specified words: ',verses_containing_words)




def ref_and_verse(Book, Chapter, Verse, printing=True, saveit=False, ref_str=False):
    
    """
    Returns the verse as a string, and the reference as either a string or a 
    set of values.
    """
    
    # write out verse
    the_verse = verse(Book, Chapter, Verse, printing=False, saveit=True)
    
    
    #ref = 


def v(Book_Chapter_Verses,printing=True,saveit=False):
    """
    Used to simplify process of selecting verse or verses
    """
    if ',' in Book_Chapter_Verses:
        verses(Book_Chapter_Verses)
    else:
        verse(Book_Chapter_Verses,printing=True,saveit=False)
        
        
    
def verse(Book_Chapter_Verse,printing=True,saveit=False):
    
    """
    Convert (Book_Chapter_Verse) to format that Python understands for 
    finding the verse.
    
    Book_Chapter_Verse must be entered as a string (it must be within quotation marks).
    Like this: "John 3:16"
    
    Returns a continuous string.
    """
    
    # check each element until whitespace is reached to determine book name
    index = 0
    element = Book_Chapter_Verse[index]
    while element != ' ':
        index += 1
        element = Book_Chapter_Verse[index]
    
    # extract book name
    Book = Book_Chapter_Verse[0:index]
    
    index += 1
    beginningOfReferenceIndex = index
    element = Book_Chapter_Verse[index]
    # find chapter and verse
    while element != ':':
        index += 1
        element = Book_Chapter_Verse[index]
    
    # extract chapter and verse number
    Chapter = int(Book_Chapter_Verse[beginningOfReferenceIndex:index])
    Verse = int(Book_Chapter_Verse[index+1:])
       
    # try to get the verse
    try:
        # identify the verse
        the_verse_array = Bible[Book][Chapter-1][Verse]
        # convert the verse to a continuous string
        the_verse = verse_writeout(the_verse_array)
    
        # print the verse in the command window?
        if printing == True:
            print(the_verse)
        
        # save the_verse?
        if saveit == True:
            return the_verse
    except KeyError:
            print('-!-!-!-!- This verse does not exist, unless there is a bug somewhere.  Please try again.')
    


def verses(Book_Chapter_Verses):
    """
    return multiple verses in a row.
    input as 'BookName Chapter:Begin,End'
    """
    
    # check each element until ':' is reached to determine book name
    index = 0
    element = Book_Chapter_Verses[index]
    while element != ':':
        index += 1
        element = Book_Chapter_Verses[index]
    
    # extract book name
    Book_Chapter = Book_Chapter_Verses[0:index]
    
    # check each element until ',' is reached to determine 1st verse 
    indexB = index + 1
    element = Book_Chapter_Verses[indexB]
    while element != ',':
        indexB += 1
        element = Book_Chapter_Verses[indexB]
    
    # extract first verse
    Begin = Book_Chapter_Verses[index+1:indexB]
    BeginNumber = int(Begin)
    
    # extract last verse
    End = Book_Chapter_Verses[indexB+1:]
    EndNumber = int(End) + 1
    
    # print the verses
    for i in range(BeginNumber,EndNumber):
        print('    (' + Book_Chapter + ':%d)'%i)
        verse(Book_Chapter + ':%d'%i)

    
    
def verse_writeout(Verse):
    # write out verse as continuous string
    total_verse = ''
    for element in Verse:
        if element is ',' or element is '.' or element is ':' or element is ';' or element is '?' or element is '!':
            total_verse += element
        else:
            total_verse += ' ' + element
    total_verse = total_verse[1:]
    
    return total_verse
    
    
    
#Bible = {'Psalms':Psalms , 'Proverbs':Proverbs}
#print([key for key,value in sentences.items()])

print('All books have been successfully imported.')
print('To print a verse, enter: v("Book Chapter:Verse")')
print('       or verses, enter: v("Book Chapter:Begin,End")')
print('To search for words, enter: findW("word")')