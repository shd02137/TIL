# 스택&큐 / 프린터

## 첫번째 시도

```python
from collections import deque

def solution(priorities, location):
    answer = 0
    wanted = priorities[location]
    list_doc = deque(priorities)

    while 1:
        if max(list_doc)==list_doc[0]:
            if location == 0:
                answer += 1
                return answer

            list_doc.popleft()
            location -= 1
            answer += 1
        else:
            list_doc.append(list_doc.popleft())
            if location == 0:
                location = len(list_doc) -1
            else:
                location -= 1


    return answer
```

매번 남아있는 우선순위의 최대값을 비교해가며 출력을하여 시간이 오래 걸린다.

최대 O(n^2) 정도의 시간이 걸린다고 예상된다.



## 다른 사람의 풀이

```python
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
```

any를 사용해서 가장 높은 우선도인지 아닌지를 구분하였다.
any를 사용하는 방법은 알지만 실제로 사용을 잘 못했는데 사용을 염두 해두어야겠다.



## 다시 풀어보기

```python
def solution(priorities, location):
    answer = 0
    my_priority=priorities[location]
    
    print("goal's_priority =" , my_priority)
    
    priority_dict = {}
    for priority in priorities:
        if priority in priority_dict:
            priority_dict[priority] += 1
        else:
            priority_dict[priority] = 1
    priority_dict = dict(sorted(priority_dict.items(),key = (lambda x : x[0]),reverse= True))
    
    for priority in priority_dict.keys():
        while priority_dict[priority] > 0:
            if priorities[0] == priority:
                answer += 1
                priorities = priorities[1:]
                priority_dict[priority] -= 1
                if location == 0:
                    return answer
                else:
                    location -= 1
            else:
                priorities.append(priorities[0])
                priorities = priorities[1:]

                if location == 0:
                    location = len(priorities) -1
                else:
                    location -= 1

            
    return answer
```

딕셔너리를 사용하여 우선순의마다 몇개의 문서가 있는지 먼저 알아낸 뒤 출력을 하였다.

매번 max()계산을 하지 않아 시간은 단축되었지만 여전히 최대 O(n^2) 정도의 시간이 걸릴 것으로 예상된다.

우선순위마다 마지막 출력의 index를 구한다면 시간이 훨신 단축될것으로 예상한다.