# Merge Sort code in Python

def merge_sort(NumberList):
	"""
	Merge sort code to sort Number List
	Call this code like - merge_sort([34,12,78,90,24,67])
	"""
	length = len(NumberList)
	if length > 1:
		midpoint = length // 2
		left_half = merge_sort(NumberList[:midpoint])
		right_half = merge_sort(NumberList[midpoint:])
		i = 0
		j = 0
		k = 0
		left_length = len(left_half)
		right_length = len(right_half)
		while i < left_length and j < right_length:
			if left_half[i] < right_half[j]:
				NumberList[k] = left_half[i]
				i += 1
			else:
				NumberList[k] = right_half[j]
				j += 1
			k += 1
			
		while i < left_length:
			NumberList[k] = left_half[i]
			i += 1
			k += 1
		
		while j < right_length:
			NumberList[k] = right_half[j]
			j += 1
			k += 1
			
	return NumberList

if __name__ == '__main__':
	try:
		raw_input
	except NameError:
		raw_input = input
		
	user_input = raw_input('Enter numbers separated by comma:\n').strip()
	unsorted = [int(item) for item in user_input.split(',')]
	print(merge_sort(unsorted))
