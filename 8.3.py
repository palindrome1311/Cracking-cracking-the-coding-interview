import sys
sys.setrecursionlimit(10000000)

def getIndex(arr,start,end):
    if(end<start):
        return -1
    
    mid = int((start+end)/2)
    midValue = arr[mid]
    
    if(midValue==mid):
        return mid
    
    leftIndex=min(mid-1,midValue)
    left=getIndex(arr,start,leftIndex)
    if(left>=0):
        return left

    rightIndex= max(mid+1,midValue)
    right = getIndex(arr,rightIndex,end)
    return right



arr=[-10,-5,2,2,2,3,4,7,9,12,13]
n = len(arr)
start = 0
end  = n-1
print(getIndex(arr,0,n-1))
    