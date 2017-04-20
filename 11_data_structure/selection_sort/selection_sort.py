def selection_sort(li):
    minIdx = 0
    list_len = len(li)
    for i in range(list_len-1):
        midIdx = i
        for j in range(i+1, list_len):
            if li[minIdx] > li[j]:
                minIdx = j
        li[minIdx], li[i] = li[i], li[minIdx]

if __name__=='__main__':
    li = [4, 6, 1, 7, 2, 8, 3, 5, 9, 10, 12, 11]
    selection_sort(li)
    print(li)
