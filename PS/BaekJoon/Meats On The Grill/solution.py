import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    answer = ""
    n = int(l.input())
    for _ in range(n):
        row, col = l.input().split()
        row, col = int(row),int(col)

        for _ in range(row):
            r = l.input()
            answer += (r[::-1] + "\n")
            
    answer.strip()
        

    return answer

file_paths = ["ex1.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())