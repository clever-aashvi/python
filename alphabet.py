user_input = input("Enter a character: ")

if len(user_input) == 1 and user_input.isalpha():
    print(f"Yes, '{user_input}' is an alphabet letter.")
else:
    print(f"No, '{user_input}' is NOT a single alphabet letter.")
