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

```python
def solution(n, build_frame):
    answer = []
    
    for line in build_frame:
        x,y,build_type,action = line
        
        if action:
            build = create(x,y,build_type,answer)
            if build:
#                print("build",build)
                answer.append(build)
            
        else:
            destroy = delete(x,y,build_type,answer)
            if destroy:
#                print("destroy", destroy)
                if destroy in answer:
                    answer.remove(destroy)
        
    answer = sorted(answer , key = lambda x: (x[0],x[1],x[2]))
#    print("답", answer)
    return answer

# 0: 기둥, 1: 보 , 2 : 둘다
def create(x,y,build_type,answer):
    result = [x,y,build_type]
    # 기둥을 만들 수 있는 경우 
    # 바닥에 있는 경우 
    # 보의 한쪽 끝에 있는 경우
    # 또다른 기둥 위에 있는 경우
    
    ## 저거따지니까 머리아프다. 그냥 기둥을 못만드는 경우를 찾자.
    # 양쪽이 보 인경우
    # 바닥에 기둥이 아닌경우
    # 바닥이 아닌경우는 마지막에 따진다.
    
    ## 필드가 나눠져 있어서 머리가 더아프다 그냥 지어논 로그만 보자
    # 바닥인경우
    # 보의 한쪽 끝에 있는경우
    # 또다른 기둥 위에 있는 경우
#    print("build_check", result)
    if build_type == 0: # 기둥
#        print("stick")
        if y == 0:
            return result
        left_bo = 0
        right_bo = 0
        if [x,y,1] in answer:
            right_bo = 1
        if [x-1,y,1] in answer:
            left_bo = 1
        if right_bo + left_bo == 1:
            return result
        elif right_bo + right_bo == 0:
            if [x,y-1,0] in answer:
                return result
        return None
    # 보를 만들 수 있는 경우
    # 한쪽 끝이 기둥 위에 있는 경우
    # 양쪽 끝이 보인 경우
    else: # 보
#        print("bo")
        if [x,y-1,0] in answer or [x+1,y-1,0] in answer:
            return result
        if [x-1,y,1] in answer and [x+1,y,1] in answer:
            return result
    
    return None

def delete(x,y,build_type,answer):
    result = [x,y,build_type]
    # 지우기가 불가능한 경우
    # 내위에 기둥이 있는경우
    # 내위에 보가 있는데 양옆에 기둥이 없는 경우
#    print("delete_check", result)
    if build_type == 0: # 기둥
        if [x,y+1,0] in answer:
            return None
        left_bo = [x-1,y+1,1] in answer
        right_bo = [x,y+1,1] in answer
        if left_bo + right_bo != 2:
            if right_bo:
                if [x+1,y,0] not in answer:
                    return None
            if left_bo:
                if [x-1,y,0] not in answer:
                    return None
        
    else: # 보
        if [x,y,0] in answer or [x+1,y,0] in answer: #  내 한쪽끝 위에 기둥있는경우
            return None
        left_bo = [x-1,y,1] in answer
        if left_bo: # 내 왼쪽에 보가있는경우
#            print("check_leftbo")
            if [x-1,y-1,0] not in answer: # 왼쪽보의 왼쪽 아래에 기둥이 없는 경우
                if [x,y-1,0] not in answer: # 왼쪽보의 오른쪽 아래에 기둥이 없는 경우
                    return None
        right_bo = [x+1,y,1] in answer
        if right_bo: # 내 오른쪽에 보가 있는 경우
#            print("check_rightbo")
            if [x+2,y-1,0] not in answer:       # 오른쪽 보의 오른쪽 아래에 기둥이 없는 경우
                if[x+1,y-1,0] not in answer:    # 오른쪽 보의 왼쪽 아래에 기둥이 없는 경우
                    return None
        
#    print("ok_destroy", result)
    return result
```

시간을 많이 써가면서 다시 풀고 테스트 케이스는 다 맞았는데 제출하니까 거의 다 틀렸더라 

뭐가 문제 인지 찾아 봤지만 도저히 찾을 수 없어서 결국 다른 사람의 풀이를 찾아 보았다.



## 다른 사람의 풀이

```python
def impossible(result):
    COL, ROW = 0, 1
    for x, y, a in result:
        if a == COL: # 기둥일 때
            if y != 0 and (x, y-1, COL) not in result and \
        (x-1, y, ROW) not in result and (x, y, ROW) not in result:
                return True
        else: # 보일 때
            if (x, y-1, COL) not in result and (x+1, y-1, COL) not in result and \
        not ((x-1, y, ROW) in result and (x+1, y, ROW) in result):
                return True
    return False

def solution(n, build_frame):
    result = set()
    
    for x, y, a, build in build_frame:
        item = (x, y, a)
        if build: # 추가일 때
            result.add(item)
            if impossible(result):
                result.remove(item)
        elif item in result: # 삭제할 때
            result.remove(item)
            if impossible(result):
                result.add(item)
    answer = map(list, result)
    
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))
```

일단 지우거나 부신뒤 남은것이 규칙에 맞는지 판단하는 방법으로 풀이를 하는 것을 보았다.

한참동안 어이가 없어서 멍하고 있었다. 그리고 기둥은 보의 한쪽 끝부분에 있어야 한다는 말을 보두개의 사이에는 못들어간다고 이해를 해서 + 모양으로 만드는게 안될거라고 생각했는데 내 착각이었다.

저렇게 하면 계속해서 건물을 지었다 부셔야해서 비효율적이지 않은가 라고 생각했지만 리스트를 탐색하는 횟수를 생각하면 별로 차이가 나는것도 아니고, 코드를 짜는데 드는 비용이 훨신 적어서 이게 더 좋은 방법인것 같다.

만들거나 지울때 주변 상황을 다 생각하면서 맞는지 아닌지 판단을 하려고 했는데, 너무너무너무 복잡하더라. 그래서 결국 못맞췄고...

문제를 쉽게 풀 수 있는 방법을 찾는 요령이 부족함을 뼈저리게 실감했다.

이후 다시 풀어보자. 





## 다시 풀어보기

```python

```

