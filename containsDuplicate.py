# Exaple 1: 
# num = [1,2,3,4] 
# Output for Example 1: True
# Example 2:
num = [1, 2, 3, 4]
# Output for Example 2: False

class containsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
    
out = containsDuplicate()
print(out.containsDuplicate(num))  
