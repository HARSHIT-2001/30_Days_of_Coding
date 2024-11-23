# Function to return the minimum number of swaps to create a beautiful array(Ascending/Descending sorted).
# This problem is solved in Time complexity O(n log n) and Space complexity O(n).

def min_swaps_to_beautiful_array(n, arr):
    def count_swaps(arr, order):
        swaps = 0
        indices = sorted(range(len(arr)), key=lambda k: arr[k], reverse=order)
        visited = [False] * len(arr)

        for i in range(len(arr)):
            if visited[i] or indices[i] == i:
                continue

            cycle_size = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = indices[j]
                cycle_size += 1

            if cycle_size > 0:
                swaps += (cycle_size - 1)

        return swaps

    ascending_swaps = count_swaps(arr, False)
    descending_swaps = count_swaps(arr, True)

    return min(ascending_swaps, descending_swaps)

# Input handling
n1 = int(input("Enter array size: "))   # e.g., 5
ary = input("Enter array elements separated by spaces: ")  # e.g., "4 5 3 2 1"
arr1 = list(map(int, ary.strip().split()))  # Convert to integer list

result1 = min_swaps_to_beautiful_array(n1, arr1)
print(result1)  
