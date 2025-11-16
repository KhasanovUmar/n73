students={
    '+998999999999':{
        'name':'Ali',
        'phone':'+998999999999',
        'age':12,
        'email':'test@gmail.com'
    },
    '+998999999998':{
        'name':'Vali',
        'phone':'+998999999998',
        'age':14,
        'email':'test2@gmail.com'
    }
}
c=r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
e=r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
def add_student(d: dict):
    name=input('name:')
    phone=input('phone:')
    age=input('age:')
    email=input('email:')
    s={
        phone:{
            'name':name,
            'phone':phone,
            'age':age,
            'email':email
    }}
    import re
    if re.match(c,phone) and re.match(e,email):
        d.update(s)
    else:
        print("Formatlar to'g'ri kiritilganligini tekshiring")
def view_student(d:dict):
    for k,v in d.items():
        print(f'id:{k}. name:{v['name']}. phone:{v['phone']}. email:{v['email']}')

def student_manager(d:dict):
    while True:
        kod=input('1. view student \n2. add student \n3. break ')
        if kod=='1':
            view_student(d)
        elif kod=='2':
            add_student(d)
        else:break
student_manager(students)


















