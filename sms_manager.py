import re

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class SMS:
    def __init__(self, phone, message):
        self.phone = phone
        self.message = message


class Manager:
    def __init__(self):
        self.contacts_file = "contacts.txt"
        self.sms_file = "sms.txt"

    def add_contact(self):
        name = input("Ism: ")
        phone = input("Raqam: ")

        if not re.fullmatch(r'^\+?[0-9]{7,15}$', phone):
            print("Raqam xato")
            return

        with open(self.contacts_file, "a") as f:
            f.write(f"{name}|{phone}\n")

        print("Kontakt qo'shildi\n")

    def view_contacts(self):
        try:
            with open(self.contacts_file, "r") as f:
                data = f.readlines()
        except FileNotFoundError:
            print("Kontaktlar yo'q\n")
            return

        for line in data:
            name, phone = line.strip().split("|")
            print(f"{name} - {phone}")
        print()

    def check_contact(self, phone):
        try:
            with open(self.contacts_file, "r") as f:
                data = f.readlines()
        except:
            return False

        for line in data:
            _, p = line.strip().split("|")
            if p == phone:
                return True
        return False

    def send_sms(self):
        phone = input("Sms yuboriladigan telefon: ")

        if not re.fullmatch(r'^\+?[0-9]{7,15}$', phone):
            print("Telefon formati xato\n")
            return

        if not self.check_contact(phone):
            print("Bu raqam kontaktlar ichida yo'q\n")
            return

        message = input("SMS matni: ")

        with open(self.sms_file, "a") as f:
            f.write(f"{phone}|{message}\n")

        print("SMS yuborildi\n")

    def view_sms(self):
        try:
            with open(self.sms_file, "r") as f:
                data = f.readlines()
        except FileNotFoundError:
            print("SMS yo'q\n")
            return

        for line in data:
            phone, msg = line.strip().split("|")
            print(f"{phone} -> {msg}")
        print()


manager = Manager()

def run():
    while True:
        print("1. Add contact")
        print("2. View contacts")
        print("3. Send SMS")
        print("4. View SMS")
        print("5. Exit")

        x = input("Tanlov: ")

        if x == "1":
            manager.add_contact()
        elif x == "2":
            manager.view_contacts()
        elif x == "3":
            manager.send_sms()
        elif x == "4":
            manager.view_sms()
        else:
            break

run()
