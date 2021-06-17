# Asking for Email
email = input("What is you email address?: ").strip()    # User enters his/her email, to continue further
# Slicing of username takes place
user_name = email[:email.index("@")]

# Slicing of domain name takes place
domain_name = email[email.index("@")+1:]

# Here string formatting takes place:
User_Output = f"Your user name is {user_name} & Your domain name is {domain_name}"

# Displaying User_Output
print(User_Output)
