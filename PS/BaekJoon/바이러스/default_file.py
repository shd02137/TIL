import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    n = int(l.input())
    com = int(l.input())
    com_list = []
    for _ in range(com):
        line = map(int,l.input().split())
        com_list.append([*line])
    worldmap = [[0]*(n+1) for _ in range(n+1)]
    for i,j in com_list:
        worldmap[i][j] = 1
        worldmap[j][i] = 1

    virus = -1
    queue = [1]
    visited = [1]
    while queue:
        node = queue.pop(0)
        virus += 1
        for index in range(1,n+1):
            if worldmap[node][index] == 1:
                if index not in visited:
                    queue.append(index)
                    visited.append(index)
        

    print(virus)
    

    return virus

file_paths = ["ex1.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())