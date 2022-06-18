# Time: O(N) Space: O(N)
def twoSum(nums, target):
	h = {}
	for i, num in enumerate(nums):
		n = target - num
		if n not in h:
			h[num] = i
		else:
			return [h[n], i]

def main():
	print(twoSum([1,2,3,4], 7))

	# This returns the indices not the values

if __name__ == "__main__":
	main()