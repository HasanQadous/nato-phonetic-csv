import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dic = {row.letter: row.code for (index, row) in data.iterrows()}

def gen():
    user_input = input("Give ur word!!").upper()
    try:
        lists = [dic[letter] for letter in user_input]
    except KeyError:
        print("Only Letters Please!!")
        gen()
    else:
        print(lists)

gen()