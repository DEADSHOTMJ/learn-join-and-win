def reverse_words(input_string):
    words = input_string.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

user_input = input("Enter a long string: ")
result = reverse_words(user_input)
print("Output:", result)
