# 2018 카카오 블라코테 / N진수 게임

## 첫번째 풀이

```python
def solution(n, t, m, p):
    answer = '0'  
    i = 0
    while len(answer) <= m*t:
        answer += convert_int(i,n)
        i+=1
        
    result = ""
    for i in range(t):
        result += answer[p-1+i*m]
    return result


def convert_int(value,n):
    answer = ""
    while value != 0:
        if value%n >= 10:
            temp = chr(value%n+55)
        else:
            temp = str(value%n)
        answer = temp +answer
        value = value//n
    return answer
```

1. __게임데 참여하는 인원과 미리 구하려고 하는 숫자에 맞게 진수변환을 한 수를 사용하기에 충분한 길이가 될때까지 전부 구한다.__
2. __구해놓은 진수 변환을 한 수에서 내가 말해야할 숫자를 찾아서 답을 찾는다.__



문제를 풀이하면서 게임에 참여하는 인원과 미리 구할 숫자를 이용해 진수 변환을 한 수를 사용하기에 충분한 길이가 될때까지 전부 구했다.

이후에 미리 구해놓은 진수 변환을 한 숫자에서 내가 말해야할 숫자를 찾아서 답을 만들었다.



### 새로 알게된 점

이 문제를 풀면서 잘못알고있던 int()의 사용법을 알게되었다.

>`int(3,2)`를 십진법의 숫자 3을 2진법으로 변환한다라고 생각을 했는데,
>
>`int("0b11",2)`처럼 이진법 숫자 11을 십진법으로 사용하는 것이었다.

