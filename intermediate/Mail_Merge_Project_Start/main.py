#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    # letter_for_name
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

REPLACE_TEXT = "[name]"
person_names = []

with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

# removes spaces and "\n"
for name in names:
    name = name.strip()
    person_names.append(name)

# print(person_names)

with open("./Input/Letters/starting_letter.txt", mode="r") as letter:
    content = letter.read()
    print(content)
  

for person_name in person_names:
    # returns a string with replaced name
    letter_for_name  = content.replace(REPLACE_TEXT, person_name)

    with open(f"./Output/ReadyToSend/invited_letter_{person_name}.txt", mode="w") as invite:
        invite.write(letter_for_name)
