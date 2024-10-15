def main():
    x=int(input('enter a number'))
    A='A'
    B='B'
    C='C'
    print('are you following?')
    print(Hanoi(x,A,B,C))

def Hanoi(n, A,B,C):
    if n==1:
        return f'{A}-{C}'
    else:
        return f'{Hanoi(n-1,A,C,B)},{A}-{C},{Hanoi(n-1,B,A,C)}'
main()