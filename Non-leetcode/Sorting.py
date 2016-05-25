# Time O(nlogn) Space O(n)
def mergeSort(alist):
    print("Splitting ",alist)

    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i += 1
            else:
                alist[k]=righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j += 1
            k += 1

    print("Merging ",alist)

# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)
##########################################################################
# Time O(nlogn) Space O(logn)
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist, first, last):
   if first<last:
       pivot = partition(alist, first, last)
       quickSortHelper(alist, first, pivot-1)
       quickSortHelper(alist, pivot+1, last)

def partition(alist, first, last):
    pivot = alist[first]
    leftmark, rightmark = first+1, last

    while True:
        while leftmark <= rightmark and alist[leftmark] <= pivot:
           leftmark = leftmark + 1

        while alist[rightmark] >= pivot and rightmark >= leftmark:
           rightmark = rightmark -1

        if rightmark < leftmark:
           break

        alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    # print "pivot->", pivot, "    alist->", alist
    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)