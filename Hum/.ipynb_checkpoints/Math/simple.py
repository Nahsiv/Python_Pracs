def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b 
if __name__=='__main__':
    print('hello')
    a, b = map(int, input().split(" "))
    print(add(a,b))