# 동적계획법 / 정수삼각형

## 첫번째 시도

```python
def solution(triangle):
    answer = []
    for garo in triangle[::-1]:
        if not answer:
            answer = garo
        else:
            temp = []
            for i,value in enumerate(garo):
                temp.append(max(value+answer[i],value+answer[i+1]))
            answer = temp
    return max(answer)
```

아래서부터 가장 큰값이 무엇인지 확인해가면서 진행하였다.



## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python
def solution(triangle):
    answer = []
    
    for line in triangle:
        if not answer:
            answer.append(line[0])
        else:
            pre = pre_line(answer)
            answer = list(map(lambda x,y : x+y,pre,line))
            
    return max(answer)
  
def pre_line(values):
    return_value = []
    return_value.append(values[0])
    for i in range(1,len(values)):
        return_value.append(max(values[i-1],values[i]))
    return_value.append(values[-1])
    return return_value
```

위에서 모든값을 계산해가며 진행하였다.
복잡도는 O(n^2)으로 비슷하지만 먼저한것이 약간 더 빨랐다.