import sys

class Avto:
    def __init__(self, marka, model, narx, soni):
        self.marka = marka
        self.model = model
        self.narx = narx
        self.soni = soni

    def __str__(self):
        return f"{self.marka} {self.model} | Narxi: ${self.narx:,.2f} | Soni: {self.soni} dona"


class Xodim:
    def __init__(self, ism, lavozim):
        self.ism = ism
        self.lavozim = lavozim
        self.sotuvlar_soni = 0
        self.faol_mijoz = None

    def __str__(self):
        holati = f"Sotuv: {self.sotuvlar_soni} ta"
        if self.faol_mijoz:
            holati += f" (Band: {self.faol_mijoz.ism})"
        return f"{self.ism} ({self.lavozim}) | {holati}"


class Mijoz:
    def __init__(self, ism, manzil):
        self.ism = ism
        self.manzil = manzil

    def __str__(self):
        return f" {self.ism} | Manzil: {self.manzil}"


class Avtosalon:
    def __init__(self, nomi="Avtosalon Dasturi"):
        self.nomi = nomi
        self.inventar = {}
        self.xodimlar = {}
        self.mijozlar = {}

    def _kalit_olish(self, *args):
        return " ".join(arg.strip().upper() for arg in args)

    def avto_qoshish(self, avto, silent=False):
        key = self._kalit_olish(avto.marka, avto.model)
        if key in self.inventar:
            self.inventar[key].soni += avto.soni
            if not silent:
                print(f"Avto {avto.marka} {avto.model} soni oshirildi.")
        else:
            self.inventar[key] = avto
            if not silent:
                print(f"Yangi avto {avto.marka} {avto.model} qo'shildi.")

    def inventarni_korish(self):
        if not self.inventar:
            print("ℹInventar bo'sh. Mashina yo'q.")
            return
        print(f"\n--- {self.nomi} Mashinalar Ro'yxati ---")
        for key in sorted(self.inventar.keys()):
            print(f"* {self.inventar[key]}")
        print("------------------------------------------")

    def xodim_qoshish(self, xodim):
        key = self._kalit_olish(xodim.ism)
        self.xodimlar[key] = xodim
        print(f"Xodim {xodim.ism} qo'shildi.")

    def mijoz_qoshish(self, mijoz):
        key = self._kalit_olish(mijoz.ism)
        self.mijozlar[key] = mijoz
        print(f"Mijoz {mijoz.ism} ro'yxatga olindi.")

    def royxatni_korish(self, tur):
        royxat = self.xodimlar if tur == 'xodim' else self.mijozlar
        sarlavha = "XODIMLAR ROYXATI" if tur == 'xodim' else "MIJOZLAR ROYXATI"

        if not royxat:
            print(f"ℹ️ {sarlavha} bo'sh.")
            return

        print(f"\n--- {sarlavha} ---")
        for key in sorted(royxat.keys()):
            print(f"* {royxat[key]}")
        print("----------------------------")

    def mijozni_xodim_bilan_taminlash(self, mijoz_ismi, xodim_ismi):
        m_key = self._kalit_olish(mijoz_ismi)
        x_key = self._kalit_olish(xodim_ismi)

        mijoz = self.mijozlar.get(m_key)
        xodim = self.xodimlar.get(x_key)

        if not mijoz or not xodim:
            print("Xato: Ism xato kiritildi. Mijoz yoki Xodim topilmadi.")
            return

        if xodim.faol_mijoz:
            print(f"Xodim {xodim.ism} band.")
            return

        xodim.faol_mijoz = mijoz
        print(f"Xodim {xodim.ism} ga mijoz {mijoz.ism} biriktirildi.")

    def avto_sotish(self, marka, model, mijoz_ismi, xodim_ismi):
        avto_key = self._kalit_olish(marka, model)
        x_key = self._kalit_olish(xodim_ismi)

        avto = self.inventar.get(avto_key)
        xodim = self.xodimlar.get(x_key)

        if not avto or not xodim:
            print("Sotuv amalga oshmadi: Mashina yoki Xodim topilmadi.")
            return

        if avto.soni <= 0:
            print(f"Sotuv amalga oshmadi: {avto.marka} {avto.model} omborda yo'q.")
            return


        avto.soni -= 1
        xodim.sotuvlar_soni += 1
        xodim.faol_mijoz = None

        print("\nSOTUV AMALGA OSHDI!")
        print(f"Sotildi: {avto.marka} {avto.model}")
        print(f"Sotuvchi: {xodim.ism} | Xaridor: {mijoz_ismi}")
        print("------------------------------")



class Admin:
    def __init__(self, avtosalon):
        self.avtosalon = avtosalon

    def admin_menyu(self):
        while True:
            print(f"\n======== BOSH MENU - {self.avtosalon.nomi} ========")
            print("1. Mashinalar (Inventar) bo'limi")
            print("2. Xodim va Mijozlarni boshqarish")
            print("3. Avto sotish jarayoni")
            print("4. Dasturdan chiqish")
            print("--------------------------------------------------")

            tanlov = input("Tanlovingizni kiriting (1-4): ")

            if tanlov == '1':
                self._inventar_menyu()
            elif tanlov == '2':
                self._xodim_mijoz_menyu()
            elif tanlov == '3':
                self._sotuv_menyu()
            elif tanlov == '4':
                print("Dastur tugatildi.")
                sys.exit()
            else:
                print("Xato tanlov.")


    def _avto_qoshish_interfeysi(self):
        print("\n--- AVTO QO'SHISH ---")
        marka = input("Markasini kiriting: ")
        model = input("Modelini kiriting: ")
        try:
            narx = float(input("Narxini kiriting (Masalan: 20000): "))
            soni = int(input("Nechta borligini kiriting: "))
            if narx <= 0 or soni <= 0:
                raise ValueError("Narx va soni musbat bo'lishi kerak.")
            yangi_avto = Avto(marka, model, narx, soni)

            self.avtosalon.avto_qoshish(yangi_avto, silent=False)
        except ValueError:
            print("Xato: Narx yoki soni noto'g'ri kiritildi.")

    def _xodim_qoshish_interfeysi(self):
        print("\n--- YANGI XODIM QO'SHISH ---")
        ism = input("Xodim ismini kiriting: ")
        lavozim = input("Lavozimini kiriting (Sotuvchi yoki Menejer): ")
        yangi_xodim = Xodim(ism, lavozim)
        self.avtosalon.xodim_qoshish(yangi_xodim)

    def _mijoz_qoshish_interfeysi(self):
        print("\n--- YANGI MIJOZ QO'SHISH ---")
        ism = input("Mijoz ismini kiriting: ")
        manzil = input("Manzilini kiriting: ")
        yangi_mijoz = Mijoz(ism, manzil)
        self.avtosalon.mijoz_qoshish(yangi_mijoz)


    def _inventar_menyu(self):
        while True:
            print("\n--- INVENTAR BOSHQARUVI ---")
            print("1. Mashina qo'shish/sonini yangilash")
            print("2. Inventarni ko'rish")
            print("3. Orqaga")
            tanlov = input("Tanlovingizni kiriting (1-3): ")
            if tanlov == '1':
                self._avto_qoshish_interfeysi()
            elif tanlov == '2':
                self.avtosalon.inventarni_korish()
            elif tanlov == '3':
                break
            else:
                print("Xato tanlov.")

    def _xodim_mijoz_menyu(self):
        while True:
            print("\n--- XODIM/MIJOZ BOSHQARUVI ---")
            print("1. Yangi xodim qo'shish")
            print("2. Yangi mijoz qo'shish")
            print("3. Xodimlarni ko'rish")
            print("4. Mijozlarni ko'rish")
            print("5. Orqaga")
            tanlov = input("Tanlovingizni kiriting (1-5): ")
            if tanlov == '1':
                self._xodim_qoshish_interfeysi()
            elif tanlov == '2':
                self._mijoz_qoshish_interfeysi()
            elif tanlov == '3':
                self.avtosalon.royxatni_korish('xodim')
            elif tanlov == '4':
                self.avtosalon.royxatni_korish('mijoz')
            elif tanlov == '5':
                break
            else:
                print("Xato tanlov.")

    def _sotuv_menyu(self):
        while True:
            print("\n--- AVTO SOTISH MENYUSI ---")
            print("1. Mijozni Xodimga biriktirish (Kim kim bilan ishlayapti?)")
            print("2. Sotuvni yakunlash")
            print("3. Orqaga")
            tanlov = input("Tanlovingizni kiriting (1-3): ")
            if tanlov == '1':
                self._mijozni_taminlash_interfeysi()
            elif tanlov == '2':
                self._avto_sotish_interfeysi()
            elif tanlov == '3':
                break
            else:
                print("Xato tanlov.")

    def _mijozni_taminlash_interfeysi(self):
        print("\n--- MIJOZNI XODIM BILAN BIRIKTIRISH ---")
        self.avtosalon.royxatni_korish('xodim')
        self.avtosalon.royxatni_korish('mijoz')
        mijoz_ismi = input("\nBiriktiriladigan Mijoz ismini yozing: ")
        xodim_ismi = input("Biriktiriladigan Xodim ismini yozing: ")
        self.avtosalon.mijozni_xodim_bilan_taminlash(mijoz_ismi, xodim_ismi)

    def _avto_sotish_interfeysi(self):
        print("\n--- SOTUVNI YAKUNLASH ---")
        self.avtosalon.inventarni_korish()
        self.avtosalon.royxatni_korish('xodim')
        self.avtosalon.royxatni_korish('mijoz')
        marka = input("\nSotiladigan Avto markasini yozing: ")
        model = input("Sotiladigan Avto modelini yozing: ")
        mijoz_ismi = input("Xaridor Mijoz ismini yozing: ")
        xodim_ismi = input("Sotuvchi Xodim ismini yozing: ")
        self.avtosalon.avto_sotish(marka, model, mijoz_ismi, xodim_ismi)


if __name__ == "__main__":
    salon = Avtosalon("Asosiy Avtosalon")

    salon.avto_qoshish(Avto("Chevrolet", "Tracker", 20000, 5), silent=True)
    salon.avto_qoshish(Avto("Hyundai", "Elantra", 28500, 3), silent=True)

    salon.xodimlar[salon._kalit_olish("Aliyev Nodir")] = Xodim("Aliyev Nodir", "Sotuvchi")
    salon.mijozlar[salon._kalit_olish("Toshmatov Botir")] = Mijoz("Toshmatov Botir", "Toshkent")

    print("\n--- Avtosalon Dasturiga Xush Kelibsiz! ---")

    admin = Admin(salon)
    admin.admin_menyu()