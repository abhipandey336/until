def subArraySum(arr, n, sum):
	l=list()
	for i in range(n):
		curr_sum = arr[i]
		j = i+1
		while j <= n:
			if curr_sum == sum:
				for k in range(i,j):