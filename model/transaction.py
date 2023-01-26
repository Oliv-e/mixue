import model.database as database
from helper import *
from datetime import datetime
# import os


def start():
    selected_menu = None
    not_found = False
    orderData = []
    while True:
        # select tipe menu
        clearScreen()
        if selected_menu is None:
            menu_type = {
                '1': 'ice_cream',
                '2': 'original_tea',
                '3': 'real_fruit_tea',
                '4': 'milk_tea'
            }
            for i in menu_type:
                print(f'{i}. {snakeToTitle(menu_type[i])}')

            selected_menu = intInput("Pilih jenis menu : ", ['1', '2', '3', '4'])

        if (not_found):
            print("Produk tidak ditemukan!")

        # print products
        db = menu_type[str(selected_menu)]
        products = database.createList(db)
        print(f'\nProduk {snakeToTitle(menu_type[str(selected_menu)])} : ')
        print('=' * 55)
        for i in range(len(products)):
            v = products[i]
            val = f'{v[0]:8} {v[1]}'
            print(f'{val:40}', priceFormat(int(v[2])))

        code = input("Pilih code produk : ")
        clearScreen()

        product = database.search(db, 'code', code)
        if product:
            not_found = False
            amount = intInput("Masukkan jumlah pesanan : ")
            product['amount'] = amount
            orderData.append(product)

            print('1. Tambah menu lain')
            print('2. Cetak invoice')
            act = intInput("Pilih aksi : ", ['1', '2'])
            if act == 1:
                selected_menu = None
            elif act == 2:
                printInvoice(orderData)
                input("\nTekan enter untuk melanjutkan.")
                clearScreen()
                break
        else:
            not_found = True


def printInvoice(orderData):
    print('')
    totalPrice = 0
    for i in range(len(orderData)):
        order = orderData[i]
        price = order['price']
        amount = order['amount']
        totalPrice += (price * amount)

    print("Total :", priceFormat(totalPrice))
    uang = intInput("\nMasukkan uang customer : ", min_amount=totalPrice)
    if uang < totalPrice:
        print("Kurang")
    else:
        clearScreen()
        today = datetime.now()
        tanggal = today.strftime('%Y-%m-%d %H:%M:%S')

        print('=' * 75)
        print(f'{"MIXUE":^75}')
        print(f'{"PontianakTo go":^75}')
        print(generateRandom(15))
        print(tanggal)
        print('=' * 75)

        print(
            f'{"Code":8} {"Item":30} {"Price":10} {"QTY":^8} {"AMT":^15}')
        print('-' * 75)
        kembalian = uang - totalPrice
        for i in range(len(orderData)):
            order = orderData[i]
            price = order['price']
            amount = order['amount']
            print(
                f'{order["code"]:8} {order["name"]:30} {priceFormat(int(price)):10} {amount:^8} {priceFormat(price * amount):^15}')

        print('-' * 75)
        print(f'{"Total Amount":<60}', ':', priceFormat(totalPrice))
        print(f'{"Cash":<60}', ':', priceFormat(uang))
        print(f'{"Change":<60}', ':', priceFormat(kembalian))
        print(f'\n{"Address : "}',
              "Jl. Jendral Ahmad Yani No. 4, Kec. Pontianak Selatan, Pontianak")
        print(f'\n{"Tel : "}',
              "+62 851 6121 4171")
        print(f'{"Cashier : "}', "Oliver Dillon")
        print('=' * 75)
