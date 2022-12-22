def p06(nums = [2,7,11,15], target = 9):
    output_list=None
    # ↓程式區域↓
    output_list = []
    index = []
    for i in range(0,len(nums)):
        for j in range(0, len(nums)):
            total = nums[i] + nums[j]
            if(total == target and i != j):
                index.append(i)
                index.append(j)
    output_list = set(index)
    # ↑程式區域↑
    return output_list
print(p06())