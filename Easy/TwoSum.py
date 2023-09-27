
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [nums.index(target - n), i] if target - n in nums else None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))

