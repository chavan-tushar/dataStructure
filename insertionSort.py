def insertion_sort(lst):
    for i in range(1, len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i] , lst[j] =lst[j] , lst[i]
    return lst

print(insertion_sort([1,12,100,3,4,5,10,2]))