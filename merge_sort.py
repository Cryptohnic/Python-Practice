# Reflector: Brandon Alexander
# Liason: Ryan Kelley
# Synchronizer: Ian Buza

# The complexity of pop(0) on a built in list is O(N) because the list has to swap down the 
# all of the rest of the elements one index after removing from the front

# Here is the code without pop

def merge_sort(list):
    if len(list)<2:
        return list
    else:
        first_half= list[:len(list)//2]
        second_half=list[len(list)//2:]
        first_half_sorted=merge_sort(first_half)
        second_half_sorted=merge_sort(second_half)
        return merge(first_half_sorted,second_half_sorted)
        
def merge(first_list,second_list):
    list=[]
    a=0 # first_list index
    b=0 # second_list index
    while a<len(first_list) and b<len(second_list): # while we aren't done with both lists, append the smaller value
        if first_list[a]<second_list[b]:
            list.append(first_list[a]) 
            a+=1
        else:
            list.append(second_list[b])
            b+=1
    while a<len(first_list): # if we didn't finish the first list, add the rest of it
        list.append(first_list[a])
        a+=1
    while b<len(second_list): # if instead we didn't finish the second list, add the rest of it
        list.append(second_list[b])
        b+=1
    return list

if __name__=='__main__':
    # empty case works for merge_sort
    print(merge_sort([]))
    # already reversed case merge_sort still works
    print(merge_sort([10,9,8,7,6,5,4,3,2,1]))
    # assorted list merge_sort still works
    print(merge_sort([6789,1230,123,1,-1,-19287,9837,-98]))
    # already sorted case merge_sort still works
    print(merge_sort([1,2,3,4,5,6,7,8,9,10]))
    # empty case works for merge
    print(merge([],[]))
    # listA last element is less than listB first element for sorted lists merges properly
    print(merge([1,2,3,4,5],[6,7,8,9,10]))
    # listB last element is less than listA first element for sorted lists merges properly
    print(merge([6,7,8,9,10],[1,2,3,4,5]))
    # assorted already sorted lists merge properly
    print(merge([1,3,5,7],[2,4,6,8]))