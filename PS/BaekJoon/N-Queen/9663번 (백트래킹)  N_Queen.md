# 9663번 (백트래킹) / N_Queen

# 첫 풀이

```python
answer = 0
n=int(input())
chess_map = [[0]*n for _ in range(n)]

def now_chess(chess_map,index,i):
    new_map = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            new_map[a][b] = chess_map[a][b]

    total = 0
    
    if new_map[i][index] == 1:
        return 0
    else:
        for a in range(n):
            new_map[i][a] = 1
            new_map[a][index] = 1
            if i-a>=0 and index-a>0:
                new_map[i-a][index-a] = 1
            if i-a>=0 and index+a<n:
                new_map[i-a][index+a] = 1
            if i+a<n and index-a>=0:
                new_map[i+a][index-a] = 1
            if i+a<n and index+a<n:
                new_map[i+a][index+a] = 1

    for m in range(n):
        if i+1 == n:
            return 1
        total += now_chess(new_map,m,i+1)
        
    return total

for m in range(n):
    answer += now_chess(chess_map,m,0)

print(answer)

```





```python
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions

count = 1
def solution(l):
    answer = 0
    n=int(l.input())
    chess_queen = []
    def now_chess(index,i):

        total = 0

        for a in range(n):
            if [i,a] in chess_queen:
                return 0
            if [a,index] in chess_queen:
                return 0
            if i-a>=0 and index-a>=0:
                if [i-a,index-a] in chess_queen:
                    return 0
            if i-a>=0 and index+a<n:
                if [i-a,index+a] in chess_queen:
                    return 0
            if i+a<n and index-a>=0:
                if [i+a,index-a] in chess_queen:
                    return 0
            if i+a<n and index+a<n:
                if [i+a,index+a] in chess_queen:
                    return 0

        chess_queen.append([i,index])

        for m in range(n):
            if i+1 == n:
                return 1
            total += now_chess(m,i+1)
            while len(chess_queen) > i+1:
                chess_queen.pop()
            
        return total

    for m in range(n):
        answer += now_chess(m,0)
        chess_queen.pop()
    print(answer)

    return answer

file_paths = ["ex1.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())

```



최근 백준 문제를 풀면서 얼마나 비효율적인 코드를 짜고있었는지 실감하고있다.

시간초과가 도저히 해결이 안된다.

찾고나서는 아차싶은데 찾기전에는 뭐가 문제인지 찾기가 너무힘들다.