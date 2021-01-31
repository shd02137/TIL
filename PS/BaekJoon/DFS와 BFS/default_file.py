import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    answer = ""
    n,e,start = map(int,l.input().split())
    search_map = [[0]*(n+1) for _ in range(n+1)]
    for _ in range(e):
        i,j = map(int,l.input().split())
        search_map[i][j] = 1
        search_map[j][i] = 1

    dfs_visited = [0]*(n+1)

    def dfs(start,visited):
        result = str(start)+" "
        visited[start] = 1
        for index,value in enumerate(search_map[start]):
            if value == 1 and visited[index] == 0:
                visited[index] = 1
                result += dfs(index,visited)
        return result  
    answer += dfs(start,dfs_visited).strip()+"\n"

    bfs_visited = [0] * (n+1)
    bfs_visited[start] = 1
    bfs_queue = [start]
    while bfs_queue:
        nd = bfs_queue.pop(0)
        answer += str(nd) + " "
        for index,node in enumerate(search_map[nd]):
            if node == 1 and bfs_visited[index] == 0:
                bfs_queue.append(index)
                bfs_visited[index] = 1


    answer = answer.strip()

    print(answer)
    return answer

file_paths = ["ex1.txt","ex2.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())