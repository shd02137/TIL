# 정렬 / 가장큰수

## 첫번째 시도

```python
def solution1(numbers):
    answer = ''
    temp = list(map(str,numbers))
    
    temp.sort(key=lambda x: x*3)
    temp.reverse()
    while 1:
        answer = answer + temp.pop(0)
        if len(temp)==0:
            break
    
    answer = str(int(answer))
    
    return answer
```





## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python
def solution(numbers):    
    answer = ''
    temp = list(map(str,numbers))
    
    temp.sort(key=lambda x: x*4)
    temp.reverse()
    
    answer = "".join(temp)
    
    answer = str(int(answer))
    
    return answer
```

