# 해시 / 위장

## 첫번째 시도

```python
import collections
import numpy

def solution(clothes):
    answer = 1
    temp = 0
    npClothes = numpy.matrix(clothes)
    npClothes = npClothes.T
    clothes = npClothes.tolist()
    result = collections.Counter(clothes[1])
    print(result)
    for i in set(clothes[1]):
        print(result[i])
        answer = answer * (result[i]+1)

    return answer-1
```

방법은 간단하게 각각 의상의 종류별 개수를 구한뒤 조합개수를 구해주었다.

하지만 구현이 상당히 복잡하게 되어있다.

이부분을 해결해보자



## 다른 사람의 풀이

```


```







## 다시 풀어보기



```python
def solution(clothes):
    answer = 1
    clothes_set={}
    for cloth in clothes:
        if cloth[1] in clothes_set.keys():
            clothes_set[cloth[1]] += 1
        else:
            clothes_set[cloth[1]] = 1
    for i in clothes_set:
        answer *= (clothes_set[i] + 1) 
    return answer-1

```

처음에 했던 방법은 딕셔너리를 사용하지 않고 풀었지만 딕셔너리를 사용하고 훨신 간단하게 문제를 해결할 수 있었다.