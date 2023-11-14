# Selection Sort O(N^2)

def selection_sort(list):
    back=len(list)-1
    for selection_spot in range(back,0,-1):
        max_spot=selection_spot
        for i in range(0,selection_spot):
            if list[i]>list[max_spot]:
                max_spot=i
        list[selection_spot],list[max_spot]=list[max_spot],list[selection_spot]
    return list

print(selection_sort([10,1,2,1,4,4,1,8,1,2,4,1,4,6,26]))