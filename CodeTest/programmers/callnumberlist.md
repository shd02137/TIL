# 해시 / 전화번호 목록

## 첫 번째 시도
```python
def solution(phone_book):
    answer = True
    phone_book.sort()
    sortPhoneBook = sorted(phone_book)
    for i in range(0,len(sortPhoneBook)-2):
        if sortPhoneBook[i] in sortPhoneBook[i+1] :
            return False;

    return answer
```

해시 없이 소트를 이용하고 앞 문자열과 뒷문자열을 비교하여 시작부분이 겹치는 지 활용했다.
소트를 이용해 문제를 풀어서 속도가 느리다. 또한 문제의 주어진 조건인 해시를 이용하지 못했다.
(해시를 어떻게 사용해야 하는지를 몰랐다.)

또한 앞 전화번호가 꼭 중간부터 겹치는 특수한 경우에는 오류가 날 가능성이 있을 것이라고 예상한다.

112 1112 같은 경우



## 다른 사람의 풀이
```python
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
```

파이선에서 딕셔너리는 해시로 구현되어있다. 이것을 이용한다.

전화 번호를 해시 키로 이용하였고 해시 값으로 해당 번호의 유무를 True/False로 구분하였다.