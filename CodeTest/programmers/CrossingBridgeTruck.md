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

```python
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count
```

방법은 유사하지만 클래스를 사용해서 문제를 해결한것을 확인할 수 있었다.





## 다시 풀어보기

```python
def solution(bridge_length, weight, truck_weights):
    time = 0
    on_bridge = []
    on_bridge_weights = 0
    
    while truck_weights:
        if on_bridge:
            if on_bridge[0][1] == time:
                on_bridge_weights -= on_bridge[0][0]
                on_bridge=on_bridge[1:]
        
        if truck_weights[0] + on_bridge_weights <= weight:
            on_bridge_weights +=truck_weights[0]
            on_bridge.append([truck_weights[0],time+bridge_length])
            truck_weights=truck_weights[1:]
        time += 1
        #print(time , "=" , on_bridge, ",",on_bridge_weights)
        
    return time+bridge_length
```

pop(0)을 사용하지 않은것을 제외하면 방법은 달라지지 않았다. 

약간 코드가 정리되었다.

