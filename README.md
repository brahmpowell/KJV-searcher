# ReadMe

A simple (King James) Bible searching algorithm written entirely in Python.

Currently designed for command line use in a Python shell.

Running `Function_scripts/Search_Functions.py` while in a Python shell in the base directory of the project will load the searching functions.

`findW("words separated by spaces", casesensitive=False)` searches for a word or list of words, not in any particular order.

`v("Book_name_with_underscores_if_necessary Chapter:Verse")` searches for a specific verse.  If looking for 2nd Corinthians 1:1, for example, enter `v("II_Corinthians 1:1")`.

`v("Book_name_with_underscores_if_necessary Chapter:VerseBegin,VerseEnd")` searches for a passage.  If looking for 2nd Corinthians 1:1-1:3, for example, enter `v("II_Corinthians 1:1,3")`.

### TODO:
Create a GUI.
Fix case-sensitivity for all-caps use of LORD.
Analyze memory usage, possibly change search method to live file reading instead of file loading (this may be slower, however)
Fix context printing in `findW()`.