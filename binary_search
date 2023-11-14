# O(log(N))

def binary_search(list,target):
    front=0
    back=len(list)-1
    count=0
    while front<=back:
        if front==back:
            return f'{target} found at spot {mid} after {count} iterations' if list[front]==target else f'{target} not found after {count} iterations in a list of size {len(list)}'
        count+=1
        mid=(front+back)//2
        if list[mid]==target:
            return f'{target} found at spot {mid} after {count} iterations'
        elif list[mid]>target:
            back=mid-1
        else:
            front=mid+1
    return f'{target} not found after {count} iterations'

print(binary_search([1],10))
print(binary_search([1,2],10))
print(binary_search([1,2,3],10))
print(binary_search([1,2,3,4],10))
print(binary_search([1,2,3,4,5],10))
print(binary_search([1,2,3,4,5,6],10))
print(binary_search([1,2,3,4,5,6,7],10))
print(binary_search([1,2,3,4,5,6,7,8],10))
print(binary_search([1,2,3,4,5,6,7,8,9],10))
print(binary_search([1,2,3,4,5,6,7,8,9,10],12))
print(binary_search([1,2,3,4,5,6,7,8,9,10,11],12))
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12],13))
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13],14))