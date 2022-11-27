def partition(array, low, high):
	pivot = array[high] # choose the rightmost element as pivot

	i = low - 1 # pointer for greater element

	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])

	(array[i + 1], array[high]) = (array[high], array[i + 1]) # Swap the pivot element with the greater element specified by i

	return i + 1 # Return the position from where partition is done

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)

		quickSort(array, low, pi - 1) #left

		quickSort(array, pi + 1, high) #right

data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)