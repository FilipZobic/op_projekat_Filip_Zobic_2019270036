import json
import os


def get_path_data(filename):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(file_dir)
    new_path = os.path.join(parent_dir, f'data/{filename}')
    return new_path


def get_student(value, attribute_name):

    new_path = get_path_data("studenti.json")

    user = {}
    student_found = False

    with open(new_path, "r") as json_file:
        students = json.load(json_file)
        for stud in students:
            if(value == stud[attribute_name]):
                user = stud
                student_found = True
                break
    json_file.close()
    return user, student_found


def students_contains_string_in_name(string):

    new_path = get_path_data("studenti.json")

    string = string.lower()
    students_found = False
    student_list = []

    with open(new_path, "r") as json_file:
        students = json.load(json_file)
        for stud in students:
            name_to_be_checked = stud['ime'].lower()
            if(string in name_to_be_checked):
                student_list.append(stud)
                students_found = True
    json_file.close()

    return student_list, students_found


# Saves data to file
def write_json(data, filename):
        with open(filename,'w') as f:
            json.dump(data, f, indent=6)
        f.close()


def register_student(index, password, name, surname, email):

    new_path = get_path_data("studenti.json")

    student = {
        "broj indeksa": index,
        "lozinka": password,
        "ime": name,
        "prezime": surname,
        "email": email,
        "ocene": []
    }
    with open(new_path) as json_file:
        data = json.load(json_file)
        temp = data
        temp.append(student)
    write_json(data,new_path)

    json_file.close()


def update_student(student):

    new_path = get_path_data("studenti.json")

    with open(new_path) as json_file:
        data = json.load(json_file)
        temp = data
        i = 0
        while(True):
            if(temp[i]['broj indeksa'] == student['broj indeksa']):
                temp[i] = student
                break
            i = i + 1
    write_json(data, new_path)

    json_file.close()


def prof_does_exist_in_json_all_students(sub_code):

    new_path = get_path_data("studenti.json")

    sub_code = str(sub_code)
    professor_found = False

    prof_codes = []

    with open(new_path, "r") as json_file:
        students = json.load(json_file)
        for stud in students:
            for stud_subj in stud['ocene']:
                if(str(sub_code) == stud_subj["sifra_predmeta"]):
                    if("sifra_profesora" in stud_subj):
                        if(len(stud_subj["sifra_profesora"])!=0):
                            will_add = True
                            for prof_code in prof_codes:
                                if(stud_subj["sifra_profesora"] == prof_code):
                                    will_add = False
                            if(will_add == True):
                                prof_codes.append(stud_subj["sifra_profesora"])


    json_file.close()

    if(len(prof_codes)>0):
        professor_found = True
    else:
        professor_found = False

    return prof_codes, professor_found
