# 스택&큐 / 주식 가격

## 첫번째 시도

```python
def solution(prices):
    answer = []
    length = len(prices)
    for i in range(0,length):
        n=0
        for j in range(i,length-1):
            if prices[i]>prices[j]:

                answer.append(n)
                i=i+1
                break
                
            n = n + 1
            
            if n==length-1-i:
                answer.append(n)

    answer.append(0)
    
    return answer
```



## 다른 사람의 풀이

```

```

다 비슷비슷해서 안넣었다.



## 다시 풀어보기

```python
def solution(prices):
    answer = []
    prices = list(map(int,prices))
    for self_index in range(len(prices)):
        count = 0
        for other_index in range(self_index+1,len(prices)):
            count = other_index - self_index
            if prices[self_index] > prices[other_index]:
                break
        answer.append(count)
    
    return answer
```

