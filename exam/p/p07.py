def p07(version1='1.0.0', version2='1.0.0'):
    output=None
    # ↓程式區域↓
    if len(version2) == len(version1):
        version1_list = []
        version2_list = []
        # 將input放進version1_list & version2_list:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        # version1_list和version2_list的比較(從index 0 到 index 1):
        for i in range(0, len(version1_list)):
            if int(version1_list[0]) < int(version2_list[0]): # index0
                output = -1
                break
            elif int(version1_list[0]) > int(version2_list[0]):
                output = 1
                break
            else: # version1_list[0] == version2_list[0], 比較index1
                if int(version1_list[1]) < int(version2_list[1]):
                    output = -1
                    break
                elif int(version1_list[1]) > int(version2_list[1]):
                    output = 1
                    break
                else: # version1_list[1] == version2_list[1], 比較index2
                    if int(version1_list[2]) < int(version2_list[2]):
                        output = -1
                        break
                    elif int(version1_list[2]) > int(version2_list[2]):
                        output = 1
                        break
                    output = 0
    else:
        output = 0
    # ↑程式區域↑
    return output
print(p07())