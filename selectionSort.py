def selection_sort(lst):
    for i in range(len(lst) - 1):
        minIndex = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst

print(selection_sort([3,2,14,20,100,1,5]))