import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.Question import Questions


def solution(l):

    nummax = 0
    nums = []
    while 1:
        n = int(l.input())
        if n ==0:
            break
        else:
            if nummax< n:
                nummax =n
            nums.append(n)

    che = [True]*nummax

    temp_list = []

    for i in range(2,int(nummax**0.5)+1):
        if che[i] == True:
            temp_list.append(i)
            for n in range(i+i,nummax,i):
                che[n] = False


    for i in range(int(nummax**0.5)+1,nummax):
        if che[i]:
            temp_list.append(i)


    def find(n):
        for i in temp_list:
            if che[n-i]:
                print(f"{n} = {i} + {n-i}")
                return True

        print("Goldbach's conjecture is wrong.")
        return None

    for n in nums:
        find(n)

    return 0

file_paths = ["ex1.txt"]

q = Questions(file_paths)
q.solution = solution
print(q.submit())