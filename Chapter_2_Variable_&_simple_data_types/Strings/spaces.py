#blank spaces are called whitespace in programming
message = "Hello, \n World!"  # \n is used to add a new line    
print(message)

msg = "Hello  "
print(msg)
print(msg.rstrip())

text_with_spaces = "Hello World!    \n"
cleaned_text = text_with_spaces.rstrip()

print(f"Original: '{text_with_spaces}'")
print(f"Cleaned:  '{cleaned_text}'")