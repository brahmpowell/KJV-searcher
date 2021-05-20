# ReadMe

A simple (King James) Bible searching algorithm written entirely in Python.  Written in 2015 as a practice project for advancing in Python.

Running `from Runit.Searches import *` will load the searching functions.  WARNING: As always, be careful using `import *`.  To be safe, you may want to `import Search_Functions as sf` instead.

`findW("words separated by spaces", casesensitive=False, bk=None)` searches for a word or list of words, not in any particular order.  The `bk` parameter, if None, will cause all books of the Bible to be searched.  If `bk='OT'` or `bk='ot'`, only the Old Testament will be searched (same with `'nt'` or `'NT'` for the New Testament).  To search through only one book, set `bk` to the name of that book.  To search through a list of books, set `bk` to a list of book names.

`v("Book_name_with_underscores_if_necessary Chapter:Verse")` searches for a specific verse.  If looking for 2nd Corinthians 1:1, for example, enter `v("II_Corinthians 1:1")`.  A full list of book names can be found in `Runit/Searches.py` as well as in other files.

`v("Book_name_with_underscores_if_necessary Chapter:VerseBegin,VerseEnd")` searches for a passage.  If looking for 2nd Corinthians 1:1-1:3, for example, enter `v("II_Corinthians 1:1,3")`.

To see the exact notation used for each book name, execute `print_books()`.

### TODO:
- [ ] Create a GUI.
- [ ] Fix case-sensitivity for all-caps use of LORD.
- [ ] Analyze memory usage, possibly change search method to live file reading instead of file loading (this may be slower, however).
- [x] Capability to search a single chapter, or multiple chapters, or one testament at a time.
- [ ] Fix context printing in `findW()`.
- [ ] Avoid printing individual verses in separate `print` calls.