# 동적계획법 / 등굣길

## 첫번째 시도

```python
def solution(m, n, puddles):
    answer = [[0] * (m+1) for i in range(n+1)]

    for i in puddles:
        answer[i[1]][i[0]] = -1
    for i in range(1,n+1):
        if answer[i][1] == -1:
            break
        answer[i][1] = 1
    for i in range(1,m+1):
        if answer[1][i] == -1:
            break
        answer[1][i] = 1
        
    for i in range(2,n+1):
        for j in range(2,m+1):
            if [j,i] not in puddles:
                top = 0
                left = 0
                if answer[i-1][j] != -1:
                    top = answer[i-1][j]
                if answer[i][j-1] != -1:
                    left = answer[i][j-1]
                answer[i][j] = top + left
            
    print(answer)
    return answer[n][m] % 1000000007
```

갈수 있는 가장자리에 모두 1을 넣어준뒤 갈수 있는곳에 갈수 있는 경우의 수를 모두 더해주면서 해결했다. 문제는 쉽지만 해결방법이 복잡하게 나왔다.



## 다시 풀어보기

```python
def solution(m, n, puddles):
    answer = 0
    
    root_count=[[1]*m for _ in range(n)]
    root_count[0][0] = 1
    for j,i in puddles:
        root_count[i-1][j-1] = 0
    

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i==0:
                root_count[i][j] *= root_count[i][j-1]
            elif j==0:
                root_count[i][j] *= root_count[i-1][j]
            else:
                root_count[i][j] *= (root_count[i-1][j] + root_count[i][j-1])


    
    return root_count[n-1][m-1]%1000000007
```

약간 더 짧아 지기는 했지만 만족스럽지 않고 더 짧고 간단해질수  있을것같다.

다른사람의 풀이를 보았다.



## 다른 사람의 풀이

```python
def solution(m,n,puddles):
    grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
    if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1                #미리 -1로 체크
    grid[1][1] = 1
    for j in range(1,n+1):
        for k in range(1,m+1):
            if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[j][k] = 0
                continue
            grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]
```

식은 거의 같지만 map의 왼쪽과 위쪽에 한칸 여유를 주고 0을 넣어주어 어 예외처리를 하지 않을 수 있었다.
