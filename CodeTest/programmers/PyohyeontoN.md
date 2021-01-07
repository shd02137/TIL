# 동적계획법 / N으로 표현

## 첫번째 시도

```python
def sol(number,number_list,answer):
    if answer <5:
        1
        print("%d" %answer + str(number_list))
    if answer > 8:
        return -1
    if number in number_list:
        return answer
    else:
        temp_list = []
        for i in number_list:
            temp_list.append(i + number_list[0])
            temp_list.append(i - number_list[0])
            temp_list.append(i * number_list[0])
            temp_list.append(i // number_list[0])
            temp_list.append(i*10 + number_list[0])
        for i in temp_list:
            if i >= 1 and i <= 32000 and i not in number_list:
                number_list.append(i)
        answer = sol(number,number_list,answer + 1)
    return answer

def solution(N, number):
    N = 4
    number = 17
    answer = 1
    number_list = []
    number_list.append(N)
    print(number_list)
    answer = sol(number,number_list,answer);
    return answer
```

결국 못풀고 이후 다시 시도하기로 했다.

```
def solution(N, number):
    makableNumber = [[N],[N*10+N,N+N,N-N,N*N,N//N]]
    #print(makableNumber)
    
    if N == number:
        return 1
    
    count = 2
    while number not in makableNumber[-1]:
        WillAddMakableNumber = [makableNumber[-1][0]*10+N]
        tempNumberList = CalcList(makableNumber)
        WillAddMakableNumber += list(set(tempNumberList))
        #print(tempNumberList,end="\n================\n")
        makableNumber.append(WillAddMakableNumber)
        
        if count > 8:
            return -1
        else:
            count += 1
    for i in makableNumber:
        #print(i)
        pass
    return count

def CalcList(list):
    tempList = []
    for i in range((len(list)+1)//2):
        for value1 in list[i]:
            for value2 in list[-1+i]:
                tempList += CalcNumber(value1,value2)
    return tempList
    
def CalcNumber(a,b):
    tempList = [a+b,a-b,a*b,b+a,b-a,b*a]
    if b!=0:
        tempList.append(a//b)
    if a!=0:
        tempList.append(b//a)
    return tempList
```

이후 다시 풀었으나 반절만 맞았다.
계산할때 일부 계산이 누락되는것을 확인 했지만 왜 계산을 안하는지 정말 한참을 고민했고 그 결과 답을 찾아내었다.

```
def solution(N, number):
    makableNumber = [[N]]
    
    if N == number:
        return 1
    
    count = 1
    while number not in makableNumber[-1]:
        WillAddMakableNumber = [makableNumber[-1][0]*10+N]
        tempNumberList = CalcList(makableNumber)
        WillAddMakableNumber += list(set(tempNumberList))
        makableNumber.append(WillAddMakableNumber)

        if count > 8:
            return -1
        else:
            count += 1
            
    return count 

def CalcList(list):
    tempList = []
    for i in range((len(list)+1)//2):
        for value1 in list[i]:
            for value2 in list[-1-i]:
                tempList += CalcNumber(value1,value2)
    return tempList
    
def CalcNumber(a,b):
    tempList = [a+b,a-b,a*b,b-a]
    if b!=0:
        tempList.append(a//b)
    if a!=0:
        tempList.append(b//a)
    return tempList
```

잘못된 이유는 계산 실수였는데, ` for value2 in list[-1-i]: `로 써야하는걸 ` for value2 in list[-1+i]  ` 로 착각하여 벌어진 실수였다.

## 다른 사람의 풀이

```python
def solution(N, number):
    S = [{N}]
    for i in range(2, 9):
        lst = [int(str(N)*i)]
        for X_i in range(0, int(i / 2)):
            for x in S[X_i]:
                for y in S[i - X_i - 2]:
                    lst.append(x + y)
                    lst.append(x - y)
                    lst.append(y - x)
                    lst.append(x * y)
                    if x != 0: lst.append(y // x)
                    if y != 0: lst.append(x // y)
        if number in set(lst):
            return i
        S.append(lst)
    return -1
```

전체적인 방법은 같지만 코드가 훨신 깔끔하고 보기 좋다.
같은 숫자가 붙어있는 555 같은 숫자는 문자열으로 간단하게 해결하는등 가독성이 훨신 좋다.



## 다시 풀어보기

```python

```

