# check if the given string is a number using lambda function
string_input = "1234"
number_check = (lambda s: s.isdigit())(string_input)
if number_check:
    print(f'The given string "{string_input}" is a number.')
else:
    print(f'The given string "{string_input}" is not a number.')

