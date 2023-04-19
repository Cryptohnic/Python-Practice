plist=[]
n=int(input('What is your number?: '))
for i in range(2,n):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime: plist.append(i)
print(f'List of prime numbers less than {n}: {plist}')