# Given an array of  distinct integers, transform the array into a zig zag sequence by permuting the array elements. 
# A sequence will be called a zig zag sequence if the first  elements in the sequence are in increasing order and 
# the last elements are in decreasing order, where . You need to find the lexicographically smallest zig zag sequence of the given array.



def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) -1
    
    median = max(a)
    first = a[0:mid]
    second = a[mid+1::]
    second = a[mid:n-1]
    second = second[::-1]
    first.append(median)
    res = first + second
    return print(*res)

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
