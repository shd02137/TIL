# 스택 & 큐/ 다리를지나는트럭

## 첫번째 시도

```python
def solution(bridge_length, weight, truck_weights):
    answer = 0
    time=0
    bridge_sum=0
    bridge_out = []
    bridge_on = []
    total_car = len(truck_weights)

    while total_car>0:
        time += 1
        if len(bridge_out)!=0:
            if bridge_out[0] == time:
                bridge_sum -= bridge_on[0]
                bridge_out.pop(0)
                bridge_on.pop(0)
                total_car -= 1

        if len(truck_weights)!=0:
            if bridge_sum + truck_weights[0] <= weight:
                bridge_sum += truck_weights[0]
                bridge_out.append(time+bridge_length)
                bridge_on.append(truck_weights[0])
                truck_weights.pop(0)



    return time
```





## 다른 사람의 풀이

```

```







## 다시 풀어보기



```python

```

