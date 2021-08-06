'''
    Time Complexity : O(N)
    Space Complexity : O(1)

    Where N is the length of the array.
'''

from sys import stdin

def countOccurences(arr, n, x) :

	# Initialize a count variable
	count = 0

	# traverse in the array
	for i in range(n) :
		
		# if current element is x, increment count
		if arr[i] == x :
			count += 1

	# return count
	return count



	
n,x = map(int, input().split())
arr = list(map(int, input().strip().split(" ")))

print(countOccurences(arr, n, x))