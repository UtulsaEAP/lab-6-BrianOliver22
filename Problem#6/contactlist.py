""""
Name: Brian Oliver
Lab time: 2/29/2024 12:30
"""
def process_user_contacts(user_input):
    if "," in user_input:
        user_contacts = dict(subString.split(",") for subString in user_input.split(" ")) 
    else:
        vlue = user_input.split(" ")
        user_contacts ={}
        counter = 0
        counter2 = 1

        while (counter < len(vlue)):
            user_contacts.update({vlue[int(counter)] : vlue[counter2]})
            counter += 2
            counter2 += 2

  #  user_input = 
   # tokens = 


    # Put word pairs into a dictionary
    
    # Get contact name from input, output contact's phone number
    contact_name = input("Enter the contact name: ")
    if (contact_name in user_contacts):
        print(user_contacts[contact_name])
    elif (contact_name not in user_contacts):
        print("Contact not found.")

    

   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
