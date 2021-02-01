import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):
    row,col = map(int,l.input().split())

    chess_map = []
    for i in range(row):
        line = list(l.input())
        chess_map.append(line)

    change_min = []
    for c in range(0,col-7):
        for r in range(0,row-7):
            a_w = 0
            a_b = 0
            for i in range(0,8):
                for j in range(0,8):
                    if i%2 == j%2:
                        if chess_map[r+i][c+j] != "W":
                            a_w += 1
                        else:
                            a_b += 1
                    else:
                        if chess_map[r+i][c+j] !="W":
                            a_b +=1
                        else:
                            a_w += 1
            change_min.append(min(a_w,a_b))

    print(min(change_min))

    return min(change_min)

file_paths = ["ex1.txt","ex2.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())