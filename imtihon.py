import random
import datetime
import os
import platform
from reportlab.pdfgen import canvas

# ======== USER CLASS ========
class User:
    def __init__(self, name, pas, card, bal, role="user"):
        self.name = name
        self.pas = pas
        self.card = card
        self.bal = bal
        self.role = role
        self.savat = []  # list of Tovar objects
        self.tarix = []

    def add_savat(self, t, kg):
        for i in self.savat:
            if i.tit == t.tit:
                i.kg += kg
                return
        self.savat.append(Tovar(t.tit, t.price, kg))

    def edit_savat(self, tit, kg):
        for i in self.savat:
            if i.tit == tit:
                if kg <= 0:
                    self.savat.remove(i)
                else:
                    i.kg = kg

    def buy(self):
        jami = sum(i.price * i.kg for i in self.savat)
        if jami > self.bal:
            print("Balans yetmaydi!")
            return False

        # savat nusxasi (chek uchun)
        old_savat = [Tovar(i.tit, i.price, i.kg) for i in self.savat]

        self.bal -= jami

        for i in self.savat:
            self.tarix.append(f"{i.tit} {i.kg}kg – {i.price*i.kg} so'm")

        # PDF chek yaratish va avtomatik ochish
        fayl = qogoz_chek(self.name,
                          [{"nom":i.tit,"miqdor":i.kg,"narx":i.price} for i in old_savat],
                          self.card)

        self.savat = []
        print("Sotib olindi va chek tayyor!")
        return True

# ======== TOVAR CLASS ========
class Tovar:
    def __init__(self, tit, price, kg=0):
        self.tit = tit
        self.price = price
        self.kg = kg

# ======== MARKET CLASS ========
class Market:
    def __init__(self):
        self.users = []
        self.tovarlar = []
        self.cats = []
        self.load_def()

    def load_def(self):
        # default admin va foydalanuvchilar
        self.users.append(User("admin", "1234", "0000000000000000", 0, "admin"))
        self.users.append(User("ali", "1111", "1111222233334444", 500000))
        self.users.append(User("vali", "2222", "5555666677778888", 300000))
        self.cats.append("meva")
        self.tovarlar.append(Tovar("olma", 12000))
        self.tovarlar.append(Tovar("banan", 18000))

    def login(self, name, pas):
        for u in self.users:
            if u.name == name and u.pas == pas:
                return u
        return None

    def reg(self):
        name = input("Login: ")
        pas = input("Parol: ")
        card = input("Karta(16 raqam): ")
        if len(card)!=16 or not card.isdigit():
            print("Xato karta!")
            return
        bal = random.randint(10000, 999000)
        u = User(name, pas, card, bal)
        self.users.append(u)
        print(f"Ro'yxatdan o'tdi. Balans: {bal} so'm")

    def add_tov(self):
        t = input("Nom: ")
        p = int(input("Narx: "))
        self.tovarlar.append(Tovar(t,p))
        print("Qo'shildi")

    def edit_tov(self):
        t = input("Nom: ")
        for i in self.tovarlar:
            if i.tit == t:
                p = int(input("Yangi narx: "))
                i.price = p
                print("O'zgardi")
                return

    def del_tov(self):
        t = input("Nom: ")
        for i in self.tovarlar:
            if i.tit == t:
                self.tovarlar.remove(i)
                print("O'chirildi")
                return

# ======== PDF CHEK FUNKSIYA ========
def qogoz_chek(user_name, savat, karta):
    folder = "cheklar"
    if not os.path.exists(folder):
        os.mkdir(folder)
    dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    fayl = os.path.abspath(f"{folder}/CHEK_{user_name}_{dt}.pdf")  # absolute path

    c = canvas.Canvas(fayl)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(200, 800, "MARKET 24/7")
    c.setFont("Helvetica", 12)
    c.drawString(50, 780, "Toshkent, O'zbekiston")
    c.drawString(50, 765, f"Sana: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")
    c.drawString(50, 750, f"User: {user_name}")
    c.drawString(50, 735, "----------------------------------")

    y = 720
    jami = 0
    for i in savat:
        nom = i['nom']
        miq = i['miqdor']
        narx = i['narx']*miq
        jami += narx
        c.drawString(50, y, f"{nom:<12}{miq:<5}{narx} so'm")
        y -= 20

    c.drawString(50, y-10, "----------------------------------")
    c.drawString(50, y-30, f"Jami: {jami} so'm")
    c.drawString(50, y-50, f"Karta: **** **** **** {karta[-4:]}")
    c.drawString(50, y-70, "Rahmat! Yana keling!")
    c.showPage()
    c.save()

    print(f">>> Chek tayyor: {fayl}")

    # avtomatik ochish
    try:
        if platform.system() == "Windows":
            os.startfile(fayl)
        elif platform.system() == "Darwin":  # macOS
            os.system(f"open '{fayl}'")
        else:  # Linux
            os.system(f"xdg-open '{fayl}'")
    except Exception as e:
        print("Chekni ochib bo'lmadi:", e)

    return fayl

# ======== USER MENU ========
def user_menu(u, m):
    while True:
        print("\n1) Mahsulotlar  2) Savat  3) Balans  4) Tarix  5) Karta almashtirish  0) Chiqish")
        s = input(">>> ")
        if s=="1":
            print("\nMahsulotlar:")
            for i in m.tovarlar:
                print(f"{i.tit} - {i.price} so'm")
            n = input("Nom: ")
            kg = float(input("Kg: "))
            for i in m.tovarlar:
                if i.tit == n:
                    u.add_savat(i, kg)
        elif s=="2":
            print("\nSavat:")
            for i in u.savat:
                print(f"{i.tit} {i.kg}kg {i.price*i.kg} so'm")
            print("1) Tahrir  2) Sotib olish")
            c = input(">>> ")
            if c=="1":
                n = input("Nom: ")
                k = float(input("Kg: "))
                u.edit_savat(n, k)
            elif c=="2":
                u.buy()
        elif s=="3":
            print(f"Balans: {u.bal} so'm")
            if input("Pul qo'shilsinmi? (h/n): ")=="h":
                s=int(input("Miqdor: "))
                u.bal += s
                print("Balans yangilandi")
        elif s=="4":
            print("\nTarix:")
            for t in u.tarix:
                print(t)
        elif s=="5":
            c=input("Yangi karta: ")
            if len(c)==16 and c.isdigit():
                u.card = c
                print("Karta almashtirildi")
            else:
                print("Xato karta!")
        elif s=="0":
            break

# ======== ADMIN MENU ========
def admin_menu(u, m):
    while True:
        print("\n1) Tovar qo'sh  2) Tahrir  3) O'chirish  4) Foydalanuvchilar tarixi  0) Chiqish")
        s = input(">>> ")
        if s=="1":
            m.add_tov()
        elif s=="2":
            m.edit_tov()
        elif s=="3":
            m.del_tov()
        elif s=="4":
            for us in m.users:
                print(f"\n{us.name}:")
                for t in us.tarix:
                    print(" ", t)
        elif s=="0":
            break

# ======== ASOSIY LOOP ========
m = Market()
while True:
    print("\n1) Login  2) Ro'yxatdan o'tish  0) Chiqish")
    c = input(">>> ")
    if c=="1":
        n = input("Login: ")
        p = input("Parol: ")
        u = m.login(n,p)
        if u:
            if u.role=="admin":
                admin_menu(u,m)
            else:
                user_menu(u,m)
        else:
            print("Login yoki parol xato!")
    elif c=="2":
        m.reg()
    elif c=="0":
        break
