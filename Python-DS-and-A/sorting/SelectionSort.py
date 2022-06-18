# Python program for implementation of Selection
# Sort
import sys

def selection_sort(a):
	# Traverse through all array elements
	for i in range(len(a)):
		# Find the minimum element in remaining
		# unsorted array
		min_idx = i
		for j in range(i+1, len(a)):
			if a[min_idx] > a[j]:
				min_idx = j

		# Swap the found minimum element with
		# the first element  
		a[i], a[min_idx] = a[min_idx], a[i]

def main():		
	A = [64, 25, 12, 22, 11]
	selection_sort(A)
	print(A)

if __name__ == "__main__":
    main()