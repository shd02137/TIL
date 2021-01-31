import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    answer = 0

    c,s = map(int,l.input().split())
    num = list(map(int,l.input().split()))

    start_point = 0
    end_point = start_point

    sum = 0
    while start_point < len(num) and end_point < len(num):
        sum += num[end_point]
        if sum == s:
            answer += 1
            sum -= num[start_point]
            start_point += 1
            end_point += 1
        elif sum > s:
            sum -= num[start_point]
            sum -= num[end_point]
            start_point += 1
        elif sum < s:
            end_point += 1



    print(answer)



    return answer


file_paths = ["ex1.txt","ex2.txt","ex3.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())