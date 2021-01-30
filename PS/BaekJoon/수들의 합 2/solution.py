import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from default.readfile import Readtxt 

r = Readtxt("ex2.txt")

print(r.lines)