import random

# Define the set of characters that can be used in the usernames
char_set = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'

# Generate 1 million random usernames and store them in a list
usernames = []
for i in range(1000000):
    username = ''
    for j in range(8):  # Assume each username is 8 characters long
        username += random.choice(char_set)
    usernames.append(username)

# Define a function to check if a username is valid
def is_valid_username(username):
    # Put your validation criteria here
    # For example, you may want to check if the username is already taken
    # on Roblox, or if it contains inappropriate words
    # For this example, we'll just assume all usernames are valid
    return True

# Loop through the list of usernames and check if they're valid
for username in usernames:
    if is_valid_username(username):
        print(f"{username} is available")
    else:
        print(f"{username} is not available")
