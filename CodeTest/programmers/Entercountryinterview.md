# 이분탐색 / 입국심사

## 첫번째 시도

이분 탐색을 시도하지 않고 실제로 입국심사를 하는것처럼 매번 가장 빨리 끝나는 입국심사대를 탐색하여 사람을 넣었다.

결과는 당연히 시간 초과로 실패했다.

이후 이분탐색을 한 타인의 코드를 보고 한번 이해를 한뒤 이후 다시 풀기를 다짐하고 종료했다.

그리고 다시 풀어보았다.

```python
def solution(n, times):
    answer = 0
    min_WaitingTime = 0
    max_WaitingTime = n * max(times)
    
    
    print(min_WaitingTime)
    print(max_WaitingTime)
    
    while min_WaitingTime < max_WaitingTime:
        middle = (min_WaitingTime + max_WaitingTime)/2
        middle_total = middle * n
    
    answer = min_WaitingTime
    
    return answer
```

시간을 기준으로 while 문을 돌리고 좌측 시간 끝과 우측 시간 끝을 이동시키면서 이분탐색을 한다는 것은 기억이 나지만 뭘기준으로 시간을 비교했는지 도저히 기억이 안나서 이상태에서 한참 고민을 했다.

결국 한참을 고민한 결과 시간동안 할 수 있는 사람을 기준으로 좌우 시간끝을 조정하였다.

```
def solution(n, times):
    answer = 0
    min_WaitingTime = 0
    max_WaitingTime = n * max(times)
    

    while min_WaitingTime < max_WaitingTime:
        
        middle = int((min_WaitingTime + max_WaitingTime)//2)
        able_people = 0
        for time in times:
            able_people += int(middle//time)
        if able_people < n:
            min_WaitingTime = middle + 1 
        else:
            max_WaitingTime = middle
        
        
    
    answer = min_WaitingTime
    
    return answer
```

통과는 했는데 이분탐색할 때 좌우 값을 결정하는 것이 너무 헷갈린다.





## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python

```



