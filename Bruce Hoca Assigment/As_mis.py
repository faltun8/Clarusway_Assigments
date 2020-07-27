def missing_char(word, n):
    return word[:n] + word[n+1:]


print(missing_char('kitchen', 3))