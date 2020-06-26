for _ in range(int(input())):
    a,A=int(input()),set(map(int,input().split()))
    b,B=int(input()),set(map(int,input().split()))
    if B==B.union(A):
        print(True)
    else:
        print(False)
