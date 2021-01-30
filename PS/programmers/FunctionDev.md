# 큐 & 스택 / 기능개발

## 첫번째, 2번째 시도

```python
import math

def solution(progresses, speeds):
    answer = []
    day=[0]*len(progresses)
    for i in range(len(progresses)):
        day[i]=math.ceil((100-progresses[i])/speeds[i])

    print(day)

    temp = -1
    for i in range(len(day)):
        if temp>=i:
            i=i
            print("!")
        else:
            print("i="+str(i))
            count=1

            if i==len(day)-1:
                answer.append(count)
                break
            for j in range(i+1,len(day)):
                print(j)
                if day[i]<day[j]:
                    print(day[i])
                    temp=j-1
                    answer.append(count)
                    print("count"+str(count))
                    break
                else:
                    count += 1
                    if j==len(day)-1:
                        answer.append(count)
                        temp=j
                        print("end")


    return answer


```

```python
import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    day=deque([0]*len(progresses))
    for i in range(len(progresses)):
        day[i]=math.ceil((100-progresses[i])/speeds[i])
    
    left=day[0]
    count=0
    while len(day)>0:
        temp = day.popleft()
        if left<temp:
            answer.append(count)
            count=1
            left = temp
        else:
            count += 1
            
    answer.append(count)
    
    return answer
```

완성까지 걸리는 일수를 계산해서 답을 내었다.



## 다른 사람의 풀이

```


```







## 다시 풀어보기

```python
def solution(progresses, speeds):
    answer = []
    end = 0
    while end < len(progresses):
        progresses = [progress + speed for progress,speed in zip(progresses,speeds)]
        if progresses[end] >= 100:
            count = 0
            for progress in progresses[end:]:
                if progress >= 100:
                    count += 1
                    end += 1
                else:
                    break
            answer.append(count)
        
    
    return answer
```

프로그래시스를 계속 스피드스 만큼 더해서 해결하였다.

처음에는 남은 일수를 계산해야한다는 생각으로 풀었는데, 다시 생각해보니 간단하게 진척도가 100만 넘어가면 되는 문제였다.

pop(0)을 사용하면 불필요한 progresses를 계산하지 않게 되어 속도가 훨신 빠르지만 
새롭게 임포트 시키는 것 없이 풀어보기 위해 이렇게 했다.

다시 생각해보니 break 할때 progresses = progresses[end:], speeds = speeds[end:]를 하게 된다면 더욱 빨라질것으로 예상된다.

그래서 다시 작성해 보았다.

```python
def solution(progresses, speeds):
    answer = []
    
    while progresses:
        progresses = [progress + speed for progress,speed in zip(progresses,speeds)]
        if progresses[0] >= 100:
            count = 0
            for progress in progresses[count:]:
                if progress >= 100:
                    count += 1
                else:
                    break
            progresses = progresses[count:]
            speeds = speeds[count:]
            answer.append(count)

        
    return answer
```

리스트의 크기가 작아져서 시간이 조금 단축되었다.



pop(0)가 시간이 오래 걸린다는 생각에 pop(0)를 안쓰고 있는데, 한번 써보았다.

```python
def solution(progresses, speeds):
    answer = []
    
    while progresses:
        progresses = [progress + speed for progress,speed in zip(progresses,speeds)]
        if progresses[0] >= 100:
            count = 0
            for progress in progresses[count:]:
                if progress >= 100:
                    count += 1
                else:
                    break
            for _ in range(count):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(count)

        
    return answer
```

시간이 많이 증가하는것을 확인할 수 있었다.(최대 1.5배 증가하였다.)



더 생각해보니 모든 날짜를 계산하는것이 아니고 일자를 하루씩 늘려가면서 아직 올리지 못한 작업중 맨 앞 작업의 진척도가 100이 넘는지만 계산하면 되는 간단한 문제였다.

