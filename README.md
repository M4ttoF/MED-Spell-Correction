# MED-Spell-Correction
Takes a list of incorrect spellings of words from Birkbeck corpus and finds Levenshtein distance with words from WordNet dictionary

# Requirements
If you are using conda you can use the `environment.yml` file
Otherwise all modules used are listed in `requirements.txt`

# Running program
After installing the dependencies run as `python parallel.py` 
It will give you the S@K score for K=1,5,10 accordingly