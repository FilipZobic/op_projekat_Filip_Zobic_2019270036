from user import User

from module_csv import get_professor,get_all_subjects,update_professor

from module_json import students_contains_string_in_name,get_student,update_student


def menu_professor(professor):

    def print_subjects(subjects):
        i = 1
        for sub in subjects:
            print(f"\t{i}.\t{sub[0]}\t{sub[1]}")
            i = i + 1

    def add_grade():
        print("\nPretrazi studente prema imenu")
        name = input(f'\nProf.@{professor["name"]}-->')
        student_list, students_exist = students_contains_string_in_name(name)

        if (students_exist):
            #
            i = 1
            for stud_object in student_list:
                print(f'\t\n{i}. {stud_object["broj indeksa"]} - {stud_object["ime"]} - {stud_object["prezime"]}')
                i = i + 1

            id = 0

            try:
                id = int(input(f'\nIzaberi studenta preko indexa\n\nProf.@{professor["name"]}-->'))
            except ValueError:
                id = 0
                print('\nGreska los format!!!')
                return

            user = {}
            user_match = False
            if (id != 0):
                # FindMatch
                user, user_match = get_student(id, "broj indeksa")
            #

            if (user_match == False):
                print("\nNema takvih studenata!")
            else:  # Student found
                all_subjects = get_all_subjects()

                will_loop = True
                subject_code = 0
                while (will_loop):
                    print("\n\tBr.\tSifra\tPredmet\n")
                    print_subjects(all_subjects)
                    subject_code = input(f'\nIzaberi predmet pomocu sifre predmeta.\n\nProf.@{professor["name"]}-->')
                    if (len(subject_code) == 0):
                        return
                    try:
                        subject_code = int(subject_code)
                    except ValueError:
                        print('\nGreska los format!!!')
                        continue
                    for subject in all_subjects:
                        if (subject_code == int(subject[0])):
                            will_loop = False
                            break
                    if (will_loop == True):
                        print("\nNe postojeci predmet.\n")
                        print_subjects(all_subjects)
                will_loop = True
                grade = 0

                while (will_loop):
                    grade = input(f'\nIzaberi ocenu od 5 - 10\n\nProf.@{professor["name"]}-->')
                    if (len(grade) == 0):
                        return
                    try:
                        grade = int(grade)
                    except ValueError:
                        print('\nGreska los format!!!')
                        continue
                    if (5 <= grade and 10 >= grade):
                        will_loop = False
                    else:
                        print("\nOut of bounds")

                new_grade = {'sifra_predmeta': str(subject_code), 'sifra_profesora': str(professor['code']),
                             'ocena': int(grade)}

                print("\nOcena uspesno dodata.")

                user['ocene'].append(new_grade)

                update_student(user)

        else:
            print("\nNema takvih studenata")

    def delete_grade():
        print("\nPretrazi studente prema imenu")
        name = input(f'\nProf.@{professor["name"]}-->')
        student_list, students_exist = students_contains_string_in_name(name)

        if (students_exist):
            #
            i = 1
            for stud_object in student_list:
                print(f'\t\n{i}. {stud_object["broj indeksa"]} - {stud_object["ime"]} - {stud_object["prezime"]}')
                i = i + 1

            id = 0

            try:
                id = int(input(f'\nIzaberi studenta preko indexa\n\nProf.@{professor["name"]}-->'))
            except ValueError:
                id = 0
                print('\nGreska los format!!!')

            user = {}
            user_match = False
            if (id != 0):
                # FindMatch
                user, user_match = get_student(id, "broj indeksa")
            #

            if (user_match == False):
                print("\nNema takvih studenata!")
            else:  # Student found
                professors_grades = []
                if (len(user['ocene']) == 0):
                    print("\nStudent jos nema ocenu")
                    return
                i = 0
                for grade in user['ocene']:
                    if (grade['sifra_profesora'] == professor["code"]):
                        grade['id'] = i
                        professors_grades.append(grade)
                        i = i + 1
                    else:
                        i = i + 1

                if (len(professors_grades) == 0):
                    print("\nStudent nema ocenu od ulogovanog profesora.")
                    return

                print("\n\tBr.\tSifra\tOcena")
                i = 1
                for grade in professors_grades:
                    print(f"\n\t{i}.\t{grade['sifra_predmeta']}\t\t{grade['ocena']}")
                    i = i + 1
                will_loop = True
                choice = -1
                while (will_loop):
                    choice = input(f'\nIzaberi ocenu za brisanje\n\nProf.@{professor["name"]}-->')
                    if (len(choice) == 0):
                        return
                    try:
                        choice = int(choice)
                    except ValueError:
                        print('\nGreska los format!!!')
                        continue
                    i = i - 1
                    if (1 == choice or i >= choice):
                        will_loop = False
                    else:
                        print("\nOut of bounds")
                        return

                choice = choice - 1

                pop_id = professors_grades[choice]["id"]

                user['ocene'].pop(pop_id)

                update_student(user)

        else:
            print("\nNema takvih studenata!")

    def subject_average():

        all_students, i = students_contains_string_in_name('')
        all_subjects = get_all_subjects()
        professor_code = professor['code']

        will_loop = True
        choice = -1

        selected_subject = []

        while (will_loop):

            print("\n\tBr.\tSifra\tPredmet\n")
            print_subjects(all_subjects)
            choice = input(f'\nIzaberi predmet pomocu rednog broja\n\nProf.@{professor["name"]}-->')
            if (len(choice) == 0):
                return
            try:
                choice = int(choice)
            except ValueError:
                print('\nGreska los format!!!')
                continue
            if (1 <= choice and len(all_subjects) >= choice):
                choice = choice - 1
                selected_subject = all_subjects[choice]
                will_loop = False
            else:
                print("\nOut of bounds")

        sum = 0.0

        i = 0.0
        for student in all_students:
            for grade in student['ocene']:
                if (grade['sifra_predmeta'] == selected_subject[0] and grade['sifra_profesora'] == professor_code):
                    i = i + 1.0
                    sum = sum + float(grade['ocena'])

        try:
            average = sum / i
        except ZeroDivisionError:
            print("\nProfesor ne predaje taj predmet")
            return

        print(f"\nProsek svih studenata za {selected_subject[1]}: {str(round(average, 2))}")

    def change_consultation_time():
        print('\n' + professor['consultation_time'])
        consultation_time = input(f"\nPromeni termin:\n\nProf.@{professor['name']}-->")

        if (len(consultation_time) != 0):
            schedule = consultation_time
            update_professor(professor['code'], schedule)
            professor['consultation_time'] = schedule

    should_run = True
    while (should_run):
        try:
            code = int(input(
                f'\n1.Dodaj ocenu\n2.Izbriši ocenu\n3.Prosek predmeta\n4.Termini konsultacija\n5.Povratak na glavni meni\n\nProf.@{professor["name"]}-->'))
        except ValueError:
            print('\nGreska los format!!!')
        if (code == 1):
            add_grade()
        if (code == 2):
            delete_grade()
        if (code == 3):
            subject_average()
        if (code == 4):
            change_consultation_time()
        if (code == 5):
            print("\nIzlogovanje....")
            break