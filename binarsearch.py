list_1 = [1,2,3,4,5,6,7,8,9,10]
target = 7
start = 5
end = 9
index = -1
while start <= end:
    middle = (start + end) // 2
    if list_1[middle] == target:
        index = middle
        print(index)
        break
    elif list_1[middle] > target:
        end = middle - 1
    else:
        start = middle + 1
else:
    print(index)

