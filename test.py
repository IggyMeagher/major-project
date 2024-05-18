import bcrypt

login_password = 'bob'.encode('utf-8')

# The hashed password retrieved from the database
with open('user_data/bob.txt', 'r') as file:
    file_lines = file.readlines()

# Strip any newline characters and encode the stored hashed password to bytes
stored_hashed_password = file_lines[1].strip().encode('utf-8')

if bcrypt.checkpw(login_password, stored_hashed_password):
    print('welcome')
else:
    print('get out')
