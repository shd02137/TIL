# 탐욕 법 / 단속카메라

## 첫번째 시도

```python
def solution(routes):
    answer = 1
    unique_routes = []
    for i in routes:
        if i not in unique_routes:
            unique_routes.append(i)
    unique_routes.sort()
    endPoint = -99
    for i in unique_routes:
        if endPoint == -99:
            endPoint = i[1]
        else:
            if endPoint>=i[0]:
                if endPoint>i[1]:
                    endPoint = i[1]
                    
            else:
                endPoint = i[1]
                answer += 1
        print(i)
        print(endPoint)
        print(answer)
        
    return answer
```

우선 정렬을 한뒤 나가는 지점이 가장 작은 지점을 찾는다.
이 후 나가는 지점보다 뒤에있는 시작 지점을 찾으면 카메라를 이전에 찾아놓은 가장 작은 나가는 지점에 설치한뒤 새로운 설치 위치를 찾는다. 
이 작업을 모든 경로에 대해 전부 수행한다.  



## 다른 사람의 풀이

```python

```



## 다시 풀어보기

```python
def solution(routes):
    answer = 0
    sorted_routes = sorted(routes,key=lambda x : x[1])
    
    while sorted_routes:

        temp_routes = [route for route in sorted_routes if route[0] > sorted_routes[0][1] ]
        sorted_routes = sorted(temp_routes,key=lambda x : x[1])
        answer += 1
    
    return answer
```

풀이방법은 이전에 풀었던 방식과 똑같았다.

하지만 리스트 안에 for 문을 포함하는 리스트 내포와 lambda 함수를 통한 sorted를 활용하여 훨신 간결하고 읽기 쉽게 바뀌었다.