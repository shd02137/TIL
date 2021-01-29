# 연습문제 / JadenCase 문자열 만들기

## 첫번째 시도

```python
def solution(s):
    answer = ''
    pre = ' '
    
    for i in s:
        if pre==' ':
            answer += i.upper()
        else:
            answer += i.lower()

        pre = answer[-1]

    return answer
```

1.__단어의 첫글자를 대문자로 만들고 나머지는 소문자로 만든다.__

문제는 쉬워서 올리지 않으려고 했는데 내장함수가 새로운게 있어서 적게 되었다.



### 새로 알게된점

> string.title()이라는 내장함수가 존재한다.
>
> 이 내장함수는 앞자리를 대문자로 해준다.



---

