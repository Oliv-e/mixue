# import model.database as database
import model.transaction as transaction
from helper import *

print("Selamat datang di Kasir Mixue")
# todo : fitur login (untuk nama kasir)
action = ['buat transaksi']

firstLoad = True
action_number = None
while (action_number in range(1, len(action) + 1)) or firstLoad:
    for i in range(len(action)):
        print(f'{i+1}. {action[i].title()}')

    action_number = intInput("Pilih aksi : ")

    clearScreen()

    if action_number == 1:
        transaction.start()

    action_number = 1
    firstLoad = False
