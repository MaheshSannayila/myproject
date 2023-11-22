def get_all_posible_combinations(a):
    a=sorted(a)
    items=list(range(len(a)))
    combination_1=[]
    for item in items:
        combination_1.append([item])
    # print(combination_1)
    combination_2=[]
    for combination in combination_1:
        for item in items:
            if item >combination[-1]:
                combination_2.append(combination+[item])
    # print(combination_2)
    combinations=[]
    for combination in combination_2:
        single_com=[]
        for i in combination:
            single_com.append(a[i])
        combinations.append(tuple(single_com))
    c=combinations
    return sorted(set(c))
a=input().split()
r=get_all_posible_combinations(a)
for i in r:
    print(*i)
