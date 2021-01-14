# 탐욕 법 / 조이스틱

## 첫번째 시도

```python
def solution(name):
    answer = 0
    num_name = make_str_to_num(name)
    

    min_move=find_min_move(num_name)
    
    return sum(num_name) + min_move

def make_str_to_num(name):
    answer =[]
    
    for str in name:
        num = min(ord(str)-ord("A"),ord("Z")-ord(str)+1)
        answer.append(num)
    
    return answer

def find_min_move(num_name):
    answer = 0
    now_index=0
    visited = [0]*len(num_name)
    visited[0] = 1
    for i,num in enumerate(num_name):
        if num == 0:
            visited[i] = 1
    count = 0
    
    while not all(visited):
        # print("="*10)
        # print("move :" ,answer)
        # print("visited : ",visited)
        # print("now_index : ",now_index)
        sameat=[]
        for i in range(1,1+len(visited)//2):
            # print("i :",i,"now",now_index)
            if visited[(now_index+i)%len(visited)] + visited[(now_index-i)%len(visited)] == 0:
                if not sameat:
                    answer += i
                    sameat.extend([(now_index+i)%len(visited),(now_index-i)%len(visited)])
                    # print("sameat : ",sameat)
                    continue
            if visited[(now_index+i)%len(visited)] == 0:
                if sameat:
                    now_index = sameat[0]
                else:
                    answer += i
                    now_index = ((now_index+i)%len(visited))%len(visited)
                visited[now_index] = 1
                sameat=[]
                break
            
            if visited[(now_index-i)%len(visited)] == 0:
                if sameat:
                    now_index = sameat[1]
                else:
                    answer += i
                    now_index = (now_index-i)%len(visited)
                visited[now_index] = 1
                sameat=[]
                break
            else:
                continue
                
        
        sameat=[]
            
#     print("move :" ,answer)
#     print("visited : ",visited)

    return answer
```

문자마다 얼마나 움직여야 최소로 움직일 수 있는지 계산을 한다.

그후 바꾸러가기위해 움직여야하는 칸중 가장 가까운 칸이 어디인지 찾아낸다.

양쪽으로 같은 거리에 위치하는 경우 다음으로 바꿔야 할 곳이 더 가까운곳으로 간다.

이렇게 해서 움직인거리와 바꾸기위해 필요한 행동횟수를 모두 더해서 결과를 구한다.

하지만 이렇게 해서 답이 거의 나온것같은데 2가지 경우에서 시간초과가 나온다. 

시간을 많이 투자했지만 결국 풀지 못했다 너무 많은 시간이 결려서 이후에 다시 보기로 한다. 



## 다른 사람의 풀이

```python

```



## 다시 풀어보기

```python

```

