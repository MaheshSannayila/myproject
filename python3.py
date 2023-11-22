


def get_largest_sum(a):
    all_lists=[]
    for i in range (len(a)):
        for j in range(i+1,len(a)+1):
            all_lists+= [a[i:j]]
    # print(all_lists)
    sum_1=[]
    for i in all_lists:
        sum_1+=[sum(i)]
    for j in all_lists:
        if sum(j)==max(sum_1):
            print(j)


a=[-3,2,-6,-7,0,8,-1]
get_largest_sum(a)
