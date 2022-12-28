def p08(n=8):
    output=None
    # ↓程式區域↓
    squar = 1
    i = 0
    while ((i+1)**2)*2 <= n :
        i += 1
        squar = i**2 
    if n % squar == 0:
        output = n//squar
    else:
        squar = (i+1)**2
        output = n//squar + 1
    # ↑程式區域↑
    return output
print(p08())