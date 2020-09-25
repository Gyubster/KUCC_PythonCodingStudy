def BinarySearch(Target, Array, Start, End):
    while Start <= End:
        Mid = (Start + End)//2
        if Array[Mid] == Target:
            return Mid
        elif Array[Mid] < Target:
            Start = Mid + 1
        else:
            End = Mid - 1
    return None
#  while 안에서 Mid값을 추가해서 진행. 까먹지않기. 

N = int(input())
NList = list(map(int, input().split()))
NList.sort()

M = int(input())
MList = list(map(int, input().split()))

for i in MList:
    Result = BinarySearch(i, NList, 0, N-1)
    if Result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
