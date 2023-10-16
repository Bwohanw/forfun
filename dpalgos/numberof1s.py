'''
DP algorithm from CS374
The problem: A basic arithmetic expression is composed of characters from the set {1, +, x} and
parentheses. Almost every integer can be represented by more than one basic arithmetic
expression.
For example, an expression to represent the number 6: 1+1+1+1+1+1
Another expression for 6: (1+1+1)x(1+1)
Describe and analyze an algorithm to compute, given an integer n as input, the minimum
number of 1's in a basic arithmetic expression whose value is equal to n. The number
of parentheses doesn't matter, just the number of 1's.
'''


'''Strategy:
Let minOnes(n) be the minimum number of 1s needed to represent n as a basic arithmetic expression.
Express minOnes(n) as a recurrence relation as follows:

minOnes(n) = {  1 if n=1
                min[min(minOnes(a)+minOnes(b))] over all a and b such that a*b=n, or a+b=n otherwise
                }
'''



def minOnes(n):
    elements = [0] * (n+1) #to make 1-based indexing possible
    elements[1] = 1
    for i in range(2,n+1):
        minelements = i #you can always upper bound the number of elements needed by element i with i 1s and adding them all.
        for j in range(1,i):#don't include i
            if ((elements[j] + elements[i-j]) < minelements):
                minelements = elements[j] + elements[i-j]
            if (i%j == 0 and j != 1):#we don't want to have j be 1 since we're doing multiplication
                if ((elements[j] + elements[i//j]) < minelements):
                    minelements = elements[j] + elements[i//j]
        elements[i] = minelements
    return elements[n]

#print(minOnes((int)(input("enter a number: "))))

print(minOnes(20000))

'''
The runtime for this algorithm is O(n^2), since you loop through elements which has n elements,
and you look through all possible combinations of a and b that either add or multiply to the number you're looking at,
which can be done in O(n) time.'''