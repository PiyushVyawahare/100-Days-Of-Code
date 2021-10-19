import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_df = {row.letter: row.code for index, row in df.iterrows()}
# print(dict_df)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [dict_df[letter] for letter in word]
print(output_list)
