import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    answer = ""
    q = int(l.input())
    q_list = []
    for _ in range(q):
        q_list.append(list(map(int,l.input().split())))

    for line in q_list:
        x1,y1,r1,x2,y2,r2 = line
        length2 = ((x1-x2)**2+(y1-y2)**2)**0.5
        if x1==x2 and y1==y2:
            if r1==r2:
                answer += "-1\n"
            else:
                answer += "0\n"
            continue
        if r1+r2 == length2 or abs(r2-r1) == length2:
            answer += "1\n"
        elif r1+r2 > length2 > abs(r2-r1):
            answer += "2\n"
        else:
            answer += "0\n"
    answer = answer.strip()
    print(answer)
        


    return answer.strip()

file_paths = ["ex1.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())