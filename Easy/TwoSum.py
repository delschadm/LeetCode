
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. 暴力法
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # 2. 两遍哈希表
        # hash_table = {}
        # for i in range(len(nums)):
        #     hash_table[nums[i]] = i
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hash_table and hash_table[complement] != i:
        #         return [i, hash_table[complement]]

        # 3. 一遍哈希表
        hash_table = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))

