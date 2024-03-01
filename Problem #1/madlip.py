""""
Name: Brian Oliver
Lab time: 2/28.2024 12:30
"""
def food_input():
    user_input = input()
    tokens = user_input.split()
    storage = []

    #type you while  loop here
    while (user_input != "quit 0"):
        tokens = user_input.split()
        if (user_input != quit):
            storage.append("Eating "+ str(tokens[1]) + " " +str(tokens[0]) + " a day keeps you happy and healthy.")
        user_input = input()
    sep = "\n"
    storage = sep.join(storage)
    print(storage)



    

if __name__ == "__main__":
    food_input()
