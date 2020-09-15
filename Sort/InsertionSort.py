List = list(map(int, input().split()))

for i in range(len(List)):
    for j in range(i, 0, -1):
        if List[j-1] < List[j]:
            List[j], List[j-1] = List[j-1], List[j]
        else:
            break
# 작은걸 왼쪽 이동.
# j의 범위가 음으로가는 것을 참고.
print(List)
