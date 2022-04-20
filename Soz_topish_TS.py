# Temurbek Yorkulov 

# 20. 04. 2022

"""So'z topish o'yini"""


from random import choice
from uzwords import words

def get_words():
    word = choice(words)
    while '-' in word or ' ' in word:
        word = choice(words)
    return word.upper()
 

def display(user_letters, word):
    main_letters = ''
    for letter in word:
        if letter in user_letters.upper():
            main_letters += letter
        else:
            main_letters += "_"
    return main_letters



def play():
    word = get_words()
    word_letters = set(word)
    user_letters = ''
    print(f"Men {len(word)} ta harfdan iborat so'z uyladim: ")
    print("Marhamat topishga harakat qilib ko'ring: ")

    while len(word_letters) > 0:
        print(display(user_letters, word))
        letter = input("Xarf kiriting: ").upper()
        
        if letter in user_letters:
            print(f"Shu vaqtgacha kiritgan harflaringiz {user_letters}")
        
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting: ")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri.")
        else:
            print("Bunday harf yuq.")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta o'rinishda topdingiz.")
play()    
while True:
    print("Yana o'ynashni hohlaysizmi (ha / yo'q): ")
    answer = input()
    if answer == 'ha':
        play()
    else:
        break



























