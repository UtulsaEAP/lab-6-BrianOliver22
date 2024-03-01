""""
Name: Brian Oliver
Lab time: 3/1/2024 3:20
"""
def in_order(nums1):

    # Type your code here.

    #check = True

    #order = 0

    for i in range(1, len(nums1)):

        if nums1[i - 1] > nums1[i]:

            return False

    return True

 

if __name__ == '__main__':

    # Test out-of-order example

    nums1 = [5, 6, 7, 8, 3]

    if in_order(nums1):

        print('In order')

    else:

        print('Not in order')

        # Test in-order example

    nums2 = [5, 6, 7, 8, 10]

    if in_order(nums2):

        print('In order')

    else:

        print('Not in order')