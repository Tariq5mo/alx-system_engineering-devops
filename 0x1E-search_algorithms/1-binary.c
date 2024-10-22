#include "search_algos.h"

/**
 * print_c_arr - print the array being searched every time it changes.
 *
 * @arr: is a pointer to the first element of the original array.
 * @l: The first index the printing begins with.
 * @h: The last index the printing ends with.
 */
void print_c_arr(int *arr, int l, int h)
{
	int i;

	printf("Searching in array: %d", arr[l]);
	for (i = l + 1; i <= h; i++)
	{
		printf(", %d", arr[i]);
	}
	printf("\n");
}
/**
 * binary_search - function that searches for a value in a sorted array
 * of integers using the Binary search algorithm
 * @array: is a pointer to the first element of the array to search in.
 * @size: is the number of elements in array.
 * @value: is the value to search for
 * Return: return the index where value is located, If value is not present
 * in array or if array is NULL, your function must return -1
 */
int binary_search(int *array, size_t size, int value)
{
	int mid, l, h;

	if (!array)
		return (-1);
	l = 0;
	h = size - 1;
	for (mid = (h + l) / 2; h >= l; mid = (h + l) / 2)
	{
		print_c_arr(array, l, h);
		if (array[mid] == value)
			return (mid);
		if (array[mid] > value)
			h = mid - 1;
		else
			l = mid + 1;
	}
	return (-1);
}
