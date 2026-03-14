class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS=len(matrix),len(matrix[0])
        l,r=0,ROWS-1
        while l<=r:
            mid=(l+r)//2
            if target>matrix[mid][-1]:
                l=mid+1
            elif target<matrix[mid][0]:
                r=mid-1
            else:
                break
        if not (l<=r):
            return False
        mid=(l+r)//2
        a,b=0,COLS-1
        while a<=b:
            m=(a+b)//2
            if target<matrix[mid][m]:
                b=m-1
            if target>matrix[mid][m]:
                a=m+1
            if target==matrix[mid][m]:
                return True
        return False


