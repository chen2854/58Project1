'''
import itertools
N,k=map(int,input().split())
a=[]
for i in range(N):
  n=int(input())
  a.append(n)
rse=0
m=list(itertools.permutations(a,k))
for i in range(len(m)):
  v=1
  for j in range(k):
    v=v*m[i][j]
  if rse<v:
    rse=v
    
print(rse%(pow(10,9)+9))


num=0
for i in range(50000):
  for j in range(50000):
    if i*i+j*j <=pow(50000,2):
      num+=1
print(num*4)
print("www")

n=int(input())
m=[ [None for _ in range(30)]for i in range(30)]
for i in range(n):
  x1,y1,x2,y2=map(int,input().split())
  xleth=min(x1,x2)
  yleth=min(y1,y2)
  xend=max(x1,x2)
  yend=max(y1,y2)  
  for i in range(xleth,xend):
    for j in range(yleth,yend):
      m[i][j]=True
num=0
for i in range(30):
  for j in range(30):
    if m[i][j]==True:
      num+=1
print(num)
'''
for i in range(100,10000):
    a=i
    if (i-1)%5==0:
        i=(i-1)//5
        i=i*4
        if (i-2)%5==0:
            i=(i-2)//5
            i=i*4
            if (i-3)%5==0:
                i=(i-3)//5
                i=i*4
                if (i-4)%5==0:
                    i=(i-4)//5
                    i=i*4
                    if i%5==0:
                        print(a)
                        break


































