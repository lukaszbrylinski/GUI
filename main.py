import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
print(alphabet)
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
# print(alphabet_dict)

print(alphabet)
# wrong = 1
# while wrong:
#     word = input("Type word: ")
#     try:
#         word_list = [alphabet_dict[letter.title()] for letter in word]
#     except KeyError:
#         print("Sorry, only letter in the alphabet please.")
#     else:
#         wrong = 0

def generate_npa():
    word = input("Type word: ")
    try:
        word_list = [alphabet_dict[letter.title()] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_npa()
    else:
        print(word_list)

generate_npa()