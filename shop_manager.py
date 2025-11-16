import json
phone={
    '2000000':{
        'model':'huawei',
        'narx':'2000000',
        'yil':'2024',
        'turi':'telefon'
    }
}
tv={
    '4500000':{
        'model':'samsung',
        'narx':'4500000',
        'yil':'2023',
        'turi':'tv'
    }
}
pc={
    '2500000':{
        'model':'lenovo',
        'narx':'2500000',
        'yil':'2019',
        'turi':'pc'
    }
}

def add_phones(d:dict):
    with open('phones.json','w') as f:
        data=json.dump(phone,f,indent=4)
add_phones(phone)

def add_tvs(d:dict):
    with open('tvs.json','w') as f:
        data=json.dump(tv,f,indent=4)
add_tvs(tv)

def add_pcs(d:dict):
    with open('pcs.json','w') as f:
        data=json.dump(pc,f,indent=4)
add_pcs(pc)

def wr_phones(d:dict):
    with open('phones.json','w') as f:
        data=json.dump(d,f,indent=4)

def read_phones():
    s=0
    with open('phones.json','r') as f:
        try:
            s=json.load(f)
            return s
        except:
            return False
read_phones()

def add_phones():
    data=read_phones()
    model=input('model:')
    narx=input('narx:')
    yil=input('yil:')
    turi=input('turi:')
    s={
        narx:{
            'model':model,
            'narx':narx,
            'yil':yil,
            'turi':turi
        }
    }
    if turi=='telefon':
        if data:
            data=dict(data)
            data.update(s)
            wr_phones(data)
        else:
            wr_phones(s)
        print('Yangi telefon qoshildi.')
    else:
        print("turi noto'g'ri kiritilgan")

def view_phones():
    data=read_phones()
    for k,v in data.items():
        print(f'Modeli - {v['model']}. narxi - {k}. yili - {v['yil']}. turi - {v['turi']}')

def wr_tvs(d:dict):
    with open('tvs.json','w') as f:
        data=json.dump(d,f,indent=4)

def read_tvs():
    s=0
    with open('tvs.json','r') as f:
        try:
            s=json.load(f)
            return s
        except:
            return False
read_tvs()

def add_tvs():
    data=read_tvs()
    model=input('model:')
    narx=input('narx:')
    yil=input('yil:')
    turi=input('turi:')
    s={
        narx:{
            'model':model,
            'narx':narx,
            'yil':yil,
            'turi':turi
        }
    }
    if turi=='tv':
        if data:
            data=dict(data)
            data.update(s)
            wr_tvs(data)
        else:
            wr_tvs(s)
        print('Yangi tv qoshildi.')
    else:
        print("turi noto'g'ri kiritilgan")

def view_tvs():
    data=read_tvs()
    for k,v in data.items():
        print(f'Modeli - {v['model']}. narxi - {k}. yili - {v['yil']}. turi - {v['turi']}')

def wr_pcs(d:dict):
    with open('pcs.json','w') as f:
        data=json.dump(d,f,indent=4)

def read_pcs():
    s=0
    with open('pcs.json','r') as f:
        try:
            s=json.load(f)
            return s
        except:
            return False
read_pcs()

def add_pcs():
    data=read_pcs()
    model=input('model:')
    narx=input('narx:')
    yil=input('yil:')
    turi=input('turi:')
    s={
        narx:{
            'model':model,
            'narx':narx,
            'yil':yil,
            'turi':turi
        }
    }
    if turi=='pc':
        if data:
            data=dict(data)
            data.update(s)
            wr_pcs(data)
        else:
            wr_pcs(s)
        print('Yangi pc qoshildi.')
    else:
        print("turi noto'g'ri kiritilgan")

def view_pcs():
    data=read_pcs()
    for k,v in data.items():
        print(f'Modeli - {v['model']}. narxi - {k}. yili - {v['yil']}. turi - {v['turi']}')

while True:
    def menu_manager():
        kod=input(f'1.Telefonlar \n2.Televizorlar \n3.PC lar ')
        if kod=='1':
            while True:
                kod1=input(f'1.Mavjud telefonlarni korish \n2.Yangi telefon qoshish \n3.Bosh menyuga qaytish ')
                if kod1=='1':
                    view_phones()
                elif kod1=='2':
                    add_phones()
                else:
                    menu_manager()
        elif kod=='2':
            while True:
                kod2=input(f'1.Mavjud televizorlarni korish \n2.Yangi televizor qoshish \n3.Bosh menyuga qaytish ')
                if kod2=='1':
                    view_tvs()
                elif kod2=='2':
                    add_tvs()
                else:
                    menu_manager()
        elif kod=='3':
            while True:
                kod3=input(f'1.Mavjud PC larni korish \n2.Yangi PC qoshish \n3.Bosh menyuga qaytish ')
                if kod3=='1':
                    view_pcs()
                elif kod3=='2':
                    add_pcs()
                else:
                    menu_manager()
    menu_manager()














