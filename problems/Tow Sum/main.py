class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {value: index for index, value in enumerate(nums)}
        for index, value in enumerate(nums):
            if target - value in hash_map and hash_map[target - value] != index:
                return [index, hash_map[target - value]]



solution = Solution()

print(solution.twoSum(nums=[3,2,4], target=6))
