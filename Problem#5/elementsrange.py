""""
Name: Brian Oliver
Lab time: 2/28.2024 1:30
"""
def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    my_list = []
    for i in range(len(input_list)):
        if (input_list[i] <max_val):
            if (input_list[i] > min_val):
                my_list.append(input_list[i])
    sep = ","
    my_list = sep.join(my_list)
    print(my_list+",")
if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    input_list = user_input.split()

    # Get input for the range (min and max values)
    user_put = input("Enter the min and max values separated by a space: ")
    numbers = user_put.split()
    min_val, max_val = numbers[0],numbers[1]
    filter_and_print_range(input_list,min_val,max_val)

    # Call the function to filter and print the numbers in the given range
   
