import pandas


nato_alph = pandas.read_csv("nato_phonetic_alphabet.csv")
new_nato_dict = {row.letter:row.code for (index, row) in nato_alph.iterrows()}
print(new_nato_dict)

# only_letters = False
#
# while not only_letters:
#     enter_word = input("Enter a word: ").upper()
#
#     try:
#         phonetic_list = [new_nato_dict[letter] for letter in enter_word]
#     except KeyError:
#
#         print("Sorry. Only letters accepted in the input")
#     else:
#         only_letters = True
#         print(phonetic_list)


###ANOTHER SOLUTION


def generate_phonetic():
    enter_word = input("Enter a word: ").upper()

    try:
        phonetic_list = [new_nato_dict[letter] for letter in enter_word]
    except KeyError:
        print("Sorry. Only letters accepted in the input")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()