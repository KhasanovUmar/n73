class Product:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year


class Phone(Product):
    def __init__(self, title, price, year, display, ram):
        super().__init__(title, price, year)
        self.display = display
        self.ram = ram
        self.type = "phone"


class TV(Product):
    def __init__(self, title, price, year, diagonal, smart):
        super().__init__(title, price, year)
        self.diagonal = diagonal
        self.smart = smart
        self.type = "tv"


class PC(Product):
    def __init__(self, title, price, year, cpu, gpu):
        super().__init__(title, price, year)
        self.cpu = cpu
        self.gpu = gpu
        self.type = "pc"


class Shop:
    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.baza = []


    def add_phone(self):
        title = input("Title: ")
        price = int(input("Price: "))
        year = int(input("Year: "))
        display = input("Display: ")
        ram = input("RAM (GB): ")

        p = Phone(title, price, year, display, ram)
        self.baza.append(p)


    def add_tv(self):
        title = input("Title: ")
        price = int(input("Price: "))
        year = int(input("Year: "))
        diagonal = input("Diagonal: ")
        smart = input("Smart? (ha/yoq): ")

        t = TV(title, price, year, diagonal, smart)
        self.baza.append(t)


    def add_pc(self):
        title = input("Title: ")
        price = int(input("Price: "))
        year = int(input("Year: "))
        cpu = input("CPU: ")
        gpu = input("GPU: ")

        c = PC(title, price, year, cpu, gpu)
        self.baza.append(c)


    def view_all(self):
        for item in self.baza:
            print(
                f"title: {item.title}, price: {item.price}, year: {item.year}, type: {item.type}"
            )

    def delete_product(self):
        title = input("O'chirmoqchi bo'lgan product title: ")
        for item in self.baza:
            if item.title == title:
                self.baza.remove(item)
                print("O'chirildi")
                return
        print("Topilmadi")


    def edit_product(self):
        title = input("Tahrirlash uchun product title: ")

        for item in self.baza:
            if item.title == title:
                print("Yangi qiymatlarni kiriting :")

                n_title = input(f"Title ({item.title}): ") or item.title
                n_price = input(f"Price ({item.price}): ")
                n_year = input(f"Year ({item.year}): ")

                item.title = n_title
                item.price = int(n_price) if n_price else item.price
                item.year = int(n_year) if n_year else item.year

                print("Tahrirlandi")
                return

        print("Topilmadi")


shop1 = Shop("shop1", 1234567)


def shop_manager(shop: Shop):
    while True:
        kod = input(
            "1. add phone\n2. add tv\n3. add pc\n4. view all\n5. edit product\n6. delete product\n7. break\n"
        )
        if kod == "1":
            shop.add_phone()
        elif kod == "2":
            shop.add_tv()
        elif kod == "3":
            shop.add_pc()
        elif kod == "4":
            shop.view_all()
        elif kod == "5":
            shop.edit_product()
        elif kod == "6":
            shop.delete_product()
        else:
            break


shop_manager(shop1)
