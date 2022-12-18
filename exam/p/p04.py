def p04(input = 23):
    output_list=None
    # ↓程式區域↓
    keypad = {
        '0' : [],
        '1' : [],
        '2' : ["a", "b", "c"],
        '3' : ["d", "e", "f"], 
        '4' : ["g", "h", "i"],
        '5' : ["j", "k", "l"],
        '6' : ["m", "n", "o"],
        '7' : ["p", "q", "r", "s"],
        '8' : ["t", "u", "v"],
        '9' : ["w", "x", "y", "z"]
    }
    if (input == None):
        output_list = []
    else:
        input_list = [str(input)[i] for i in range(0, len(str(input)))]
        for i in range(0, len(input_list)):
            if(i == 0):
                output_list = keypad[input_list[i]]*3**(len(str(input))-1)
                output_list.sort()   
            else:
                for j in range(0, len(output_list)):
                    add_list = keypad[input_list[i]]*3
                    output_list[j] += add_list[j]
     
    # ↑程式區域↑
    return output_list
print(p04())