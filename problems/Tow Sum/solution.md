

```python
list = [1,5,7,9,10,11,3,4]
target = 7
# solution : list[2] + list[3]
```

The intuitive solution is to for loop twice on the array which you will have the target then just you will take each number and then add up to every number in the array then the next one etc..
```python
def tow_sum(nums, target):
	for i in nums:
		for j in nums :
			if j+i == target:
			return nums.index(i),nums.index(j)
```

This is the brute force way , pretty easy right? but this takes O(n^2)

So we will notice that if you substract the number from the target you will find the other number , but you have just to check if it's in the list or not
so we will convert the list to Hash map because searching in hash map is O(1)
```python
def twoSum(self, nums: list[int], target: int) -> list[int]:
	hash_map = {value: index for index, value in enumerate(nums)}
	for index, value in enumerate(nums):
		if target - value in hash_map and hash_map[target - value] != index:
			return [index, hash_map[target - value]]
```
