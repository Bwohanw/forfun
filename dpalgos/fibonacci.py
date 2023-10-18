'''Calculates the nth fibonacci number using a dynamic programming algorithm

Runtime: O(n) since it loops once through a list of size n
'''

def fib(n):
    fibs = [0]*(n+1)
    fibs[1] = 1
    for i in range(2, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2]
    return fibs[n]

n = (int)(input("enter a number: "))
print(fib(n))