import os

read_env = lambda property: os.environ.get(property, None)

def is_vowel(w):
    to_check = ['a', 'e', 'i', 'o', 'u','y', 'A', 'E', 'I', 'O', 'U', 'Y']
    if w in to_check:
        return True     
    return False


def word_found(word, words):
     lowered = [w.lower() for w in words]
     if word.lower() in lowered:
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
    missing = []
    issubword = False

    if checked == original:
        return True, missing 
    else:
        if has_non_vowel_overlap(checked, original):# and not has_missing_non_vowels(checked, original):              
                  
            for i in checked:
                      
                if not is_vowel(i) and checked.count(i) > original.count(i):
                    return False, []
  
                  
                for index, i in enumerate(original):
                    if is_vowel(i):# and i not in checked:
                         missing.append(i)
                  
            if len(missing) < len(checked):
                issubword = True
     
    return issubword, missing

     
def has_missing_vowel(word, words):
    """ The word has a missing vowel and matches one or more other words """
    has_missing = False
    suggestions = []
    for w in words:
        s, m = is_subword(word, w)
        if s and not m:
             return []

        if s and word != w:
            suggestions.append(w)
    return suggestions


def all_uppercase(w):
    """ Helper to verify the word is in upper case """
    return w.upper() == w


def is_capitalized(w):
    """ Helper to verify the word is capitalized """
    return w.capitalize() == w

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
        return False, mc_suggestions

    return True, [] 

