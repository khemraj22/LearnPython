def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words #return a list containing all words of a string

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words): # a list is passed to pop the items
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
"""    
s = "This function will break up words for us."
print break_words("This function will break up words for us.")
print sort_words(s)
aList = [123, 'xyz', 'zara', 'abc'];

print_first_word(break_words("This function will break up words for us."))

print_last_word(aList)

print sort_sentence("Takes in a full sentence and returns the sorted words.")

print_first_and_last("Prints the first and last words of the sentence.")


print_first_and_last_sorted("Sorts the words then prints the first and last one.")

"""

