# 탐욕법 / 큰수만들기

## 첫번째 시도

```python
# 첫번째에는 못풀고 풀이를 보고 넘어갔었다.
```

문제는 이해했지만 알고리즘으로 정리하지 못해서 다른사람의 풀이를 보고 공부했다.



## 다른 사람의 풀이

```python

```





## 다시 풀어보기

```python
def solution(number, k):
    answer = ''

    while k:
        if len(number) == 0:
            return answer[:-k]
        answer += number[0]
        number = number[1:]
        while len(answer)> 1:
            if answer[-1] > answer[-2]:
                answer = answer[:-2] + answer[-1]
                k -= 1
            else:
                break
            if k ==0:
                break

    
    return answer+number
```

테스트 케이스 10 번에서 시간이 미친듯이 길어졌다.
아마 문자열의 마지막 쯤에서 큰수가 나와서 앞의 숫자를 모두 없애는 일을 많이 반복한것이라고 추측된다.