def p09(citations=[1,3,1]):
    h=None
    # ↓程式區域↓
    for i in range(1, len(citations)+1):
        count = 0
        for j in range(0, len(citations)):
            if citations[j] >= i :
                count = count+1
            if count == i :
                h = count
                break
    # ↑程式區域↑
    return h
print(p09())
