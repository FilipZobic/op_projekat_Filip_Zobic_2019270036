from professor import Prof
from student import Stud
from module_csv import get_professor
from module_json import get_student

def login():

    def professor_login(code):
        data_valid = False
        data,user_exists = get_professor(code,0)
        if(user_exists==True):
            username = input('\nUnesi korisničko ime:\n\n@-->')
            if(username==data[2]):
                data_valid = True
            else:
                print("Pogrešno korisničko ime!!!")
                data_valid = False
            if(data_valid==True):
                password = input(f'\nUnesi lozinku\n\n@Prof.{data[2]}-->')
                if(password==data[1]):
                    print(f'\n@Prof.{data[2]}-->Dobrodošli')
                    data_valid = True
                else:
                    print("\nPogrešna lozinka!!!")
                    data_valid = False
            if(data_valid):
                # setujemo dictionary ovde sa key valuima
                user = Prof(data[0], data[1], data[2], data[3], data[4], data[5])
                user.menu_user()
        return user_exists

    def student_login(index):
        data_valid = False
        student, user_exists = get_student(index, 'broj indeksa')
        if(user_exists == True):
            username = input('\nUnesi korisničko ime:\n\n@-->')
            if(username == student['ime']):
                data_valid = True
            else:
                print("\nPogrešno korisničko ime!!!")
                data_valid = False
            if(data_valid==True):
                password = input(f'\nUnesi lozinku\n\n@Stud.{student["ime"]}-->')
                if(password==student['lozinka']):
                    print(f'\n@Stud.{student["ime"]}-->Dobrodošli')
                    data_valid = True
                else:
                    print("Pogrešna lozinka!!!")
                    data_valid = False
            if(data_valid):
                user = Stud(student['broj indeksa'],student['lozinka'],student['ime'],student['broj indeksa'],student['prezime'],student['ocene'])
                # saljemo dictionary u menu_user metodu i tu sve menjamo
                user.menu_user()
            
        return user_exists
        
    try:
        code = int(input('\nUnesi šifru ili indeks:\n\n@-->'))
    except ValueError:
        print('\nGreska los format!!!')
        return
    codes = str(code)

    user_found = professor_login(codes)
    if(user_found==False):
        user_found = student_login(code)
        if(user_found==False):
            print("\nKorisnik ne postoji")