def highest(numbers):
    """Return the biggest number in the list."""
    ordered = sorted(numbers) 
    return ordered[-1]

    nums = [7, 42, 19]
    print(highest(nums))
    print(nums)
    print(highest([5]))
   
    