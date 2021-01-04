# 정렬 / H-index

## 첫번째 시도

```python
def solution(citations):
    answer = citations[0]
    citations.sort()
    h = 0
    while 1:
        count = 0

        for i in citations:
            if i >= h:
                count += 1
        if h>count:

            break
        answer = h
        h += 1

    return answer
```





## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python
def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    order = count()
    for citation in citations:
        i = next(order)
        print(citation, i)
        if i > citation:
            return i-1
        
    return next(order) -1


def count():
    n = 0
    while 1:
        n += 1
        yield n
```

