# -*- coding: utf-8 -*-
#4
n,p=map(int, input().split())
A=[]
for i in range(1,n+1):
    s=list(map(str,str(i)))
    #print(s)
    A=A+s
#print(A)
time=A.count(str(p))
print(time)