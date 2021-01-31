# 1260(DFS,BFS) / DFS와 BFS

## 첫번째 풀이

``` python
answer = ""
n,e,start = map(int,input().split())
search_map = [[0]*(n+1) for _ in range(n+1)]
for _ in range(e):
    i,j = map(int,input().split())
    search_map[i][j] = 1
    search_map[j][i] = 1

dfs_visited = [0]*(n+1)
dfs_visited[start] = 1
dfs_str = str(start)+" "

def m_dfs(s,visited,search_map,dfs_str):
    for index,node in enumerate(search_map[s]):
        if node == 1 and visited[index] == 0:
            visited[index] = 1
            dfs_str += (str(index)+" ")
            dfs_str = m_dfs(index,visited,search_map,dfs_str)

    return dfs_str.strip()

answer += m_dfs(start,dfs_visited,search_map,dfs_str)+"\n"

bfs_visited = [0] * (n+1)
bfs_visited[start] = 1
bfs_queue = [start]
while bfs_queue:
    nd = bfs_queue.pop(0)
    answer += str(nd) + " "
    for index,node in enumerate(search_map[nd]):
        if node == 1 and bfs_visited[index] == 0:
            bfs_queue.append(index)
            bfs_visited[index] = 1


answer = answer.strip()

print(answer)
```

처음에 틀린 풀이이다. 방법은 맞는것 같은데 어디서 틀린지 몰라서 다시 만들었다.
백준에서 최소한 어떤 출력이 나오는지만이라도 알았으면 좋겠다.
너무 불편해...

```python
answer = ""
n,e,start = map(int,input().split())
search_map = [[0]*(n+1) for _ in range(n+1)]
for _ in range(e):
    i,j = map(int,input().split())
    search_map[i][j] = 1
    search_map[j][i] = 1

dfs_visited = [0]*(n+1)

def dfs(start,visited):
    result = str(start)+" "
    visited[start] = 1
    for index,value in enumerate(search_map[start]):
        if value == 1 and visited[index] == 0:
            visited[index] = 1
            result += dfs(index,visited)
    return result  
answer += dfs(start,dfs_visited).strip()+"\n"

bfs_visited = [0] * (n+1)
bfs_visited[start] = 1
bfs_queue = [start]
while bfs_queue:
    nd = bfs_queue.pop(0)
    answer += str(nd) + " "
    for index,node in enumerate(search_map[nd]):
        if node == 1 and bfs_visited[index] == 0:
            bfs_queue.append(index)
            bfs_visited[index] = 1

answer = answer.strip()

print(answer)
```

dfs와 bfs를 구현하는 문제였다. 방법은 유명해서 적지 않고 따로 bfs dfs를 정리하는 글을 적을 예정이다.