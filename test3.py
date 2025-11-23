class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email


class Group:
    def __init__(self, title, profession):
        self.title = title
        self.profession = profession
        self.students = []

    def add_student(self):
        name = input("Ism: ")
        phone = input("Telefon: ")
        age = input("Yosh: ")
        email = input("Email: ")
        s = Student(name, phone, age, email)
        self.students.append(s)

    def view_students(self):
        for i, s in enumerate(self.students, 1):
            print(f"{i}. {s.name} - {s.phone}")

    def read_student(self):
        self.view_students()
        idx = int(input("Student raqami: ")) - 1
        s = self.students[idx]
        print(s.name, s.phone, s.age, s.email)

    def delete_student(self):
        self.view_students()
        idx = int(input("O‘chirish raqami: ")) - 1
        self.students.pop(idx)


class OTM:
    def __init__(self, title):
        self.title = title
        self.groups = []

    def edit_title(self):
        self.title = input("Yangi OTM nomi: ")

    def add_group(self):
        title = input("Guruh nomi: ")
        profession = input("Yo‘nalish: ")
        g = Group(title, profession)
        self.groups.append(g)

    def view_groups(self):
        for i, g in enumerate(self.groups, 1):
            print(f"{i}. {g.title} - {g.profession}")

    def read_group(self):
        self.view_groups()
        idx = int(input("Guruh raqami: ")) - 1
        g = self.groups[idx]
        print(g.title, g.profession)

    def delete_group(self):
        self.view_groups()
        idx = int(input("O‘chirish raqami: ")) - 1
        self.groups.pop(idx)


class ERP:
    def __init__(self):
        self.otms = []

    def add_otm(self):
        title = input("OTM nomi: ")
        o = OTM(title)
        self.otms.append(o)

    def view_otm(self):
        for i, o in enumerate(self.otms, 1):
            print(f"{i}. {o.title}")

    def read_otm(self):
        self.view_otm()
        idx = int(input("OTM raqami: ")) - 1
        o = self.otms[idx]
        print(o.title)

    def delete_otm(self):
        self.view_otm()
        idx = int(input("O‘chirish raqami: ")) - 1
        self.otms.pop(idx)


erp = ERP()

def menu():
    while True:
        print("""
====================
1. OTM qo‘shish
2. OTMlarni ko‘rish
3. OTMni o‘qish
4. OTM o‘chirish
====================
5. Guruh qo‘shish
6. Guruhlarni ko‘rish
7. Guruh o‘qish
8. Guruh o‘chirish
====================
9. Student qo‘shish
10. Studentlarni ko‘rish
11. Student o‘qish
12. Student o‘chirish
13. OTM nomini tahrirlash
====================
0. Chiqish
====================
""")
        cmd = input("tanlang: ")

        if cmd == "1":
            erp.add_otm()
        elif cmd == "2":
            erp.view_otm()
        elif cmd == "3":
            erp.read_otm()
        elif cmd == "4":
            erp.delete_otm()
        elif cmd == "5":
            erp.view_otm()
            idx = int(input("Qaysi OTM? ")) - 1
            erp.otms[idx].add_group()
        elif cmd == "6":
            erp.view_otm()
            idx = int(input("Qaysi OTM? ")) - 1
            erp.otms[idx].view_groups()
        elif cmd == "7":
            erp.view_otm()
            idx = int(input("Qaysi OTM? ")) - 1
            erp.otms[idx].read_group()
        elif cmd == "8":
            erp.view_otm()
            idx = int(input("Qaysi OTM? ")) - 1
            erp.otms[idx].delete_group()
        elif cmd == "9":
            erp.view_otm()
            idx = int(input("OTM tanlang: ")) - 1
            erp.otms[idx].view_groups()
            gidx = int(input("Guruh tanlang: ")) - 1
            erp.otms[idx].groups[gidx].add_student()
        elif cmd == "10":
            erp.view_otm()
            idx = int(input("OTM tanlang: ")) - 1
            erp.otms[idx].view_groups()
            gidx = int(input("Guruh tanlang: ")) - 1
            erp.otms[idx].groups[gidx].view_students()
        elif cmd == "11":
            erp.view_otm()
            idx = int(input("OTM tanlang: ")) - 1
            erp.otms[idx].view_groups()
            gidx = int(input("Guruh tanlang: ")) - 1
            erp.otms[idx].groups[gidx].read_student()
        elif cmd == "12":
            erp.view_otm()
            idx = int(input("OTM tanlang: ")) - 1
            erp.otms[idx].view_groups()
            gidx = int(input("Guruh tanlang: ")) - 1
            erp.otms[idx].groups[gidx].delete_student()
        elif cmd == "13":
            erp.view_otm()
            idx = int(input("OTM tanlang: ")) - 1
            erp.otms[idx].edit_title()
        elif cmd == "0":
            break

menu()
