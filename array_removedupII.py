class Solution:
    # @param A a list of integers
    # @return an integer
    # @it's a good solution!

    def removeDuplicates(self, A):
        if len(A) <= 2:
            return len(A)
        prev = 1
        curr = 2
        while curr < len(A):
            if A[curr] == A[prev] and A[curr] == A[prev - 1]:
                curr += 1
            else:
                prev += 1
                A[prev] = A[curr]
                curr += 1
        return prev + 1


myList=[1,2,2,2,3,3,4,4,5,6]
result=Solution()
print(result.removeDuplicates(myList))

#how to output array
#I feel this solution is not good, should record the number count instead
