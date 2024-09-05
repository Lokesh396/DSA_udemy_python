# Quicksort implementation using Lomuto Partition.

class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)

    def partition(self, arr, low, high):
        # code here
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


sol = Solution()
arr = [1, 4, 3, 2, 10, 8, 6]
sol.quickSort(arr, 0, 6)
print(arr)


# QuickSort implementation using Hoare Partition

class Solution1:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1

            j -= 1
            while arr[j] > pivot:
                j -= 1

            if i >= j:
                return j
            arr[i], arr[j] = arr[j], arr[i]
        



sol1 = Solution1()
arr1 = [1, 4, 3, 2, 10, 8, 6]
sol.quickSort(arr1, 0, 6)
print(arr1)
