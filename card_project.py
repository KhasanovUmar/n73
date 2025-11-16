import json
import re
# card={
#     '8600030411777067':{
#         'karta raqami':'8600030411777067',
#         '4ta raqami':'7067',
#         'amal qilish muddati':'12/28',
#         'karta egasi':'Umar Khasanov',
#         'summa':200000,
#         'karta nomi':'asosiy'
#     }
# }

# def add_card(d:dict):
#     with open('card_data.json','a') as f:
#         data=json.dump(card,f,indent=4)
# add_card(card)

def wr_cards(d:dict):
    with open('card_data.json','w') as f:
        data=json.dump(d,f,indent=4)

def read_cards():
    s=0
    with open('card_data.json','r') as f:
        try:
            s=json.load(f)
            return s
        except:
            return False
read_cards()

n = r'^\d{16}$'
def add_card():
    data=read_cards()
    card_number=input('Karta raqamini kiriting:')
    c4_numbers=card_number[-4:]
    card_data=input('Amal qilish muddatini kiriting (namuna:12/28):')
    card_user=input('Karta egasining ism familiyasi:')
    import random
    card_money=random.randint(1000,99000)
    card_name=input('Karta nomini kiriting (masalan: asosiy):')
    s={
        c4_numbers:{
            'karta raqami':card_number,
            '4ta raqami': c4_numbers,
            'amal qilish muddati':card_data,
            'karta egasi':card_user,
            'summa':card_money,
            'karta nomi':card_name
        }
    }
    if re.match(n,card_number):
        if data:
            data=dict(data)
            read_cards()
            data.update(s)
            wr_cards(data)
        else:
            wr_cards(s)
        print('Yangi karta qoshildi')
    else:
        print('Parametrlarni kiritishda xatolik.\nYaxshilab tekshiring va qayta urining')

def view_cards():
    data=read_cards()
    if not data:
        prnt=input('===============\nKartalar mavjud emas.\nQoshish uchun 1 ni bosing:')
        if prnt=='1':
            add_card()
        else:
            print('Notogri qiymat. Qayta urining')
        return
    keys=list(data.keys())
    print('=== Mavjud kartalar ===')
    i=1
    for k in keys:
        card=data[k]
        print(str(i)+'.'+card['karta nomi'] + '-'+card['4ta raqami'])
        i+=1
    card_select=input("Ortga qaytish uchun 'd' tugmasini bosing.\nKerakli tartib raqam yoki tugmani kiriting:")
    if card_select=='d':
        card_menu()
    if card_select.isdigit():
        e=int(card_select)
        if 1<=e<=len(keys):
            k=keys[e-1]
            card=data[k]
            print('=== Malumot ===')
            print("Karta nomi:", card['karta nomi'])
            print("Karta raqami:", card['karta raqami'])
            print("Amal qilish muddati:", card['amal qilish muddati'])
            print("Karta egasi:", card['karta egasi'])
            print("Summa:", card['summa'], "so'm")
            print('---------------')
            while True:
                kod1=input('Otkazma amalga oshirish uchun 1 ni bosing.\nOrtga qaytish uchun 2 ni bosing: ')
                if kod1=='1':
                    kod2=input('Otkazmoqchi bolgan summani kiriting: ')
                    if int(kod2)<card['summa']:
                        print('Qabul qilindi.')
                        kod3 = input('Karta raqamini kiriting: ')
                        if re.match(n, kod3):
                            card['summa'] -= int(kod2)

                            with open('card_data.json', 'r') as f:
                                all_cards = json.load(f)
                            all_cards[card['4ta raqami']] = card
                            with open('card_data.json', 'w') as f:
                                json.dump(all_cards, f, indent=4)

                            try:
                                with open('stories.json', 'r') as f:
                                    stories = json.load(f)
                            except:
                                stories = []

                            stories.append({
                                "from_card": card['karta raqami'],
                                "to_card": kod3,
                                "amount": kod2
                            })

                            with open('stories.json', 'w') as f:
                                json.dump(stories, f, indent=4)

                            print("Otkazma muvaffaqiyatli yakunlandi.\nQolgan balans:",card['summa'])
                        else:
                            print("Karta raqamini kiritishda xatolik.\nSonlar 16 tadan ko'p yoki kam ekanini tekshiring")
                            break
                    else:
                        print("Kartada mablag' yetarli emas.\nMavjud mablag':", card['summa'], "so'm")
                        print('---------------')
                        kod4=input('Qatya urinish uchun 1 ni bosing.\nOrtga qaytish uchun 2 ni bosing: ')
                        if kod4=='2':
                            view_cards()
                if kod1=='2':
                    view_cards()
        else:
            print('Tartib raqam xato')
    else:
        print('Qiymat notogri.')

def delete_card(card_key):
    try:
        with open('card_data.json','r') as f:
            data=json.load(f)
    except:
        print("Karta topilmadi")
        return
    if card_key in data:
        del data[card_key]
        with open('card_data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print(f"{card_key} raqamli karta o'chirildi.")
    else:
        print("Bunday karta mavjud emas.")

def view_stories():
    try:
        with open('stories.json', 'r') as f:
            stories = json.load(f)
    except:
        print("Hozircha hech qanday o'tkazma mavjud emas.")
        return

    if not stories:
        print("Hozircha hech qanday o'tkazma mavjud emas.")
        return

    print("O'tkazmalar tarixi:")
    i=1
    for t in stories:
        print('---------------')
        print(f"{i}. Kartadan: {t['from_card']}\nKartaga: {t['to_card']}\nMiqdor: {t['amount']} o'tkazilgan")
        i+=1

def clear_stories():
    with open('stories.json','w') as f:
        json.dump([],f,indent=4)
    print('Tarix tozalandi!')

def stories_menu():
    strs=input("1.Tarixni ko'rish\n2.Tarixni tozalash\n3.Ortga\nTanlang:")
    if strs=='1':
        view_stories()
    elif strs=='2':
        print('Tarixni tozalashga ishonchingiz komilmi?')
        strs2=input('1.Ha\n2.Yoq (ortga qaytish)\nAniqlik kiriting:')
        if strs2=='1':
            clear_stories()
        elif strs2=='2':
            stories_menu()
        else:
            print("Noto'g'ri qiymat")
    elif strs=='3':
        card_menu()

def card_menu():
    while True:
        print('=== Kartalarni boshqarish bolimi ===')
        print('Raqamlardan birini tanlang:')
        cardtext=input('1. Karta qoshish \n2. Mavjud kartalar \n3. Mavjud kartani ochirish \n4. Otkazmalar tarixi \nTanlash:')
        if cardtext=='1':
            add_card()
        elif cardtext=='2':
            view_cards()
        elif cardtext=='3':
            key = input("O'chirmoqchi bo'lgan kartaning \noxirgi 4 raqamini kiriting: ")
            delete_card(card_key=key)
        elif cardtext=='4':
            stories_menu()

def all_menu():
    while True:
        print("=== Assalomu aleykum ===")
        print("=== Ilovamizga xush kelibsiz ===")
        allmenu=input("Kirish uchun '1' ni bosing:")
        if allmenu=='1':
            print('== Ilovamizni tanlaganingiz uchun raxmat ==')
            print("== Bo'limlardan tanlashni boshlang ==")
            startproject=input('1.Kartalarni boshqarish\n2.Daturchi\nTanlang:')
            if startproject=='1':
                card_menu()
            elif startproject=='2':
                print("Dasturchi: Xasanov\nBog'lanish turi: (hozircha mavjud emas)")
            else:
                print("Qiymat noto'g'ri. Qayta urining")
all_menu()








