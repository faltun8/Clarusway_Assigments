def not_string(word):
    if word[0:3] == "not":
        return word
    else:
        return "not " + word
