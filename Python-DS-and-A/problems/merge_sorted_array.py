def merge(nums1, m, nums2, n) -> None:
	# Make a copy of the first m elements of nums1.
	nums1_copy = nums1[:m] 
	
	# Read pointers for nums1Copy and nums2 respectively.
	p1 = 0
	p2 = 0
	
	# Compare elements from nums1Copy and nums2 and write the smallest to nums1.
	for p in range(n + m):
		# We also need to ensure that p1 and p2 aren't over the boundaries
		# of their respective arrays.
		if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
			nums1[p] = nums1_copy[p1] 
			p1 += 1
		else:
			if len(nums1) < p:
				nums1[p] = nums2[p2]
				p2 += 1
			else:
				nums1.append(nums2[p2])
				p2 += 1

	return nums1

def main():
	print(merge([1,2,5,7], 4, [1,3,4,6], 4))

if __name__ == "__main__":
	main()