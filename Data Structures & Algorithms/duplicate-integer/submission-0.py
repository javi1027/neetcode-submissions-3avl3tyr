class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        new = []

        for num in nums: 
            if num not in new:
                new.append(num)
            
            else:
                return True
        
        return False

        