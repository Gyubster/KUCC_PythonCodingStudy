List = list(map(int, input().split()))

for i in range(len(List)):
    Minimum_List = i
    for j in range( i+1, len(List)):
        if List[Minimum_List] > List[j]:
            Minimum_List = j
    List[Minimum_List], List[i] = List[i], List[Minimum_List]

# 두개가 바뀌어도 똑같은데 why..?

print(List)
