
cube = lambda x: x**3 

def fibonacci(n):
    result=[0,1]
    [result.append(result[i-2]+result[i-1]) for i in range(2,n)]
    return result[0:n]



if __name__ == '__main__':
