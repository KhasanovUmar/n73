class User:
    def __init__(self, name, phone, seria, age, username, password):
        self.name = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.username = username
        self._password = password
        self.role = "user"

    def check_password(self, p):
        return self._password == p

    def menu(self, park):
        pass


class Admin(User):
    def __init__(self, name, phone, seria, age, username, password):
        super().__init__(name, phone, seria, age, username, password)
        self.role = "admin"

    def edit_user(self, park):
        for i, u in enumerate(park.users):
            print(i, u.name, u.role)
        tan = input("Tahrir ID: ")
        if not tan.isdigit() or int(tan) >= len(park.users):
            print("Noto‘g‘ri ID")
            return
        u = park.users[int(tan)]
        print("1. Name\n2. Phone\n3. Seria\n4. Age")
        f = input("Qaysi qism? ")
        if f == "1":
            u.name = input("Yangi name: ")
        elif f == "2":
            u.phone = input("Yangi phone: ")
        elif f == "3":
            u.seria = input("Yangi seria: ")
        elif f == "4":
            u.age = input("Yangi age: ")
        else:
            print("Noto‘g‘ri tanlov")
            return
        print("Ma’lumot yangilandi.")

    def delete_user(self, park):
        for i, u in enumerate(park.users):
            print(i, u.name, u.role)
        tan = input("O'chirish ID: ")
        if tan.isdigit() and int(tan) < len(park.users):
            park.users.pop(int(tan))
            print("O‘chirildi.")
        else:
            print("Noto‘g‘ri ID")

    def add_user(self, park):
        print("1. Admin qo'shish\n2. Driver qo'shish")
        t = input("Tanlov: ")
        name = input("Ism: ")
        phone = input("Phone: ")
        seria = input("Seria: ")
        age = input("Yosh: ")
        username = input("Login: ")
        password = input("Parol: ")
        if t == "1":
            park.users.append(Admin(name, phone, seria, age, username, password))
            print("Admin qo‘shildi.")
        elif t == "2":
            park.users.append(Driver(name, phone, seria, age, username, password))
            print("Driver qo‘shildi.")
        else:
            print("Noto‘g‘ri tanlov.")

    def edit_car(self, park):
        for i, c in enumerate(park.cars):
            print(i, c.model, c.brand, c.year)
        tan = input("Tahrir ID: ")
        if not tan.isdigit() or int(tan) >= len(park.cars):
            print("Noto‘g‘ri ID")
            return
        c = park.cars[int(tan)]
        print("1. Model\n2. Brand\n3. Year\n4. Seria")
        f = input("Qaysi qism? ")
        if f == "1":
            c.model = input("Yangi model: ")
        elif f == "2":
            c.brand = input("Yangi brand: ")
        elif f == "3":
            c.year = input("Yangi year: ")
        elif f == "4":
            c.seria = input("Yangi seria: ")
        else:
            print("Noto‘g‘ri tanlov")
            return
        print("Mashina yangilandi.")

    def delete_car(self, park):
        for i, c in enumerate(park.cars):
            print(i, c.model, c.brand)
        tan = input("O'chirish ID: ")
        if tan.isdigit() and int(tan) < len(park.cars):
            park.cars.pop(int(tan))
            print("O‘chirildi.")
        else:
            print("Noto‘g‘ri ID")

    def delete_order(self, park):
        for i, o in enumerate(park.orders):
            print(i, "User:", o.user_id, "Car:", o.car_id, o.date_start, o.date_end)
        tan = input("O'chirish ID: ")
        if tan.isdigit() and int(tan) < len(park.orders):
            park.orders.pop(int(tan))
            print("Buyurtma o‘chirildi.")
        else:
            print("Noto‘g‘ri ID")

    def menu(self, park):
        while True:
            print("\n--- ADMIN PANEL ---")
            print("1. Mashina qo'shish")
            print("2. Mashinalar")
            print("3. Foydalanuvchilar")
            print("4. Buyurtmalar")
            print("5. Foydalanuvchi tahrirlash")
            print("6. Mashina tahrirlash")
            print("7. Foydalanuvchi o‘chirish")
            print("8. Mashina o‘chirish")
            print("9. Buyurtma o‘chirish")
            print("10. Yangi foydalanuvchi qo‘shish")
            print("0. Chiqish")
            tan = input("Tanlov: ")
            if tan == "1":
                model = input("Model: ")
                brand = input("Brand: ")
                year = input("Yili: ")
                seria = input("Seria: ")
                park.cars.append(Car(model, brand, year, seria))
                print("Mashina qo‘shildi.")
            elif tan == "2":
                for i, car in enumerate(park.cars):
                    print(i, car.model, car.brand, car.year)
            elif tan == "3":
                for u in park.users:
                    print(u.name, u.role)
            elif tan == "4":
                for o in park.orders:
                    print(o.user_id, o.car_id, o.date_start, "->", o.date_end)
            elif tan == "5":
                self.edit_user(park)
            elif tan == "6":
                self.edit_car(park)
            elif tan == "7":
                self.delete_user(park)
            elif tan == "8":
                self.delete_car(park)
            elif tan == "9":
                self.delete_order(park)
            elif tan == "10":
                self.add_user(park)
            elif tan == "0":
                break


class Driver(User):
    def __init__(self, name, phone, seria, age, username, password):
        super().__init__(name, phone, seria, age, username, password)
        self.role = "driver"

    def menu(self, park):
        while True:
            print("\n--- DRIVER PANEL ---")
            print("1. Mashinalar")
            print("2. Buyurtma berish")
            print("3. Buyurtmalarim")
            print("0. Chiqish")
            tan = input("Tanlov: ")
            if tan == "1":
                for i, car in enumerate(park.cars):
                    print(i, car.model, car.brand, car.year)
            elif tan == "2":
                cid = input("Mashina ID: ")
                if cid.isdigit() and int(cid) < len(park.cars):
                    start = input("Boshlanish sana: ")
                    end = input("Tugash sana: ")
                    park.orders.append(Order(self.username, int(cid), start, end))
                    print("Buyurtma qabul qilindi.")
                else:
                    print("Xato ID")
            elif tan == "3":
                for o in park.orders:
                    if o.user_id == self.username:
                        car = park.cars[o.car_id]
                        print(car.model, o.date_start, "->", o.date_end)
            elif tan == "0":
                break


class Car:
    def __init__(self, model, brand, year, seria):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria


class Order:
    def __init__(self, user_id, car_id, date_start, date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end


class Park:
    def __init__(self, title):
        self.title = title
        self.users = []
        self.cars = []
        self.orders = []


def park_manager(park):
    while True:
        u = input("Login: ")
        p = input("Parol: ")
        found = None
        for x in park.users:
            if x.username == u and x.check_password(p):
                found = x
                break
        if found:
            print("Xush kelibsiz,", found.name)
            found.menu(park)
        else:
            print("Login yoki parol xato.")


park = Park("AutoPark")
park.users.append(Admin("Admin", "000", "AA", 30, "admin", "123"))
park.users.append(Driver("Ali", "111", "BB", 22, "ali", "111"))
park_manager(park)
