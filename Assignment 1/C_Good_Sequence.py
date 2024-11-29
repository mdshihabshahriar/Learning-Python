n = int(input())
ans = 0
a = list(map(int,input().split()))  #list e rakha
dc={} #freq rakhar jonne dictionary
for i in a:
    dc[i]=dc.get(i,0)+1
v=[]   #num and freq eksathe rakhar jonne
for key,val in dc.items():
    v.append((key, val))
for i in range(len(v)):
    if v[i][1] > v[i][0]:
        ans += (v[i][1] - v[i][0])
    elif v[i][1] < v[i][0]:
        ans += v[i][1]
    else:
        continue
print(ans)
