import os
import csv
from csv import writer
from tempfile import NamedTemporaryFile
import shutil


def get_path_data(filename):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(file_dir)
    new_path = os.path.join(parent_dir, f'data/{filename}')

    return new_path


def get_professor(code, i):
    new_path = get_path_data('profesori.csv')

    code_exists = False

    with open(new_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='-')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                if (row[i] == str(code)):
                    code_exists = True
                    break
                line_count += 1
            else:
                line_count += 1
    csv_file.close()
    return row, code_exists


def register_prof(index, password, name, surname, email, schedule):
    new_path = get_path_data('profesori.csv')

    professor = []
    professor.extend([index, password, name, surname, email, schedule])

    with open(new_path, 'a+', newline='') as csv_file:
        csv_writer = writer(csv_file, delimiter='-')
        csv_writer.writerow(professor)

    csv_file.close()


def update_professor(code, new_consultation_time):
    new_path = get_path_data('profesori.csv')

    tempfile = NamedTemporaryFile(mode='w', delete=False)

    with open(new_path, 'r') as csv_file, tempfile:
        reader = csv.DictReader(csv_file, delimiter='-',
                                fieldnames=['sifra', 'lozinka', 'ime', 'prezime', 'email', 'terminKonsultacija'])
        csv_writer = writer(tempfile, delimiter='-')

        for row in reader:
            if (str(row['sifra']) == str(code)):
                row['terminKonsultacija'] = new_consultation_time

            row = [row['sifra'], row['lozinka'], row['ime'], row['prezime'], row['email'], row['terminKonsultacija']]
            csv_writer.writerow(row)

    shutil.move(tempfile.name, new_path)
    csv_file.close()


def get_all_subjects():
    new_path = get_path_data('predmeti.csv')

    subjects = []

    with open(new_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            if (line_count != 0):
                subjects.append(row)
                line_count += 1
            else:
                line_count += 1

    csv_file.close()
    return subjects
