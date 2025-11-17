import re
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
s1=Contact('ali',"4578574","sdfd@gmail.com")
baza=[s1]

re1=r'^[A-Za-zА-Яа-яЎҒҚҲʼ\' ]{2,30}$'
re2=r'^(?:\+?998\s*|\s*0)(?:90|91|93|94|95|97|98|99|33|71|88)\s*\d{3}\s*\d{2}\s*\d{2}$'
re3=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
def add_contact(s:list):
    name=input('Ism: ')
    phone=input('Telefon: ')
    email=input('Email: ')
    if re.match(re1,name) and re.match(re2,phone) and re.match(re3,email):
        print("Kontakt qoshildi")

    else:
        print("Parametrlarda xatolik bor.Namunalar:\nAli\n+998991234567\nali@gmail.com")



def update_contact(baza: list):
    while True:
        if not baza:
            print("Kontakt mavjud emas!")
            return

        print("Kontaktlar:")
        for i, contact in enumerate(baza, 1):
            print(f"{i}) Ism: {contact[0]}, Telefon: {contact[1]}, Email: {contact[2]}")

        try:
            index = int(input("Tahrirlanuvchi kontakt tartib raqamini tanlang: ")) - 1
            if index < 0 or index >= len(baza):
                print("Qiymat noto'g'ri")
                return
        except ValueError:
            print("Raqam kiriting")
            return

        contact = baza[index]
        print(f"Tanlangan kontakt: Ism: {contact[0]}, Telefon: {contact[1]}, Email: {contact[2]}")
        t1= input("1.Ismni tahrirlash\n2.Raqamni tahrirlash\n3.Emailni tahrirlash\n4.Ortga\nTanlang: ")

        if t1 == "1":
            new_name = input("Yangi ism: ")
            if re.match(re1, new_name):
                contact[0] = new_name
                print("Ism tahrirlandi")
            else:
                print("Xatolik. Ismda ortiqcha belgilar mavjud.")

        elif t1 == "2":
            new_phone = input("Yangi raqam: ")
            if re.match(re2, new_phone.replace(" ", "")):
                contact[1] = new_phone
                print("Raqam tahrirlandi")
            else:
                print("Raqam xato kiritilgan. Namuna: +998991234567")

        elif t1 == "3":
            new_email = input("Yangi email: ")
            if re.match(re3, new_email):
                contact[2] = new_email
                print("Email tahrirlandi")
            else:
                print("Emailda xatolik bor. Namuna: youremail@gmail.com")
        elif t1 == "4":
            contact_manager()

        else:
            print("Qiymat noto'g'ri")

def view_contact(baza: list):
    if not baza:
        print("Hali kontakt mavjud emas!")
        return

    print("\nKontaktlar:")
    count = 1
    for item in baza:
        print(f"{count}. Ism: {item.name}, Telefon: {item.phone}, Email: {item.email}")
        count += 1


def contact_manager():
    while True:
        kod=input("1.Mavjud kontaktlar\n2.Kontaktlarni tahrirlash\n3.Yangi kontakt\nTanlang: ")
        if kod=="1":
            view_contact(baza)
        elif kod=="2":
            update_contact(baza)
        elif kod=="3":
            add_contact(baza)
        else:
            print("Qiymat noto'g'ri")
contact_manager()


