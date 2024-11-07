name="baba"
reversed_string =name[::-1]
print(reversed_string)


# Function to check if a string is a palindrome using a for loop
def is_palindrome(string):
    # Normalize the string by removing spaces and converting to lowercase
    string = string.replace(" ", "").lower()

    # Use a for loop to compare characters from start and end
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:  # Compare characters from both ends
            return False
    return True


# Input from the user
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")