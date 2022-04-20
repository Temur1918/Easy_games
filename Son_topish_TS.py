# Temurbek Yorkulov

# 16. 04. 2022

"""Son topish uyini"""

from random import randint
from random import choice

while True:
    k_number = randint(1, 11)
    print("Keling siz bilan uyin uynaymiz, \nSiz men uylagan sonni topishingiz kerak: 1 dan 10 gacha oraliqdagi ")
    t_number = 1
    while True:
        u_answer = int(input("sonni kiriting: "))
        if u_answer == k_number:
            print(f"Siz {t_number} - urinishda tugri topdingiz!")
            break
        if u_answer < k_number:
            print(f"Men o'ylagan son {u_answer} dan katta!")
        else:
            print(f"Men o'ylagan son {u_answer} dan kichik!")
        t_number += 1


    print("Keling endi siz o'ylagan sonni men topishga harakat qilaman!")
    print("O'yinni boshlash uchun 'start' buyrug'ini kiriting: ")
    start = input()
    t1_number = 1
    u_number = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
    if start == 'start':
        while True:
            number = choice(u_number)
            print(f"Siz {number} sonini o'yladingiz to'g'rimi (To'g'ri topdingiz 'T', "
            "\nnMen uylagan son kichik '-'\nMen o'ylagan son katta '+':")
            k_question = input().lower()
            if k_question == 't':
                print(f"Men {t1_number} - urinishda topdim! Umumiy hisob:")
                if t1_number == t_number:
                    print(f"{t1_number} : {t_number} Do'stlik g'alaba qozondi!")
                elif t1_number > t_number:
                    print(f"Men g'alaba qozondim umumiy hisob {t1_number} : {t_number}!")
                else:
                    print("Men g'laba qozondim {t1_number} : {t_number}!")
                    break

            elif k_question == '-':
                u_number = u_number[ : number - 1]
                t1_number += 1
            
            elif k_question == '+':
                u_number = u_number[number : ]
                t1_number += 1
            
            else:
                print("Mavjud bo'lmagan javobni kiritdingiz! ")
                t1_number += 1
            
    print("Yana o'ynamoqchimisiz! (ha, yo'q)")
    y_answer = input()
    if y_answer != 'ha':
        break
















