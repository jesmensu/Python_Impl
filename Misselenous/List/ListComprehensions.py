if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #result = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if (a+b+c != n)]
    A=[]
    result=[]
    for a in range(x+1):
         for b in range(y+1):
             for c in range(z+1):
                A.append(a)
                A.append(b)
                A.append(c)
                
                if (a+b+c != n):
                    result.append(A)
                A = []
    print(result)
