from module_csv import get_all_subjects,get_professor
from module_json import prof_does_exist_in_json_all_students, get_student


def menu_student(student):

    def calculate_average_mark():
        grade_sum = 0.0
        student_copy, dummy = get_student(student["code"], 'broj indeksa')

        student['grades'] = student_copy['ocene']

        num_grades = len(student['grades'])
        for grade in student['grades']:
            grade_sum += float(grade['ocena'])

        print("\nGlobalan prosek ocena je " + str(round(grade_sum/float(num_grades), 2)))

    def show_subjects():
        choice = input(f'\n1.Položeni\n2.Nepoloženi\n\n@Stud.{student["name"]}-->')
        if(len(choice) == 0):
            return

        try:
            choice = int(choice)
        except ValueError:
            print('\nGreska los format!!!')
            return

        all_subjects = get_all_subjects()

        student_done_subjects = student['grades']

        subjects_not_done = []

        subjects_done = []

        for sub in all_subjects:
            done = False
            for stud_sub in student_done_subjects:
                if(stud_sub['sifra_predmeta'] == sub[0]):
                    done = True
                    break
                else:
                    done = False
            if (done == False):
                subjects_not_done.append(sub)
            else:
                subjects_done.append(sub)

        if(choice == 1):
            print('\n\t\tSifra\t\tNaziv')
            for subject in subjects_done:
                print(f'\t\t{subject[0]}\t\t{subject[1]}')
        elif(choice == 2):
            print('\n\t\tSifra\t\tNaziv')
            for subject in subjects_not_done:
                print(f'\t\t{subject[0]}\t\t{subject[1]}')
        else:
            print('\nGreska ne postoji izbor!!!')

    def prof_info():

        all_subjects = get_all_subjects()



        print('\n\t\tSifra\t\tNaziv\n')

        sub_code = ''
        for subject in all_subjects:
            print(f'\t\t{subject[0]}\t\t{subject[1]}')

        try:
            sub_code = int(input(f'\n1.Ukucaj sifru predmeta\n\n@Stud.{student["name"]}-->'))
        except ValueError:
            print('\nGreska los format!!!')
            return

        prof_codes, prof_exists = prof_does_exist_in_json_all_students(sub_code)

        professors = []

        for code in prof_codes:
            prof, i = get_professor(code, 0)
            # If prof code alredy exists in it dont add it
            if(len(professors) != 0):
                for prof_c in professors:
                    add_prof = True
                    if(prof[0] == prof_c[0]):
                        add_prof = False
                    if(add_prof):
                        professors.append(prof)

            else:
                professors.append(prof)


        if(len(professors)>0):
            print("\n\tSifra\tIme\t\tPrezime\t\t\tEmail\t\t\t\t\t\tKonsultacija\n")
            for professor in professors:
                print(f"\t{professor[0]}\t\t{professor[2]}\t{professor[3]}\t\t{professor[4]}\t\t{professor[5]}\n")
        else:
            print("\nNijedan profesor ne predaje taj predmet ili navedena sifra ne ozndacava ni jedan predmet")

    should_run = True
    while (should_run):
        try:
            code = int(input(
                f'\n1.Računaj prosek\n2.Prikaži ispite\n3.Informacije o profesoru predmeta\n4.Povratak na glavni meni\n\n@Stud.{student["name"]}-->'))
        except ValueError:
            print('\nGreska los format!!!')
            continue
        if (code == 1):
            calculate_average_mark()
        if (code == 2):
            show_subjects()
        if (code == 3):
            prof_info()
        if (code == 4):
            print("\nIzlogovanje...")
            break