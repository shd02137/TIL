#  / 순위

## 첫번째 시도

```python
def solution(n, results):
    answer = 0
    
    wins = [[] for _ in range(n+1)]
    loses = [[] for _ in range(n+1)]
    
    for _ in range(n):
        for result in results: 
            win = result[0]
            lose = result[1]
            if lose not in wins[win]:
                wins[win].append(lose)
            if win not in loses[lose]:
                loses[lose].append(win)
            for i  in wins[lose]:
                if i not in wins[win]:
                    wins[win].append(i)
                if win not in loses[i]:
                    loses[i].append(win)
            for i in loses[win]:
                if i not in loses[lose]:
                    loses[lose].append(i)
                if lose not in wins[i]:
                    wins[i].append(lose)
    

        
                
    # print(wins,loses, sep = "\n")
    
    for i in range(1,n+1):
        if len(wins[i]) + len(loses[i]) + 1 == n:
            answer += 1
        
    return answer
```

방법은 맞는데 시간초과가 나온다.
처음에 리스트가 아닌 집합을 사용하려고 했지만 오류로 인해 리스트로 선회했었는데,
방법도 처음에 집합을 사용했을때와 달라졌고, 시간 초과를 해결하려면 집합을 사용해야만 할것 같으므로 다시 시도해 보았다.



```python
def solution(n, results):
    answer = 0
    
    wins = [set() for _ in range(n+1)]
    loses = [set() for _ in range(n+1)]
    
    for _ in range(n):
        for result in results: 
            win = result[0]
            lose = result[1]
            wins[win].add(lose)
            loses[lose].add(win)
            for i  in wins[lose]:
                wins[win].add(i)
                loses[i].add(win)
                
            for i in loses[win]:
                loses[lose].add(i)
                wins[i].add(lose)
    
                
    # print(wins,loses, sep = "\n")
    
    for i in range(1,n+1):
        if len(wins[i] | loses[i]) + 1 == n:
            answer += 1
        
    return answer
```

시간이 약 0.125배로 줄면서 바로 성공했다.

은근히 나중에 다시보면 변수명으로 헷갈리게 될것같다.



## 다른 사람의 풀이

```python
from collections import defaultdict
def solution(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    for i in range(1, n + 1):
        for winner in lose[i]: win[winner].update(win[i])
        for loser in win[i]: lose[loser].update(lose[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer
```

방법은 비슷하지만 update를 사용하여 훨신 깔끔하고 읽기 좋게 풀었다.

update를 사용해본적이 없어 익숙하지 않아서 알고도 사용하지 못했는데 다시한번 시도해 봐야 겠다.



## 다시 풀어보기

```python

```

