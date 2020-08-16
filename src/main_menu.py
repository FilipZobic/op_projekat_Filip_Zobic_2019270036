from login import login
from register import register

def main_menu():
    while(True):
        selection = input('\n1. Prijava na sistem\n2. Registracija\n3. Izlazak iz aplikacije\n\n@-->')
        if(selection=='1'):
            login()
        elif(selection=='2'):
            register()
        elif(selection=='3'):
            print('\nIzlazak iz aplikacije...')
            exit()
        else:
            print("\nGreska!!! Unesi jednu od ponudjenih opcija")
            continue

# Program Start


main_menu()


# ==============
