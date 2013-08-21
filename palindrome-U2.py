# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    text = text.lower()
    text_length = len(text)
    result = (0, 0)
    for start, end in palindromeSmall(text):
    # Grow each small palindrome base to its maximum size.
        while (start > 0 and end+1 < text_length and text[start-1] == text[end+1]):
            start -= 1
            end += 1
    # Check if current palindrome is the largest yet found.
        if end+1-start > result[1]-result[0]:
            result = (start, end+1)
    return result

def palindromeSmall(text):
    '''Returns i,j such that text[i,j+1] is a palindrome of length 2 or 3.'''
    text_length = len(text)
    for i in range(text_length-1):
        if i>0 and text[i-1] == text[i+1]:
            yield i-1, i+1
        if text[i] == text[i+1]:
            yield i, i+1
    
def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
