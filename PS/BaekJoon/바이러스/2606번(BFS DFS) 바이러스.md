# 2606번 (DFS BFS) / 바이러스

## 첫번째 풀이

```python
n = int(input())
com = int(input())
com_list = []
for _ in range(com):
    line = map(int,input().split())
    com_list.append([*line])
worldmap = [[0]*(n+1) for _ in range(n+1)]
for i,j in com_list:
    worldmap[i][j] = 1
    worldmap[j][i] = 1

virus = -1
queue = [1]
visited = [1]
while queue:
    node = queue.pop(0)
    virus += 1
    for index in range(1,n+1):
        if worldmap[node][index] == 1:
            if index not in visited:
                queue.append(index)
                visited.append(index)
    

print(virus)
```

1.  __BFS 혹은 DFS를 이용하여 1번에 연결되어있는 노드가 총 몇개인지 개수를 구하면 된다.__



간단한 BFS혹은 DFS를 사용하는 문제였다.