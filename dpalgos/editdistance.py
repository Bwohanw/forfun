'''
Another problem talked about in CS374
Problem statement: Suppose you had 2 strings A and B (lengths m and n)
What is the minimum required number of edits you need to turn string A into string B?
An edit is either an insertion of a new character, a deletion of an existing character, or
a replacement of an existing character with a different character
For example:
A = dog
B = hose
One way to turn dog into hose would be:
replace d with h
replace g with s
insert e at the end
'''


'''Strategy:
We wish to first develop a recursive definition for our problem. Let editDistance(i,j) be the minimum number of 
edits required to transform A[1,...,i] into B[1,...,j]

We can define editDistance(i,j) recursively as follows:

editDistance(i,j) = {i if j = 0
                    j if i = 0
                    
                    min(editDistance(i,j-1) + 1, editDistance(i-1,j) + 1, editDistance(i-1,j-1) + (1 if A[i] != B[j], and 0 if A[i] = B[j]))}

The intuition is that if j is 0, we know the rest of the edits have to be deletions. If i is 0, the rest of the edits have
to be insertions. Otherwise, we can either perform:
1. an insertion, represented by the (i,j-1) case (we match the jth character of B with an insert in A),
2. a deletion, represented by the (i-1,j) case (we delete the ith character)
3. a replacement, represented by the (i-1,j-1) case (we have to add 0 or 1 depending on if we need to replace or if they're already the same)


We can memoize this recurrence as a 2D array, where each entry (i,j) relies on its left element, above element, and diagonal up left element.

Runtime: O(m*n)
'''

A = input("enter the string A: ")
B = input("enter the string B: ")


def editDistance():
    distance = []
    for i in range(len(A)+1):
        distance.append([0] * (len(B)+1))
    for i in range(len(A) + 1):
        distance[i][0] = i
    for j in range(len(B) + 1):
        distance[0][j] = j
    for i in range(1, len(A)+1):
        for j in range(1, len(B) + 1):
            insert = distance[i-1][j] + 1
            delete = distance[i][j-1] + 1
            repl = distance[i-1][j-1]
            if (A[i-1] != B[j-1]):#minus 1 because we're 1-indexing in the array, but 0-indexing in the string
                repl += 1
            distance[i][j] = min(insert, min(delete, repl))
    return distance[len(A)][len(B)]#get the element at the actual lengths of the string because it's 1-indexed

print(editDistance())