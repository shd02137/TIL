import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    answer = 0
    

    return answer

file_paths = ["ex1.txt","ex2.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())