##selectionsort
def selection(arr):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[min_ind]>arr[j]:
                    min_ind=j
        arr[i],arr[min_ind]= arr[min_ind],arr[i]
    return arr
arr=['g','a','n','g','a','d','h','a','r']
print(arr)
print(selection(arr))


def selection1(arr):
    for i in range(len(arr)):
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[min_ind]>arr[j]:
                    min_ind=j
            arr[i],arr[min_ind]= arr[min_ind],arr[i]
    return arr
arr=[5,2,7,8]
print(arr)
print("selection sort is ",selection1(arr))

####insertion sort

def insertion(arr):
    for i in range(1,len(arr)):
        if(arr[i-1]>arr[i]):
            j=i
            while(j>=0):
                if(j>0 and arr[j-1]>arr[j]):
                    temp=arr[j-1]
                    arr[j-1]=arr[j]
                    arr[j]=temp
                j-=1
    return arr
arr=[4,2,7,8,7,8,6,4]
print(arr)
print("insertion sort is ",insertion(arr))

def insertion1(arr):   ##ascii values
    for i in range(1,len(arr)):
        if(ord(arr[i-1])>ord(arr[i])):
            j=i
            while(j>=0):
                if(j>0 and ord(arr[j-1])>ord(arr[j])):
                   arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
    return arr
arr=['g','a','n','g','a','d','h','a','r']
print(arr)
print("insertion sort is ",insertion1(arr))

####bubble sort
def bubble(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-i-1):
            if (arr[j][1] >arr[j + 1][1]):
                arr[j][1],arr[j+1][1]=arr[j+1][1],arr[j][1]
    return arr
arr=[
    [1,2],
    [3,4],
    [2,1],
    [56,3]
]
a=bubble(arr)
print("bubble sort is ",a)

###merge sort
def merge_sort(arr):
