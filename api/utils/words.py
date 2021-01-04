import os

read_env = lambda property: os.environ.get(property, None)

def is_vowel(w):
    to_check = ['a', 'e', 'i', 'o', 'u','y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if w in to_check:
        return True     
    return False


def word_found(word, words):
     if word in words:
         return True
        
     if word.lower() in words:
         return True
        
     if word.capitalize() in words:
         return True
        
     if word.upper() in words:
         return True

     return False


def has_missing_non_vowels(w, orig):
    missing = []
    for i in w:
        if w.count(i) < orig.count(i) or i not in orig:
             return True

    if len(orig) > len(w):
       for i in orig:
           if not is_vowel(i):
               if i not in w or w.count(i) < orig.count(i):
                   missing.append(i)

    return len(missing) > 0


def has_non_vowel_overlap(w, orig):
    missing = []
    
    if len(w) > 0 and len(orig) > 0:
        if w[-1] != orig[-1]:
            return False
        if w[0] != orig[0]:
            return False             

    for i in orig:
        if not is_vowel(i) and i not in w: 
             return False
    for i in w:
        if not is_vowel(i) and i not in orig:
            return False
    return True


def is_missing_vowel(missing):
    """ Helper function to check if a vowel is missing """

    to_check = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in missing:
        if i not in to_check:
            return False
    return True


def is_subword(checked, original):
    """ Use this to identify if one word is subword of another """
    issubword = False

    if checked == original:
        return True
    else:
        if has_non_vowel_overlap(checked, original): 
            return True
      
    return issubword

     
def has_missing_vowel(word, words):
    """ The word has a missing vowel and matches one or more other words """
    has_missing = False
    suggestions = []
    for w in words:
        s = is_subword(word, w)

        if s: # and word != w:
            suggestions.append(w)
    return suggestions


def all_uppercase(w):
    """ Helper to verify the word is in upper case """
    return w.upper() == w


def all_lowercase(w):
    """ Helper to very the word is in lower case """
    return w.lower() == w 


def is_capitalized(w):
    """ Helper to verify the word is capitalized """
    return w.capitalize() == w


def in_legitimate_format(w):
    """ Check if the word is capitalized or all upper case """
    if is_capitalized(w) or all_uppercase(w):
        return True
    elif all_lowercase(w):
        return True
    return False    


def has_repeated_characters(word, words):

    suggestions = []
    for w in words:
        if w == word:
            return []
        elif has_non_vowel_overlap(word, w):
            for i in w:
                if w.count(i) < word.count(i):
                    suggestions.append(w)
    return list(set(suggestions)) 

def has_mixed_casing(word, words):
    """ Has mixed casing """
    suggestions = []
    has_mixed = False
 
    for w in words:
        if w.lower() == word.lower() and w!=word:
            if not is_capitalized(w) and not all_uppercase(w):
                suggestions.append(w)  
 
    return suggestions


def has_combination(word, words):
    """ The case when we may have mixture of scenarios """
    suggestions = []

    if not is_capitalized(word) and not all_uppercase(word):
        word = word.lower()

    rc_suggestions = has_repeated_characters(word, words)

    for i in word:
        for index, w in enumerate(rc_suggestions):
            if is_vowel(i) and i not in w:
                rc_suggestions.pop(index)
                        
    return rc_suggestions 


def spellcheck(word):
    """ Check spelling """

    with open(read_env("DICT_PATH")) as f:
        words = [i[:-1] for i in f.readlines()]

    # Check if the actual word as is in vocabulary
    if word_found(word, words):
        return True, []

    # The mixed case
    combinations = has_combination(word, words)
    if combinations:
        return False, combinations

    # The missing vowel case
    mv_suggestions = has_missing_vowel(word, words)
    if mv_suggestions:
        return False, mv_suggestions

    # The repeated character case
    rc_suggestions = has_repeated_characters(word, words)
    if rc_suggestions:
        return False, rc_suggestions


    # The mixed casing case
    mc_suggestions = has_mixed_casing(word, words)
    if mc_suggestions:

        if word_found(word, mc_suggestions):
            return True, []

        return False, mc_suggestions

    # Word is in vocabulary and has legit case
    if in_legitimate_format(word):
        if word_found(word, words):
            return True, []


    # By now we only want to report as found th words that relate to vocabulary
    if not word_found(word, words):
        return False, []

    return True, [] 

