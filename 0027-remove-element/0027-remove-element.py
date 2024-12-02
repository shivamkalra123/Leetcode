class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize the pointer for the next position to place an element
        index = 0
        
        # Iterate through the list
        for x in nums:
            if x != val:
                nums[index] = x 
                index += 1 
        
       
        return index
