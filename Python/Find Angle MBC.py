# Enter your code here. Read input from STDIN. Print output to STDOUT

from cmath import *
a = int(input())
b = int(input())
print(str(int(round((phase(complex(b / 2, a / 2)) * 180) / 3.1415, 0)))+'°')
