class Product:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year


class Shop:
    def __init__(self,title,phone):
        self.title = title
        self.phone = phone
        self.baza= []

    def add_water(self):
        title=input('Title')
        price=int(input('Price'))
        year=int(input('Year'))
        p1=Product(title,price,year)
        p1.type = 'water'
        self.baza.append(p1)

    def add_food(self):
        title=input('Title')
        price=int(input('Price'))
        year=int(input('Year'))
        p2=Product(title,price,year)
        p2.type = 'food'
        self.baza.append(p2)

    def add_parfums(self):
        title=input('Title')
        price=int(input('Price'))
        year=int(input('Year'))
        p3=Product(title,price,year)
        p3.type = 'parfums'
        self.baza.append(p3)

    def view_all(self):
        for item in self.baza:
            print(f'title:{item.title},price:{item.price},year:{item.year} type: {item.type}')

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

shop1=Shop('shop1',1234567)


def shop_manager(shop:Shop):
    while True:
        kod = input('1. add water \n 2. add food \n 3. add parfums \n 4. view all \n 5. edit product \n 6. delete product \n 7. break')
        if kod == '1':
            shop.add_water()
        elif kod == '2':
            shop.add_food()
        elif kod == '3':
            shop.add_parfums()
        elif kod == '4':
            shop.view_all()
        elif kod == '5':
            shop.edit_product()
        elif kod == '6':
            shop.delete_product()
        else:
            break
shop_manager(shop1)