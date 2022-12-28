def p03(x=210):
    reverse=None
    # ↓程式區域↓
    output = 0
    input = str(x)
    output = input[::-1]
    reverse = int(output)
    # ↑程式區域↑
    return reverse
print(p03())