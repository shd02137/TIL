import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


from default.Question import Question

file_path = "ex1.txt"

def solution():
    answer = 0


    return answer


q = Question(file_path)
q.solution = solution
print(q.submit())