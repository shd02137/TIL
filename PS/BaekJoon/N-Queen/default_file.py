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