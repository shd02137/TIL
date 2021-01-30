# 탐욕법/ 구명보트

## 첫번째 시도

```python
import collections

def solution(people, limit):
    #people = [1,2,2,2,2,3,3,3,4]
    #limit = 4
    
    answer = 0
    people.sort()
    p=collections.deque(people)
    while p:
        now=p.pop()
        while now < limit:
            if not p:
                break
            
            if now + p[0] > limit:
                break
            now += p.popleft()
        answer +=1
    
        
    return answer
```



## 다른 사람의 풀이

```python

```



## 다시 풀어보기

```python
def solution(people, limit):
    answer = 0
    
    people.sort()
    
    while people:
        if len(people) == 1:
            return answer + 1
        
        if people[0] + people[-1] <=limit:
            people.pop()
            people.pop(0)
        else:
            people.pop()
        answer += 1
    
    return answer
```

빠르다고 생각했지만 효율성 1번에서 시간초과가 나왔다.
pop(n)이 시간복잡도가 커서 발생하는 문제라 deque를 사용하면 쉽게 통과할 수 있지만, 다른방법을 사용해 보기로 했다.

```python
def solution(people, limit):
    answer = 0
    
    people.sort()
    
    head = 0
    foot = len(people)-1
    while head <= foot:
        
        
        if head == foot:
            return answer + 1
        
        if people[head] + people[foot] <= limit:
            head += 1
            foot -= 1
        else:
            foot -= 1
            
        answer += 1
    
    return answer
```

pop() 대신 처음과 끝의 위치를 잡는 변수를 지정하여 문제를 해결하였다.

