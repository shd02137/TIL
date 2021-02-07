# 연습문제 / N개의 최소공배수

## 첫번째 시도

```python
def solution(arr):
    max_num = max(arr)

    t = 2
    while 1:
        all_pass = True
        for i in arr:
            if max_num % i != 0:
                all_pass = False
                break
        if all_pass:
            return max_num
        max_num = max(arr) * t
        t+=1
            
```









---

