import random
import re
from collections import Counter
from nltk import ngrams


def verify_word(word):
    if (re.search('^[A-Z]', word) is None or
            (re.search('[.!?]$', word)
             and re.search('^[A-Z]', word))):
        return False
    return True


user_input_file = input()

f = open(user_input_file, "r", encoding="utf-8")

txt = f.read()
tokens = [i for i in txt.replace('\n', ' ').split(' ') if len(i) > 0]
n_grams = ngrams(tokens, 3)
result_n_grams = [x for x in n_grams]
heads = [f'{head[0]} {head[1]}' for head in result_n_grams]
count = 1

while count <= 10:

    while True:
        random_input = random.choice(heads)
        if verify_word(random_input):
            break

    text = random_input.split(' ')

    try:

        for i in range(len(text), 10):

            tails = [result_n_grams[i][2] for i in range(len(result_n_grams))
                     if heads[i] == random_input]

            freq_counter = Counter(tails)
            tails_list = list(freq_counter.keys())
            weights_list = list(freq_counter.values())
            next_word = ''.join(random.choices(population=tails_list, weights=weights_list))

            text.append(next_word)
            random_input = f'{text[len(text) - 2]} {text[-1]}'

            if len(text) > 4 and re.search('[.!?]$', next_word):
                break

        if len(re.findall('[.!?]', ' '.join(text))) > 1:
            text.clear()
        elif re.search('[.!?]$', text[-1]):
            print(' '.join(text))
            text.clear()
            count += 1
        else:
            text.clear()


    except Exception as ex:
        print("Key Error. The requested word is not in the model. Please input another word.")
