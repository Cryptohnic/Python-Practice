# O(N^2)

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(1,i+1):
            if list[j-1]>list[j]:
                list[j-1],list[j]=list[j],list[j-1]
    return list

print(bubble_sort([2,3,1,10,1]))
print(bubble_sort([2,3,1,10,1,9,11,12,1,1,1,10]))