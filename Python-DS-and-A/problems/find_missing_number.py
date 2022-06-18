"""
You are given an array of positive numbers from 1 to n, such that all numbers from 1 to n are present except one number x.
You have to find x. The input array is not sorted. Look at the below array and give it a try before checking the solution.
"""
# Time complexity: Linear, O(n)
# Space complexity: Constant, O(1)

def find_missing(input):
	# calculate sum of all elements 
	# in input list
	sum_of_elements = sum(input)
	
	# There is exactly 1 number missing 
	n = len(input) + 1
	actual_sum = (n * ( n + 1 ) ) / 2
	return actual_sum - sum_of_elements

def main():
	input = [3,7,1,2,8,4,5]
	print(find_missing(input))

if __name__ == "__main__":
    main()