def process_input(input_string):
      # Split into separate strings
  
  my_list = input_string.split()
  highest_val = 0
  for i in range(len(my_list)):
      my_list[i] = eval(my_list[i])
    # Convert strings to floats
  for i in range(len(my_list)):
      if (highest_val < my_list[i]):
          highest_val = my_list[i]
  average_value = 0
  for i in range(len(my_list)):
      average_value += my_list[i]
  average_value = average_value/len(my_list)

    # Get max and average
  max_value = highest_val
  return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
