class User:
    
    code = ''
    password = ''
    name = ''
    surname = ''
    email = ''
    
    def __init__(self, code, password, name, surname, email):
        self.code = code
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
