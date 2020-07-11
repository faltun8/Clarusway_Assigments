result =[1,1]
i = 1

while result[-1] < 55:
    result.append(result[i]+result[i-1])
    i+=1

print(result)