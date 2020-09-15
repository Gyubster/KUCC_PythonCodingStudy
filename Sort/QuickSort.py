List = list(map(int, input().split()))

def QuickSort(List):
    if len(List) <= 1:
        return  List

    pivot = List[0]
    tail = List[1:]
    # 1번뒤부터의 리스트 원소

    LeftSide = [x for x in tail if x <= pivot]
    RightSide = [x for x in tail if x >= pivot]

    return QuickSort(LeftSide) + [pivot] + QuickSort(RightSide)

#List 중간에 원소만 집어넣을수있음. []식으로

print(QuickSort(List))
