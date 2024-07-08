n=int(input())
p=int(input())
time=0
for i in range(1,n+1):
    for j in str(i):
        if j==str(p):
            time=time+1
print(time)