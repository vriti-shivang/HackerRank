if __name__ == '__main__':
    n = int(input())
    
    integer_list = list(map(int, input().split()))
    if len(integer_list) == n:
        integer_list = tuple(integer_list)
        print(hash(integer_list))
