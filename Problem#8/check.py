def in_order(nums):
    # Type your code here.
    check = True
    order = 0
    for i in range(len(nums)):
        if (order < nums[i]):
            order = nums[i]
        elif (order > nums[i]):
            check = False
    return check

if __name__ == '__main__':
    # Test out-of-order example
    nums = [5, 6, 7, 8, 3]
if in_order(nums):
    print('In order')
else:
    print('Not in order')
        
    # Test in-order example
    nums = [5, 6, 7, 8, 10]
if in_order(nums):
    print('In order')
else:
    print('Not in order')
