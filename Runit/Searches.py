# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:56:52 2015

@author: Brahm Powell
"""


import collections
import numpy as np
import os
from timeit import default_timer as tc

def pjoin(*paths):
    paths = [p for p in paths if p != '']
    if len(paths) > 0:
        joined = os.path.join(*paths)
    else:
        joined = ''
    return joined

def try_index(Verse, vals):
    """
    Helper function.
    Used to find (if possible) indices of words in a list.
    """
    inds = []
    for word_str in vals:
        if word_str in Verse:
            inds.append(Verse.index(word_str))
    return inds

def strip_punct(Verse):
    """
    Strip punctuation and brackets from verse.
    """
    def str_replace(w):
        for p in punctuation_plus:
            w = w.replace(p, "")
        return w
    new_verse = [str_replace(w) for w in Verse]
    new_verse = [w for w in new_verse if w != ""]
    return new_verse



# NOTE:  Bible books are in Bible like:
#    Bible = {'Book':[{'v#':[each_word_string]}]}
#    Bible = {'Genesis':Book, 'Exodus':Book2, ...}
#        Book = [{},{},{}]
# search them by going:
#    Bible['BookName'][chapter#-1][verse#]
Book_names = [
    'Genesis',
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
    'Revelation'
]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
punctuation = '!():;.,?'
punctuation_plus = punctuation + '[]'

Bible = {}
Bible_searchable = {}
version = 'V1'
for book_name in Book_names:
    fname = book_name + '_' + version + '.npy'
    fpath = pjoin('Book_arrays', fname)
    Bible[book_name] = np.load(fpath, allow_pickle=True)
    Bible_searchable[book_name] = []
    Book = Bible[book_name]
    for chapter_index in range(len(Book)):
        Chapter = Book[chapter_index]
        Chapter = {verse_name:strip_punct(EntireVerse) for verse_name,EntireVerse in Chapter.items()}
        Bible_searchable[book_name].append(Chapter)
    

def findW(words, casesensitive=False, context=False, ordered=0, bk=None):
    """
    Used to locate instances of words in the Bible.
    Input words must be a single string, with words separated by spaces.
    Args:
        words:          (string) Single space-separated string of words to find (verse must contain all words)
        casesensitive:  (bool, default False) Whether to respect letter capitalizations
        context:        (bool, default False) Whether to search verses "in context" (NotImplemented)
        ordered:        (int, default 0) Whether to search for words properly ordered
            0 - Order does not matter
            1 - Words should be in order, but need not be consecutive
            2 - Words should be in order and consecutive (NotImplemented)
        bk:             (optional) Options for restricting search to certain parts of the Bible.
            None - searches entire Bible
            'OT' - searches Old Testament only
            'NT' - searches New Testament only
            list - a list of books to search through
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

    # change apostrophes?
    for i in range(len(word_array)):
        word = word_array[i]
        if "'" in word:
            word_split = word.split("'")
            word = u"\u2019".join(word_split)
            word_array[i] = word
    
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
        # print(words)
        # print(Words)
    else:
        words = word_array
        # print(words)
            

    verses_containing_words = 0
    verses_containing_extra_words = 0
    occurrences = 0
    
    # search entire Bible, or one book, or multiple books
    if bk is None:
        # If no book is specified, search entire Bible
        books_to_go_through = Book_names
    elif type(bk) == list:
        # If a list of books is specified, search those books
        books_to_go_through = bk
        for bkk in books_to_go_through:
            if bkk not in Book_names:
                print(bkk + ' not found in the books of the Bible.')
                return
    elif type(bk) == str:
        # If a single string is entered, check if it is a book, or the entire new/old testament
        books_to_go_through = [bk]
        if bk not in Book_names:
            if bk.upper() == 'OT':
                books_to_go_through = Book_names[:39]
            elif bk.upper() == 'NT':
                books_to_go_through = Book_names[39:]
            else:
                print(bk + ' not found in the books of the Bible.')
                return

    # go through books of the Bible
    for book_name in books_to_go_through:
        Book = Bible_searchable[book_name]
        
        # go through each chapter
        for chapter_index in range(len(Book)):
            chapter_number = chapter_index + 1
            Chapter = Book[chapter_index]
            
            # go through each verse
            for verse_name,EntireVerse in Chapter.items():

                # In case words should be matched in order, store a copy of the verse
                Verse = EntireVerse

                # check to see if each word is in the verse
                word_index = 0
                contains = True
                contains_added = True
                while contains and word_index < len(words):
                    
                    # If upper/lowercase is unimportant...
                    if casesensitive == False:
                        word = words[word_index]
                        Word = Words[word_index]
                        # Is word in verse? (also check non-original tongues)
                        if (word not in Verse) and (Word not in Verse):
                            contains = False
                        elif ordered != 0:
                            # If word is in verse, and order is important, let subsequent calls only search the rest of the verse
                            split_index = min(try_index(Verse, [word, Word]))
                            if (ordered == 2) and (word_index != 0) and (split_index != 0):
                                contains = False
                            Verse = Verse[split_index+1:]
                            
                    # If upper/lowercase is important...
                    elif casesensitive == True:
                        word = words[word_index]
                        # Is word in verse? (also check non-original tongues)
                        if word not in Verse:
                            contains = False
                        elif ordered != 0:
                            # If word is in verse, and order is important, let subsequent calls only search the rest of the verse
                            split_index = Verse.index(word)
                            if (ordered == 2) and (word_index != 0) and (split_index != 0):
                                contains = False
                            Verse = Verse[split_index+1:]
                            
                    word_index += 1

                if contains == True:
                    verses_containing_words += 1
                    ActualVerse = Bible[book_name][chapter_index][verse_name]
                    total_verse = verse_writeout(ActualVerse)
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



def v(Book_Chapter_Verses, printing=True, saveit=False):
    """
    Used to simplify process of selecting verse or verses
    """
    data = Book_Chapter_Verses.split(':')
    if len(data) == 1:
        # Book name and chapter specified - print entire chapter
        verses(Book_Chapter_Verses)
    elif data[1] == '':
        # Book name and chapter specified - print entire chapter
        verses(Book_Chapter_Verses)
    elif ',' in data[1]:
        # Book name and multiple verses specified - print verse range
        verses(Book_Chapter_Verses)
    else:
        # Book name and single verse specified - print single verse 
        verse(Book_Chapter_Verses,printing=True,saveit=False)
        
        
    
def verse(Book_Chapter_Verse, printing=True, saveit=False):
    
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
    

# def verses(Book_Chapter_Verses):
#     """
#     return multiple verses in a row.
#     input as 'BookName Chapter:Begin,End'
#     """
    
#     # check each element until ':' is reached to determine book name
#     index = 0
#     element = Book_Chapter_Verses[index]
#     while element != ':':
#         index += 1
#         element = Book_Chapter_Verses[index]
    
#     # extract book name
#     Book_Chapter = Book_Chapter_Verses[0:index]
    
#     # check each element until ',' is reached to determine 1st verse 
#     indexB = index + 1
#     element = Book_Chapter_Verses[indexB]
#     while element != ',':
#         indexB += 1
#         element = Book_Chapter_Verses[indexB]
    
#     # extract first verse
#     Begin = Book_Chapter_Verses[index+1:indexB]
#     BeginNumber = int(Begin)
    
#     # extract last verse
#     End = Book_Chapter_Verses[indexB+1:]
#     EndNumber = int(End) + 1
    
#     # print the verses
#     for i in range(BeginNumber,EndNumber):
#         print('    (' + Book_Chapter + ':%d)'%i)
#         verse(Book_Chapter + ':%d'%i)

def verses(Book_Chapter_Verses):
    """
    return multiple verses in a row.
    input as 'BookName Chapter:Begin,End'
    or       'BookName Chapter:'
    """

    # Split Book_Chapter data from verse data
    data = Book_Chapter_Verses.split(':')
    Book_Chapter = data[0]
    Verses_range = data[1] if len(data) > 1 else ''

    # If no verses specified, print all verses in chapter
    if Verses_range == '':
        Book_Chapter_split = Book_Chapter.split(' ')
        Book = Book_Chapter_split[0]
        Chapter = int(Book_Chapter_split[1])
        Begin = 1
        End = len(Bible[Book][Chapter-1]) + 1
    else:
        # Get beginning and end verses indices
        Begin_End = Verses_range.split(',')
        Begin = int(Begin_End[0])
        End   = int(Begin_End[1]) + 1

    # Print out each verse
    for i in range(Begin,End):
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
    
    
def print_books():
    """Prints out the book names used."""
    print('\nOLD TESTAMENT:')
    print(Book_names[:39])
    print('\nNEW TESTAMENT:')
    print(Book_names[39:])
    print('')


def count():
    """Count number of chapters, verses in Bible."""

    print('BOOK : NUM_CHAPTERS NUM_VERSES')
    num_chapters = {book_name: 0 for book_name in Book_names}
    num_verses   = {book_name: 0 for book_name in Book_names}
    book_name_chars = [len(book_name) for book_name in Book_names]
    blank_slate = ['-' for _ in range(max(book_name_chars) + 2)]

    # go through books of the Bible
    for book_name in Book_names:
        Book = Bible[book_name]
        
        # go through each chapter
        for chapter_index in range(len(Book)):
            num_chapters[book_name] += 1
            chapter_number = chapter_index + 1
            Chapter = Book[chapter_index]
            
            # go through each verse
            for verse_name,Verse in Chapter.items():
                num_verses[book_name] += 1

        num_chars = len(book_name)
        bk_printable = list(blank_slate)
        bk_printable[:num_chars+2] = [el for el in book_name+' -']
        bk_printable = ''.join(bk_printable)
        #print(book_name, ':', num_chapters[book_name], num_verses[book_name])
        print(bk_printable, num_chapters[book_name], num_verses[book_name])

    num_chapters = [num_chapters[book_name] for book_name in Book_names]
    num_verses   = [num_verses[book_name]   for book_name in Book_names]
    num_chapters_OT = num_chapters[:39]
    num_chapters_NT = num_chapters[39:]
    num_verses_OT   = num_verses[:39]
    num_verses_NT   = num_verses[39:]
    print('OT    :', sum(num_chapters_OT), sum(num_verses_OT))
    print('NT    :', sum(num_chapters_NT), sum(num_verses_NT))
    print('Total :', sum(num_chapters), sum(num_verses))







#Bible = {'Psalms':Psalms , 'Proverbs':Proverbs}
#print([key for key,value in sentences.items()])

print('All books have been successfully imported.')
print('To display a verse: v("Book Chapter:Verse")')
print('         or verses: v("Book Chapter:Begin,End")')
print('To search for words: findW("word")')