class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict={}
        for i,n in enumerate(nums):
            if n in nums_dict:
                dif=(i-nums_dict[n])
                if dif<=k:
                    return True
            nums_dict[n]=i
        return False
