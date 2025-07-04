num = [1,2,3,1]

class containsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        """
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
