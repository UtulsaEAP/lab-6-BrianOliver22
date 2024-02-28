""""
Name: Brian Oliver
Lab time: 2/28.2024 12:45
"""
def check_palindrome(user_input):
 #type your code here
    input_user = user_input [::-1]
    if (input_user == user_input):
        print("palindrome: "+user_input)
    elif (input_user != user_input):
        print("not a palindrome: "+user_input)

if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
