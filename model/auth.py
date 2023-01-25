import model.database as database


def login():
    username = input("Username : ")
    password = input("Password : ")
    cashier = database.search('cashier', 'username', username)
    if cashier:
        if cashier['password'] == password:
            return cashier

    print("Username atau password salah!")
    return login()
