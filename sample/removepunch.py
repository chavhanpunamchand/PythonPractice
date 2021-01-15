# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punch=""
for char in my_str:
    if char not in punctuations:
        no_punch=no_punch+char



print(no_punch)
