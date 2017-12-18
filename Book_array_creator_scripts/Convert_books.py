# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 21:50:06 2015

@author: Brahm
"""

import os
import numpy as np
from numpy import concatenate as npc


def convert_BibleBook(book_info):
    
    """
    Parameters:
    ----------
    
    book_info: 4-element list [name_str, text_str, min_page, max_page]
                with 5th element if there is a space in the book's name
    
    
    """
    name_str = book_info[0]
    print('name: ',name_str)
    text_str = book_info[1]
    min_page = book_info[2]
    print('minpg: ',min_page)
    max_page = book_info[3]
    print('maxpg: ',max_page)
    if len(book_info) == 5:
        name_str_delete = book_info[4]
    else:
        name_str_delete = name_str
    
    # remove Book name and page number
    for i in range(min_page,max_page):
        page_num1 = 'Page %d '%i + name_str_delete
        page_num2 = name_str_delete + ' Page %d'%i
        text_str = text_str.replace(page_num1,'')
        text_str = text_str.replace(page_num2,'')
        
    # remove linebreaks
    text_str = text_str.replace('\n',' ')
    
    
    # separate verses
    sep_verses = []
    for element in text_str:
        # remove open curly brackets an start new verse
        if element == '{':
            sep_verses.append('')
        # remove end curly brackets
        elif element == '}':
            sep_verses[-1] += ''
        # add text
        else:
            # but don't start until the first verse is initiated
            if len(sep_verses) != 0:
                sep_verses[-1] += element
        
        
    # separate references from verses
    sep_refs = []
    for verse_tot in sep_verses:
        # extract chapter number
        index = 0
        character = verse_tot[index]
        chap = ''
        while character != ':':
            chap += character
            index += 1
            character = verse_tot[index]
        # convert to integer
        Chapter = int(chap)
        
        # extract verse number
        index += 1
        character = verse_tot[index]
        ver_num = ''
        while character != ' ':
            ver_num += character
            index += 1
            character = verse_tot[index]
        # convert to integer
        Verse = int(ver_num)
        
        # extract verse
        index += 1
        rest_of_verse = verse_tot[index:]
        
        # recreate sep_verses containing all verses
        sep_refs.append([Chapter,Verse,rest_of_verse])
    
    
    
    # now format nicely like: book = [{'v1':word_array , 'v2':word_array2} , {'v1':word_array , 'v2':word_array2 , 'v3':word_array2} , {'v1':word_array}]
    # step 1: create [{},{},{},...] which is the 'book' array containing dictionaries, each of which are a chapter
    initialize_at = sep_refs[0][0]
    num_chapters = sep_refs[-1][0] + 1 - initialize_at
    final = []
    for i in range(num_chapters):
        final.append({})
    
    
    # step 2: FILL IT!!!
    for verse_info in sep_refs:
        chap_num = verse_info[0]-initialize_at
        verse_num = verse_info[1]
        text_together = verse_info[2]
        # now separate each word
        text_separate = ['']
        original_tongues = True
        for element in text_together:
            # original_tongues = False if brackets are open
            if element == '[':
                text_separate[-1] += element
                original_tongues = False
            # original tongues becomes True if brackets end
            elif element == ']':
                text_separate[-1] += element
                original_tongues = True
            # separate punctuation from words
            elif element == '.' or element == ',' or element == '?' or element == '!' or element == ':' or element == ';':
                # end last "word" and create a new "word" containing the punctuation
                text_separate.append(element)
                """ 
                I think all punctuation is in original tongues,
                    so don't worry about this next bit?
                    
                if original_tongues == False:
                    text_separate[-1] += ']'
                    text_separate.append('[' + element)
                else:
                    text_separate.append(element)
                """
            # create new "word" if there is a space
            elif element == ' ':
                if original_tongues == False:
                    text_separate[-1] += ']'
                    text_separate.append('[')
                else:
                    text_separate.append('')
            # add letter if element is a letter
            else:
                text_separate[-1] += element
        # remove empty "words"
        while '' in text_separate:
            text_separate.remove('')
        while '[]' in text_separate:
            text_separate.remove('[]')
        
        
        final[chap_num][verse_num] = text_separate
    
    
    # move to Book_arrays directory
    old_dir = os.getcwd()
    end_of_parent_dir = old_dir.index('Concordance')
    parent_dir = old_dir[:end_of_parent_dir]
    dir_to_book_arrays = parent_dir + 'Concordance_V1//Book_arrays'
    os.chdir(dir_to_book_arrays)
    np.save(name_str+'_V1.npy',final)

# import Bible Book scripts
old_dir = os.getcwd()
end_of_parent_dir = old_dir.index('Concordance')
parent_dir = old_dir[:end_of_parent_dir]
dir_to_book_array_creator_scripts = parent_dir + 'Concordance_V1//Book_array_creator_scripts'
os.chdir(dir_to_book_array_creator_scripts)
import OT_Genesis_to_Job_TEXT_V1 as OT1
import OT_Psalms_TEXT_V1 as OT2
import OT_Proverbs_to_Malachi_TEXT_V1 as OT3
import NT_TEXT_V1 as NT1

a = OT1.gen_to_job_list
b = OT2.psalms_list
c = OT3.prov_to_mlchi_list
d = NT1.nt_list

all_OT_text = npc([a,b,c])
all_NT_text = d

# put all text into one array
text = npc([all_OT_text,all_NT_text])

# and add relevant info to text arrays fo the books can be processed
All_Book_info = [['Genesis',text[0],0,32],
['Exodus',text[1],31,58],
['Leviticus',text[2],57,78],
['Numbers',text[3],77,104],
['Deuteronomy',text[4],103,126],
['Joshua',text[5],125,142],
['Judges',text[6],139,158],
['Ruth',text[7],155,160],
['I_Samuel',text[8],158,180,'1 Samuel'],
['II_Samuel',text[9],177,196,'2 Samuel'],
['I_Kings',text[10],194,216,'1 Kings'],
['II_Kings',text[11],213,234,'2 Kings'],
['I_Chronicles',text[12],232,252,'1 Chronicles'],
['II_Chronicles',text[13],249,274,'2 Chronicles'],
['Ezra',text[14],271,280],
['Nehemiah',text[15],278,290],
['Esther',text[16],287,296],
['Job',text[17],293,310],
['Psalms',text[18],307,396],
['Proverbs',text[19],391,408],
['Ecclesiastes',text[20],406,418],
['Song_of_Solomon',text[21],411,418,'Song of Songs'],
['Isaiah',text[22],411,448],
['Jeremiah',text[23],445,480],
['Lamentations',text[24],478,484],
['Ezekiel',text[25],481,514],
['Daniel',text[26],511,524],
['Hosea',text[27],521,528],
['Joel',text[28],526,530],
['Amos',text[29],528,536],
['Obadiah',text[30],532,536],
['Jonah',text[31],532,538],
['Micah',text[32],536,544],
['Nahum',text[33],539,544],
['Habakkuk',text[34],539,546],
['Zephaniah',text[35],544,550],
['Haggai',text[36],546,550],
['Zechariah',text[37],546,556],
['Malachi',text[38],553,560],
['Matthew',text[39],557,580],
['Mark',text[40],577,592],
['Luke',text[41],590,612],
['John',text[42],610,628],
['Acts',text[43],625,648],
['Romans',text[44],645,656],
['I_Corinthians',text[45],654,664,'1 Corinthians'],
['II_Corinthians',text[46],661,670,'2 Corinthians'],
['Galatians',text[47],667,674],
['Ephesians',text[48],671,678],
['Philippians',text[49],675,680],
['Colossians',text[50],678,682],
['I_Thessalonians',text[51],680,686,'1 Thessalonians'],
['II_Thessalonians',text[52],682,686,'2 Thessalonians'],
['I_Timothy',text[53],682,688,'1 Timothy'],
['II_Timothy',text[54],686,694,'2 Timothy'],
['Titus',text[55],688,694],
['Philemon',text[56],688,694],
['Hebrews',text[57],688,700],
['James',text[58],698,702],
['I_Peter',text[59],700,704,'1 Peter'],
['II_Peter',text[60],702,706,'2 Peter'],
['I_John',text[61],704,714,'1 John'],
['II_John',text[62],706,714,'2 John'],
['III_John',text[63],706,714,'3 John'],
['Jude',text[64],706,714],
['Revelation',text[65],706,725]]

for i in range(66):
    book_info = All_Book_info[i]
    convert_BibleBook(book_info)


"""
Genesis
Exodus
Leviticus
Numbers
Deuteronomy
Joshua = np.load('Joshua_V1.npy')
Judges = np.load('Judges_V1.npy')
Ruth = np.load('Ruth_V1.npy')
I_Samuel = np.load('I_Samuel_V1.npy')
II_Samuel = np.load('II_Samuel_V1.npy')
I_Kings = np.load('I_Kings_V1.npy')
II_Kings = np.load('II_Kings_V1.npy')
I_Chronicles = np.load('I_Chronicles_V1.npy')
II_Chronicles = np.load('II_Chronicles_V1.npy')
Ezra = np.load('Ezra_V1.npy')
Nehemiah = np.load('Nehemiah_V1.npy')
Esther = np.load('Esther_V1.npy')
Job = np.load('Job_V1.npy')
Psalms = np.load('Psalms_V1.npy')
Proverbs = np.load('Proverbs_V1.npy')
Ecclesiastes = np.load('Ecclesiastes_V1.npy')
Song_of_Solomon = np.load('Song_of_Solomon_V1.npy')
Isaiah = np.load('Isaiah_V1.npy')
Jeremiah = np.load('Jeremiah_V1.npy')
Lamentations = np.load('Lamentations_V1.npy')
Ezekiel = np.load('Ezekiel_V1.npy')
Daniel = np.load('Daniel_V1.npy')
Hosea = np.load('Hosea_V1.npy')
Joel = np.load('Joel_V1.npy')
Amos = np.load('Amos_V1.npy')
Obadiah = np.load('Obadiah_V1.npy')
Jonah = np.load('Jonah_V1.npy')
Micah = np.load('Micah_V1.npy')
Nahum = np.load('Nahum_V1.npy')
Habakkuk = np.load('Habakkuk_V1.npy')
Zephaniah = np.load('Zephaniah_V1.npy')
Haggai = np.load('Haggai_V1.npy')
Zechariah = np.load('Zechariah_V1.npy')
Malachi = np.load('Malachi_V1.npy')

nt_list = [Matthew_string,
Mark_string,
Luke_string,
John_string,
Acts_string,
Romans_string,
I_Corinthians_string,
II_Corinthians_string,
Galatians_string,
Ephesians_string,
Philippians_string,
Colossians_string,
I_Thessalonians_string,
II_Thessalonians_string,
I_Timothy_string,
II_Timothy_string,
Titus_string,
Philemon_string,
Hebrews_string,
James_string,
I_Peter_string,
II_Peter_string,
I_John_string,
II_John_string,
III_John_string,
Jude_string,
Revelation_string]
"""