with open("file/names.txt", "r") as name_file:
    names = name_file.read().split("\n")
    with open("file/letter.txt", "r") as letter:
        for name in names:
            letter.seek(0)
            letter_string=letter.read()
            letter_string=letter_string.replace("[name]", name)
            with open("file/letters/" + name + ".txt", "w") as new_letter:
                new_letter.write(letter_string)