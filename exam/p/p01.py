def p01(*nums):
    minnum=None
    # ↓程式區域↓
    input = [*nums]
    input.sort()
    minnum = input[0]
    # ↑程式區域↑
    return minnum