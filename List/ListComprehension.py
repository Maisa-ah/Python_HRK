from itertools import permutations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i,k,j] for i in range(x+1) for k in range(y+1) for j in range(z+1) if (i+k+j)!=n])