import re

file = open("input.txt", "r")

content = file.read()

file.close()

pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
emails = re.findall(pattern, content)

unique_emails = []

for email in emails:
    if email not in unique_emails:
        unique_emails.append(email)

output_file = open("emails.txt", "w")

for email in unique_emails:
    output_file.write(email + "\n")

output_file.close()

print("\n===== EMAIL EXTRACTOR =====")

print("\nEmails Found:")

for email in unique_emails:
    print(email)

print("\nTotal Emails Found =", len(unique_emails))

print("\nEmails saved successfully in emails.txt")