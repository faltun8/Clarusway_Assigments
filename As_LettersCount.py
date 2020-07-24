sentence = input("Sentence: ")
dic1 = {}
for i in sentence:
    count = 0
    for j in sentence:
        if i == j:
            count+=1
    dic1[i]=count

print(dic1)