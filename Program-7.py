import re
def extract_company(email):
    return email.split('@')[-1].split('.')[0]
emailAddress = input("Enter email addresses: ")
print(extract_company(emailAddress))
