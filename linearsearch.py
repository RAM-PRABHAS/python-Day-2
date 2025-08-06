list_1 = [2,3,5,7,11,13,56,97,0,99,49,63,17,999]
target = 999
for i in range(len(list_1)):
    if target == list_1[i]:
        print(i)
        break