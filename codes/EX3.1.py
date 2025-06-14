def calculate_average(numbers_list): 
    """
    Calculate the average of numbers in a list.
    
    Args:
        numbers_list (list): A list of numbers (int or float)
        
    Returns:
        float: The average of the numbers
        
    Raises:
        TypeError: If the list contains non-numeric values
        ValueError: If the list is empty
    """
    if not numbers_list:
        raise ValueError("Cannot calculate average of an empty list")
        
    total = 0 
    for num in numbers_list: 
        if not isinstance(num, (int, float)):
            raise TypeError(f"All values must be numeric, got {type(num).__name__}")
        total += num 
    average = total / len(numbers_list) 
    return average 
 
# Example of usage with error handling
try:
    my_nums = [1, 2, 'three', 4] # This will raise an error
    avg = calculate_average(my_nums) 
    print(f"Average: {avg}")
except Exception as e:
    print(f"Error: {e}")

# Correct example
correct_nums = [1, 2, 4, 5]
avg = calculate_average(correct_nums)
print(f"Average of correct numbers: {avg}")

# code de départ
a = [5, 3, 8, 6, 7, 2]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
print(a)
