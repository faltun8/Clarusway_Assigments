"""Given two strings, return True if either of the strings appears at the very end of the other string, ignoring
upper/lower case differences (in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.
end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True"""

def end_other(word1,word2):
    w1len = len(word1)
    w2len = len(word2)
    if w1len > w2len:
        return True if word1.lower()[-w2len:] == word2.lower() else False
    else:
        return True if word2.lower()[-w1len:] == word1.lower() else False

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))