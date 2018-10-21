# ReadMe

A simple (King James) Bible searching algorithm written entirely in Python.  Written in 2015 as a practice project for advancing in Python.

Running `from Search_Functions import *` while in a Python shell in the `Function_scripts` subdirectory of the project will load the searching functions.  WARNING: As always, be careful using `import *`.  To be safe, you may want to `import Search_Functions` instead.

`findW("words separated by spaces", casesensitive=False)` searches for a word or list of words, not in any particular order.

`v("Book_name_with_underscores_if_necessary Chapter:Verse")` searches for a specific verse.  If looking for 2nd Corinthians 1:1, for example, enter `v("II_Corinthians 1:1")`.

`v("Book_name_with_underscores_if_necessary Chapter:VerseBegin,VerseEnd")` searches for a passage.  If looking for 2nd Corinthians 1:1-1:3, for example, enter `v("II_Corinthians 1:1,3")`.

### TODO:
- [ ] Create a GUI.
- [ ] Fix case-sensitivity for all-caps use of LORD.
- [ ] Analyze memory usage, possibly change search method to live file reading instead of file loading (this may be slower, however).
- [ ] Fix context printing in `findW()`.
- [ ] Avoid printing individual verses in separate `print` calls.