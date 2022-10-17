from turtle import end_fill


plist=[1,2]
n=int(input('What is your number?: '))
if n==1:
    print("There are no prime numbers less than 1")
    exit()
if n==2:
    print('List of prime numbers less than',str(n)+':',plist[0:1])
    exit()
for i in range(3,n):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime:plist.append(i)
print('List of prime numbers less than',str(n)+':',plist)