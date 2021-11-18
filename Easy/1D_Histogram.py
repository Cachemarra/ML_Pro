#%% 
"""
A histogram represents the frequency distributionof data. The idea is to take
a list of values and make a tally of how many times each value occurs.

Given a 1D NumPy array, create a histogram of the data represented as a NumPy array
where the index represents the number and the value represents the count.
Note that the first index (position 0) represents how many times number 1 occurs.

There are 2 things to note:

    The parameter range default from min to max, however the task requires
    histogram starting from 1.

    bins default to only 10 values, therefore we must set it to max cover all the 
    numbers in the np.array


    example: 
        arr:   [1, 1, 1, 2, 2, 3, 5, 6, 7, 8, 9, 6, 8, 9, 7, 2, 9]
        output:[3, 3, 1, 0, 1, 2, 2, 2, 3]

"""
# Libraries
import numpy as np

# Solution Class
def get_histogram(arr: np.array) -> np.array:
    """
    Function to get an histogram of a 1D array.
    :param arr: 1D array
    :return: 1D array
    """
    # Check if the array is not an numpy object. If not, convert it to one.
    if type(arr) != np.ndarray:
        arr = np.array(arr)
    
    # Create a histogram of the array
    larg = np.unique(arr)
    
    # Create an array with the true large of the input.
    # larg has all the unique values ordered from min to max.
    # we iterate to ensure to have all the integers between the min and max.
    histogram = []
    
    for i in range(larg[-1]):
        histogram.append((arr == i+1).sum())
        
    return np.array(histogram)



#%% Test

if __name__ == "__main__":
    # Test 1
    arr = np.array([1, 1, 1, 2, 2, 3, 5, 6, 7, 8, 9, 6, 8, 9, 7, 2, 9])
    print(get_histogram(arr))
    
    # Test 2
    arr = np.array([1, 12, 6, 7, 2, 3, 4, 12, 12, 12, 6 ,6, 7, 7, 7, 7, 1, 1, 1, 1, 4, 4, 4, 4])
    print(get_histogram(arr))

