def p02(a=1, b=100):
    evensum=None
    result = 0
    # ↓程式區域↓
    for i in range(a,b+1):
        if i % 2 == 0:
            result += i
            evensum = result
    # ↑程式區域↑
    return evensum