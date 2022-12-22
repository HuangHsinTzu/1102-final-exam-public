def p05(l1=[1,4,3,2,5,2], x=3):
    output_list=None
    # ↓程式區域↓
    if(0 < x < 200):
        l2 = []
        l3 = []
        for i in range(0,len(l1)):
            if(l1[i] < x):
                l2.append(l1[i]) 
            else: 
                l3.append(l1[i])        
        l2.extend(l3)
        output_list = l2   
    # ↑程式區域↑
    return output_list
print(p05())