def custom_upper(text):
    result = ""
    for char in text:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert it to uppercase by using the ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Get input text from the user
input_text = input("Enter the text to convert to uppercase: ")

# Call the custom function to convert the input text
output_text = custom_upper(input_text)

# Print the result
print("Converted text:", output_text)
