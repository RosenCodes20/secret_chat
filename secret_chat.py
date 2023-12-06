some_string = input()
command = input()
while command != "Reveal":
    current_command = command.split(":|:")
    is_error = False

    if current_command[0] == "InsertSpace":
        index = current_command[1]
        index = int(index)
        some_string = f"{some_string[:index]} {some_string[index:]}"
    elif current_command[0] == "Reverse":
        substring = current_command[1]
        if substring in some_string:
            reversed_substring = substring[::-1]
            some_string = some_string.replace(substring, "", 1) + reversed_substring
        else:
            print("error")
            is_error = True
    elif current_command[0] == "ChangeAll":
        substring = current_command[1]
        replacement = current_command[2]
        some_string = some_string.replace(substring, replacement)
    if not is_error:
        print(some_string)
    command = input()

print(f"You have a new text message: {some_string}")
