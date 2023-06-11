from typing import List, Tuple
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    # Create a deque to store the current maximum element
    window = deque()
    
    # Create a list to store the rolling maximum elements
    max_elements = []

    # Iterate over the numbers in the input list
    for i, num in enumerate(numbers):
        # Check if the current element is greater than the last element in the deque
        while window and num >= numbers[window[-1]]:
            window.pop()
        
        # Append the current element index to the deque
        window.append(i)
        
        # Check if the first index in the deque is outside the rolling window
        if window[0] == i - len(window):
            window.popleft()
        
        # Append the current maximum element to the output list
        max_elements.append(numbers[window[0]])

    # Return the rolling maximum element list
    return max_elements
