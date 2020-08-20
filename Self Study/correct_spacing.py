
def correct_spacing(sentence):
    return " ".join(sentence.split())

'''OR'''

def correct_spacing(sent):
    while sent[0] == " ":
        sent = sent[1:]
    while sent[-1] == " ":
        sent = sent[:-1]
    i = 0
    while True:
        if i < len(sent):
            if sent[i] == " " and sent[i+1] == " ":
                sent = sent[:i] + sent[i+1:]
            else:
                i+=1
        else:
            break
    return sent














correct_spacing("The film   starts       at      midnight. ")
"""The film starts at midnight."""

correct_spacing("The  waves were crashing  on the     shore.   ")
"""The waves were crashing on the shore."""

correct_spacing("   Always look on    the bright   side of  life.")
"""Always look on the bright side of life."""