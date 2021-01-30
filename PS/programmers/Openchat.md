# 2019 카카오블라인드 코테 / 오픈 채팅방

## 첫번째 시도

```python
def solution(record):
    answer = []
    result = []
    for line in record:
        result.append(line.split())
    id_dict = dict()
    for line in result:
        if len(line) == 3:
            action,user_id,name = line[0],line[1],line[2]
        else:
            continue
        if action == "Enter":
            id_dict[user_id] = name
                
        elif action == "Change":
            id_dict[user_id] = name
            
            
    for line in result:
        action,user_id = line[0],line[1]
        if action == "Enter":
            answer.append(f"{id_dict[user_id]}님이 들어왔습니다.")
        elif action == "Leave":
            answer.append(f"{id_dict[user_id]}님이 나갔습니다.")

    
    return answer
```

처음에 생각했을때에는 뒤에서 부터 읽어주면 change하기 전에 존재하는 id를 신경 쓰지 않아도 되서 뒤에서읽고 답을 만들려고했었다. 하지만 아이디를 바꾼적 없이 들어오고 바로 나간사람의 경우에는 이름을 알 수 없는 문제가 생겨서 방향을 바꿔서 처음부터 순서대로 읽고 답을 만들었다.

우선 처음에 들어오면 딕셔너리를 만들어서 아이디와 이름을 매칭시켜준다. 
딕셔너리가 완성된뒤 채팅 내용을 보면서 들어오고 나간 기록을 답으로 넣어 주어서 풀었다.



## 다른 사람의 풀이

```python

```

크게 다르게 푼사람이 보이지 않는다.



## 다시 풀어보기

```python

```

