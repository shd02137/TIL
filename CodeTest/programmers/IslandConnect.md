# 탐욕법 / 섬연결하기

## 첫번째 시도

```python
def solution(n, costs):
    #costs = [[0,1,12],[0,2,9],[1,2,5],[1,3,1],[2,3,8]]
    inf= 99999
    notvisited = []
    for i in range(n):
        notvisited.append(i)
    visited = []
    distance = [inf]*n
    map = [[inf]*n for i in range(n)]
    
    for i in costs:
        map[i[0]][i[1]] = i[2]
        map[i[1]][i[0]] = i[2]
    
    
    while notvisited:
        start = 0
        if not visited:
            distance[0] = 0
        else:
            min_node = 0
            min_value = inf
            for i in notvisited:
                if min_value>distance[i]:
                    min_value = distance[i]
                    min_node = i
            start = min_node

        notvisited.pop(notvisited.index(start))
        visited.append(start)
        
        
        for i in notvisited:
            if distance[i]>map[start][i]:
                distance[i] = map[start][i]



    
    return sum(distance)
```





## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python

```

