class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count_val = 0
        idx = 0

        while idx < len(nums) - count_val:
            if nums[idx] == val:
                try:
                    while nums[-1 - count_val] == val:
                        count_val += 1

                    if len(nums) -1 - count_val > idx:
                        nums[idx], nums[-1 - count_val] = nums[-1 - count_val], nums[idx]
                        count_val += 1
                    else:
                        break
                except:
                    return 0
            idx += 1
            
        return idx