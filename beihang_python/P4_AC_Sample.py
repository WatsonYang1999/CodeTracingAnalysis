'''
相关联的知识点
输入输出语句
循环
数组
分支
字符串处理
错误原因，读取输入语句错误
'''

n=int(input())
p=int(input())
time=0
for i in range(1,n+1):
    for j in str(i):
        if j==str(p):
            time=time+1
print(time)