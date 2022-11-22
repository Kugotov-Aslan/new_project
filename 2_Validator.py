"""

Реализуйте класс Validator, который будет проверять строки.
К примеру, у него будет метод is_email параметром принимает строку и проверяет,
является ли она корректным емейлом или нет. Если является - возвращает true, если не является - то false.
Кроме того, класс будет иметь следующие методы:
метод is_date для проверки даты и метод is_phone для проверки телефона

"""
class Validator:
    def __init__(self, email, date, phone):
        self.email = email
        self.date = date
        self.phone = phone

    def is_email(self):
        import re
        if re.search(r'([a-z0-9. -%]+)@([a-z0-9._-]+\.[a-z]{2,})', self.email):
            return True
        else:
            return False

    def is_date(self):
        import re
        if re.search(r'^([0-2][1-9]|3[0-1])\.(0[0-9]|1[1-2])\.(1[0-9]{3}|2[0-9]{3})$', self.date):
            return True
        else:
            return False

    def is_phone(self):
        import re
        if re.search(r'^(.+7|7|8)[\s|\-]?[0-9]{3}[\s|\-]?[0-9]{3}[\s|\-]?[0-9]{2}[\s|\-]?[0-9]{2}$', self.phone): # либо с пробелом между группами цифр, либо с -
            return True
        else:
            return False

em = Validator(email='sampler0707@gmail.com', date= '21.02.1989', phone='89260550007')

print(Validator.is_email(em))
print(Validator.is_date(em))
print(Validator.is_phone(em))