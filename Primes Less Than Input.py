p=[1,2]
n=int(input('What is your num?: '))
for i in range(3,n):
    f=False
    for j in range(2,i):
        if i%j==0:
            f=True
            break
    if not f:p.append(i)
print('List of prime numbers less than',str(n)+':',p)