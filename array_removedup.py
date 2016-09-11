class Solution():
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        j = 0
        for i in range(0, len(A)):
            if A[i] != A[j]:
                A[i], A[j+1] = A[j+1], A[i]
                j = j + 1
        return j+1



myList=[1,2,2,3,3,4,5,6]
result=Solution()
print(result.removeDuplicates(myList))

#how to print out the output array
