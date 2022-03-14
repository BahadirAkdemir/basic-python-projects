import pandas as pd

data = pd.read_csv('nato_phonetic_alphabet.csv')

dict = {row.letter: row.code for (index,row) in data.iterrows()}


def generate_phonetic(dict):
    try:
        name = input('Enter your name: ')
        name = name.upper()
        dict = {a:dict[a] for a in name}
        OUTPUT = [dict[a] for a in name] 
    except:
        print("Not in alphabet, Please give valid input")
        generate_phonetic(dict)
    else:
        print(OUTPUT)

generate_phonetic(dict)