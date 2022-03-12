import pandas as pd

data = pd.read_csv('NATO Phonetic Alphabet/nato_phonetic_alphabet.csv')

dict = {row.letter: row.code for (index,row) in data.iterrows()}
name = input('Enter your name: ')
name = name.upper()

dict = {a:dict[a] for a in name}

for key in name:
    print(f"{key} for {dict[key]}")