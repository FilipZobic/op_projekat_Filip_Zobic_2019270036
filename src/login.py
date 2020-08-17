from professor import menu_professor
from student import menu_student
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
                professor = {"code": data[0], "password": data[1], "name": data[2], "surname": data[3], "email": data[4], "consultation_time": data[5]}
                menu_professor(professor)
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
                #saljem njega u menu
                student = {"code": student['broj indeksa'], "password": student['lozinka'],
                           "name": student['ime'], "surname": student['prezime'], "email": student['email'], "grades": student['ocene']};
                menu_student(student)
            
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