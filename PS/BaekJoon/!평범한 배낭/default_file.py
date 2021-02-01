import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    answer = 0
    n,k= map(int,l.input().split())
    stuffs = []
    for _ in range(n):
        w, h  = map(int,l.input().split())
        stuffs.append([w,h])
    print(n,k)
    print(stuffs)
    

    return answer

file_paths = ["ex1.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())