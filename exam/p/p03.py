def p03(x=210):
    reverse=None
    # ↓程式區域↓
    input = str(x)
    reverse = input[::-1]
    if(reverse[0] == '0'):
        reverse = reverse[1,len(reverse)]
    # ↑程式區域↑
    return reverse
print(p03())