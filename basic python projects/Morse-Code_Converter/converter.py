from turtle import position
from morse import morse

choice = input("Do you want to convert from Morse to English or English to Morse? (me or em) ")

if choice == "me":
    text = input("Enter morse to convert: (put \" \" between words) ")
    text = text.split(" ")
    key_list = list(morse.keys())
    value_list = list(morse.values())
    for words in text:
        clean_word = words.replace(" ", "")
        position = value_list.index(clean_word)
        print(key_list[position], end=" ")

else:
    text = input("Enter English to convert: ")
    for char in text:
        print(f"{morse[char.upper()]}", end=" ")