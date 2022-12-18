def p03(x=210):
    reverse=None
    # ↓程式區域↓
    input = str(x)
    reverse = input[::-1]
    reverse = reverse.strip('0')
    # ↑程式區域↑
    return reverse