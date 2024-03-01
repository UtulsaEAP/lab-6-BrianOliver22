""""
Name: Brian Oliver
Lab time: 2/28.2024 1:15
"""
def process_and_print(input_string):
      # Split into separate strings

    # Convert strings to integers and filter out negative values
  input_data = input_string.split()

  for i in range(len(input_data)):
    input_data[i] = eval(input_data[i])
  sort_list = []
  for i in range(len(input_data)):
    if (input_data[i]<0):
      sort_list.append(input_data[i])
  # print(sort_list)
  """"
  sorted_list = sort_list
  print(sorted_list)
  """
  sorted_list = sorted(sort_list)
  for i in range(len(sorted_list)):
    sorted_list[i] = str(sorted_list[i])
  sorted_list = sorted_list [::-1]
  #print(sorted_list)
  sep = " "
  sorted_list = sep.join(sorted_list)
  print(sorted_list + " ")
    # Print sorted integers
  #print(sort_list)                10 -7 4 -39 -6 12 -2
    # Sort integers in reverse order
  #lowest_number = 0
  """"
    for i in range(len(sort_list)):
      if lowest_number > sort_list[i]:
          lowest_number = sort_list[i]
  """
    
    # Print sorted integers

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = str(input("Enter a space-separated string of numbers: "))

    # Call the function to process and print the result
    process_and_print(user_input)
