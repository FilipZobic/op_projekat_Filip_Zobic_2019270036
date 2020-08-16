from module_csv import get_professor,register_prof
from module_json import get_student,register_student


def min_length(target_word, min_len):
    if(len(target_word) < min_len):
        return True
    else:
        return False


def input_basic(user_type):
    collection = []

    name = input(f'\nIme:\n\n@{user_type}-->')

    if (min_length(name, 3)):
        print("\nPrekratko ime, minimum 3 slova!")
        return []

    collection.append(name)

    surname = input(f'\nPrezime:\n\n@{user_type}-->')

    if (min_length(surname, 3)):
        print("\nPrekratko prezime, minimum 3 slova!")
        return []

    collection.append(surname)

    password = input(f'\nLozinka:\n\n@{user_type}-->')
    if (min_length(password, 3)):
        print("\nPrekratka lozinka minimum, 3 karaktera!")
        return []

    collection.append(password)

    password_check = input(f'\nPotvrdi lozinku:\n\n@{user_type}-->')
    if (password != password_check):
        print("Lozinke se ne poklapaju")
        return []

    email = input(f'\nEmail:\n\n@{user_type}-->')
    if ('@' not in email):
        print("\nLoš format fali @")
        return []

    collection.append(email)

    return collection


def register():
    
    while(True):
        choice = input('\n==Registruj:\n\n1.Student\n2.Profesor\n3.Glavni meni\n\n@-->')
        if(choice=='1'):
            try:
                index = int(input(f'\nBroj indeksa:\n\n@Stud-->'))
            except ValueError:
                print("\nLoš format!!!")
                continue
            not_used, user_exists = get_student(index,'broj indeksa')
            if(user_exists):
                print("\nJedan student je već registrovan na taj indeks")
                continue
            else:
                not_used,user_exists = get_professor(str(index), 0)
                if(user_exists):
                    print("\nProfesor je registrovan na tu sifru")
                    continue

            arr = input_basic("Stud")

            if(len(arr) == 0):
                continue

            name = arr[0]
            surname = arr[1]
            password = arr[2]
            email = arr[3]

            register_student(index, password, name, surname, email)
            print("\nRegistracija uspesno obavljena.")

        elif(choice=='2'):
            try:
                index = int(input('\nŠifra:\n\n@Prof-->'))
            except ValueError:
                print("\nLoš format!!!")
                continue
            not_used,user_exists = get_student(index,'broj indeksa')
            if(user_exists):
                print("\nJedan student je već registrovan na taj indeks")
                continue
            else:
                not_used, user_exists = get_professor(str(index),0)
                if(user_exists):
                    print("\nProfesor je registrovan na tu sifru")
                    continue

            arr = input_basic("Prof")

            if (len(arr) == 0):
                continue

            name = arr[0]
            surname = arr[1]
            password = arr[2]
            email = arr[3]


            schedule = input('\nTermin konsultacija:\n\n@Prof-->')

            register_prof(index, password, name, surname, email, schedule)
            print("\nRegistracija uspesno obavljena.")

        elif(choice == '3'):
            break
        else:
            print("\nIzaberi jednu od navedenih opcija")
