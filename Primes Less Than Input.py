plist=[]
n=int(input('What is your number?: '))
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else: 
        plist.append(i)
print(f'List of prime numbers less than {n}: {plist}')