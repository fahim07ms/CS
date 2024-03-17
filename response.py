from validator_collection import checkers

is_email_ad = checkers.is_email(input("Email Address: ").strip())

print("Valid") if is_email_ad else print("Invalid")