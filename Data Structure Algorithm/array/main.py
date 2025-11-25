my_list = ["apple", "orange", "banana", "grape", "durian"]

# O(1) Time complexity
# 1. Accessing Array value using index
value = my_list[0]

# 2. Replace Array value using index
my_list[3] = "cherry"

# O (N) Time complexity
# 1. Tranverse to get all array value
for i in range(len(my_list)):
    print(my_list[i])

# 2. finding array value without index
def find(arr, val):
    for i in range(len(arr)):
        if my_list[i] == val:
            return(True)
        else:
            return(False)


# 3. Insertion at the Beginning/Middle
def insert_element(arr, index, element):
    """Inserts an element at a specific index by manually shifting elements."""
    
    # 1. Check if the index is valid
    if index < 0 or index > len(arr):
        print("Error: Index out of bounds.")
        return arr
    
    # 2. Add a placeholder element to increase the list size (simulates allocation)
    # This step is often handled by the runtime system.
    arr.append(None) 
    
    # 3. Core O(N) step: Shift all elements from the target index to the right.
    # If index is 0, we shift N elements.
    # The loop runs from the current end (len(arr) - 2) down to the insertion index.
    # This loop contributes the O(N) complexity.
    # 
    for i in range(len(arr) - 2, index - 1, -1):
        arr[i + 1] = arr[i] # Move element one position to the right
        
    # 4. Place the new element in the empty slot
    arr[index] = element
    
    print(f"Insertion successful at index {index}.")
    return arr

# 4. Deletion at the Beginning/Middle: O(N) (Linear Time) ---
def delete_element(arr, index):
    """Deletes an element at a specific index by manually shifting elements."""
    
    # 1. Check if the index is valid
    if index < 0 or index >= len(arr):
        print("Error: Index out of bounds.")
        return arr, None
    
    # Store the value being deleted (for return value)
    deleted_value = arr[index]
    
    # 2. Core O(N) step: Shift all elements after the target index to the left.
    # The loop runs from the index of the deleted item up to the second-to-last item.
    # This loop contributes the O(N) complexity.
    # 
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1] # Move element one position to the left (overwriting the deleted one)
        
    # 3. Reduce the array size (simulates deallocation)
    # We remove the last element, which is now a duplicate of the previous element.
    arr.pop()
    
    print(f"Deletion successful at index {index}. Value deleted: {deleted_value}")
    return arr, deleted_value

# O(log N)
# 1. Binary Search (Only works on a SORTED array)
def binary_search(arr, target):
    """Finds the target element in a SORTED array using Binary Search."""

    low = 0
    high = len(arr) - 1
    
    # 
    # The loop runs only log(N) times because 'high - low' is halved on each iteration.
    while low <= high:
        # Calculate the middle index (using integer division)
        # mid = low + (high - low) // 2 is safer for very large arrays, but (low + high) // 2 works fine here.
        mid = (low + high) // 2 
        
        # Check if target is at the middle
        if arr[mid] == target:
            return mid # Element found! O(1) inside the loop
        
        # If target is greater, discard the left half (including mid)
        elif arr[mid] < target:
            low = mid + 1 # Search only in the right half
            
        # If target is smaller, discard the right half (including mid)
        else:
            high = mid - 1 # Search only in the left half
            
    # If the loop finishes, the element was not found
    return -1 # Not found
