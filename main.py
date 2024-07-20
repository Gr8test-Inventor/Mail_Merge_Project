PLACEHOLDER = "[name]"
#TODO 1: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_base = letter_file.read()
    # print(letter_base)

# TODO 2: Save names from invited_names.txt into a list called name_list
with open("./Input/Names/invited_names.txt") as names_file:
    name_list = names_file.readlines()
    # print(name_list)

# TODO 3: Format name from name_list into usable form by removing \n.
# TODO 4: Replace the [name] placeholder with the actual name from name_list.
for raw_name in name_list:
    formatted_name = raw_name.replace("\n", "") # Or raw_name.strip()
    personal_letter = letter_base.replace(PLACEHOLDER, formatted_name)
    with open(f"Output/ReadyToSend/letter_for_{formatted_name}.txt", mode= "w") as completed_letter:
        completed_letter.write(personal_letter)




# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp