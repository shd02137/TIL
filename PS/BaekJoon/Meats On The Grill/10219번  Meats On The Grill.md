# 10219번 / Meats On The Grill

## 첫번째 풀이

```python
answer = ""
n = int(input())
for _ in range(n):
    row, col = input().split()
    row, col = int(row),int(col)

    for _ in range(row):
        r = input()
        answer += (r[::-1] + "\n")
        
answer.strip()
    
print(answer)
```

1. __맵 전체를 뒤집는다.__



처음에는 알파벳으로 나눠진 고기조각을 하나씩 하나씩 찾아서 남는 자리에 넣으려고 했는데,

너무 구현하기가 어려웠다. 이렇게 한참을 고민하다가 나온답이 판을 그냥 뒤집으면 답이 나왔다.

와.....



---

