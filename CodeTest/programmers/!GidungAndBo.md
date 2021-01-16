# 2019 카카오 블라인드코테 / 기둥과 보

## 첫번째 시도

```python
#34
def solution(n, build_frame):
    answer = [[]]
    field = [[-1]*n for _ in range(n)] # 0 :없음, 1: 보, 2: 기둥 3: 둘다
    
    for action in build_frame:
        x,y,frame_type,create= action[0],action[1],action[2],action[3]
        print(x,y,frame_type,create)
        
        if create: #생성
            if frame_type: # 보
                if field[x][y-1] == 2 or field[x+1][y-1] ==2:
                    if field[x][y] == 2:
                        field[x][y] = 3
                    else:
                        field[x][y] = 1
                elif x >= 1:
                    if field[x-1][y] == 1 and field[x+1][y] == 1:
                        if field[x][y] == 2:
                            field[x][y] = 3
                        else:
                            field[x][y] = 1
            else: # 기둥
                if y == 0:
                    if field[x][y] == 1:
                        field[x][y] = 3
                    else:
                        field[x][y] = 2
                elif field[x][y-1] == 2:
                    if field[x][y] == 1:
                        field[x][y] = 3
                    else:
                        field[x][y] = 2
                elif x >= 1:
                    if field[x-1][y] == 1 ^ field[x][y] == 1:
                        if field[x][y] == 1:
                            field[x][y] = 3
                        else:
                            field[x][y] = 2
        else: # 삭제 # 0 :없음, 1: 보, 2: 기둥 3: 둘다

            
            if frame_type: # 보
                if field[x][y] == 2:
                    pass
                
                pass
            else: # 기둥
                
                
                pass
            
            
            
    return answer
```

가능한 경우를 모두 생각해서 하나씩 추가해주었다.

문제를 풀이하다가 중간에 기둥과 보가 함께 있을 수 있다는걸 알아내고,
한참동안 생각을 다시하다가 이렇게 다 생각하는 경우는 아닌거 같아서 다시하기로 마음먹고 초기화 했다.



## 다른 사람의 풀이

```python

```



## 다시 풀어보기

```python

```

